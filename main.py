#import necessary requirements 

import re 
import spacy  
from transformers import pipeline  
from flask import Flask, request, jsonify, render_template  
from werkzeug.utils import secure_filename  
import os  
from PyPDF2 import PdfReader  

# Load spaCy's pre-trained model for NLP tasks
nlp = spacy.load("en_core_web_sm")

# Load zero-shot classification model from Hugging Face Transformers
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", clean_up_tokenization_spaces=True)

# Define categories for customer requirements, company policies, and customer objections
customer_requirements = {
    "Car Type": ["Hatchback", "SUV", "Sedan", "Compact SUV"],
    "Fuel Type": ["Petrol", "Diesel", "Electric"],
    "Color": ["White", "Black", "Red", "Blue", "Silver", "Gray", "Green"],
    "Distance Travelled": ["low mileage", "high mileage", "less than 10,000 km", "more than 10,000 km"],
    "Make Year": [],  # Special case handled separately for extracting years
    "Transmission Type": ["Automatic", "Manual"],
    "Budget": ["within 6 lakhs", "within 8 lakhs", "within 10 lakhs"]
}

company_policies = [
    "Free RC Transfer",
    "5-Day Money Back Guarantee",
    "Free RSA for One Year",
    "Return Policy",
    "Warranty on Engine and Gearbox",
    "Comprehensive 200-point inspection"
]

customer_objections = [
    "Refurbishment Quality",
    "Car Issues",
    "Price Issues",
    "Customer Experience Issues",
    "Hidden Problems",
    "Maintenance Concerns",
    "Warranty Concerns"
]

def preprocess_text(text):
    """Clean the text by removing unwanted characters."""
    text = re.sub(r'\n', ' ', text)  # Replace newline characters with spaces
    text = re.sub(r'[^A-Za-z0-9,.!? ]+', '', text)  # Remove special characters
    return text

def extract_customer_requirements(transcript):
    """Extract customer requirements from the transcript."""
    result = {}
    doc = nlp(transcript)  # Use spaCy NLP to process the transcript
    
    for category, options in customer_requirements.items():
        if options:  # If there are predefined options for the category
            prediction = classifier(transcript, options)  # Use zero-shot classifier
            result[category] = prediction['labels'][0] if prediction['scores'][0] > 0.5 else None
        else:  # Handle categories without predefined options
            if category == "Make Year":
                # Extract year using regex
                years = [ent.text for ent in doc.ents if re.match(r"\b(19|20)\d{2}\b", ent.text)]
                result[category] = years if years else None
            elif category == "Distance Travelled":
                # Extract distance travelled using regex
                distances = [ent.text for ent in doc.ents if re.match(r"\d+(,\d{3})*(\.\d+)?\s*(km|kilometers|miles)", ent.text)]
                result[category] = distances if distances else None
    
    # Special handling for budget extraction using regex
    budget_match = re.search(r'\b\d{1,2}\s*lakh[s]?\b', transcript, re.IGNORECASE)
    if budget_match:
        result['Budget'] = budget_match.group(0)

    return result

def extract_company_policies(transcript):
    """Extract discussed company policies from the transcript."""
    result = []
    prediction = classifier(transcript, company_policies)  # Use zero-shot classifier
    for i, policy in enumerate(prediction['labels']):
        if prediction['scores'][i] > 0.5:
            result.append(policy)  # Add policies that have a high confidence score
    return result

def extract_customer_objections(transcript):
    """Extract customer objections from the transcript."""
    result = []
    prediction = classifier(transcript, customer_objections)  # Use zero-shot classifier
    for i, objection in enumerate(prediction['labels']):
        if prediction['scores'][i] > 0.5:
            result.append(objection)  # Add objections with a high confidence score
    return result

def process_transcript(transcript, conversation_id):
    """Process the transcript to extract requirements, policies, and objections."""
    customer_requirements = extract_customer_requirements(transcript)
    company_policies = extract_company_policies(transcript)
    customer_objections = extract_customer_objections(transcript)

    return {
        "conversation_id": conversation_id,  # Include the conversation ID in the response
        "customer_requirements": customer_requirements,
        "company_policies_discussed": company_policies,
        "customer_objections": customer_objections
    }

# Flask app setup
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'  # Folder to save uploaded files
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create the upload folder if it doesn't exist

@app.route('/')
def index():
    """Render the home page with the file upload form."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file uploads and process the transcript."""
    file = request.files['file']  # Get the uploaded file
    if not file:
        return jsonify({"error": "No file part"}), 400

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file.filename.endswith('.pdf'):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
        file.save(file_path)  # Save the uploaded PDF file
        transcript = extract_text_from_pdf(file_path)  # Extract text from the PDF
    else:
        transcript = file.read().decode('utf-8')  # Read text from the uploaded file
    
    # Process the transcript
    cleaned_transcript = preprocess_text(transcript)  # Clean the transcript text
    conversation_id = "transcript_001"  # Static conversation ID, can be dynamically generated
    response = process_transcript(cleaned_transcript, conversation_id)  # Process the transcript
    
    return jsonify(response)  # Return the response as JSON

def extract_text_from_pdf(file_path):
    """Extract text content from a PDF file."""
    reader = PdfReader(file_path)  # Initialize the PDF reader
    text = ""
    for page in reader.pages:  # Iterate over PDF pages
        text += page.extract_text()  # Extract text from each page
    return text

if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask app in debug mode
