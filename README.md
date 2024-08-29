# Niral_hackathon_team18 by Madhavan M, Dhinesh Kumar A, Keerthivasan S
Hackathon Task: Few-Shot/Zero-Shot Car Sales Conversation Information Extractor and Analyzer

**Project Overview**
This project is a Flask-based web application that processes customer service transcripts to extract customer requirements, company policies discussed, and customer objections using natural language processing (NLP) techniques. It utilizes pre-trained models from spaCy and Hugging Face Transformers for NLP tasks and handles both PDF and text file uploads.

**Prerequisites:**
Before running the project, ensure that you have the following software installed:

Python 3.6 or higher
pip (Python package installer)

main.py CONSIST OF PYTHON FILES TO RUN PLACE THE HTML(index.html) INSIDE TEMPLATES FOLDER.

**Setup Instructions**

1)Clone the Repository:

**Clone the project repository from GitHub:**
For beginners use goto: </>Code --> Download as ZIP 
2)Run pip install -r requirements.txt 
It will automatically installs every required packages for your enviroinment

**Project Structure**

app.py: The main Flask application script.
templates/index.html: HTML template for the web interface (place index.html inside templates folder for smooth experiences).
uploads/: Directory to store uploaded files.
Running the Application

**Start the Flask Application:**

Run the Flask application using the following command:

#python app.py

By default, the application runs in debug mode on http://127.0.0.1:5000.

#Access the Web Interface:

Open your web browser and navigate to http://127.0.0.1:5000 to access the application's web interface.

#Upload Files:

Use the web interface to upload a text or PDF file. The application will process the file, extract relevant information, and display the results.

#Key Functions
preprocess_text(text): Cleans the input text by removing unwanted characters and normalizing whitespace.
extract_customer_requirements(transcript): Uses spaCy and a zero-shot classification model to extract customer requirements based on predefined categories.
extract_company_policies(transcript): Identifies company policies discussed in the transcript using a zero-shot classification model.
extract_customer_objections(transcript): Extracts customer objections from the transcript using a zero-shot classification model.
process_transcript(transcript, conversation_id): Combines the above functions to process the entire transcript and return a structured response.
extract_text_from_pdf(file_path): Extracts text content from a PDF file using PyPDF2.



**OUR PROTOTYPE WITH CUSTOM TEXT:**

![Screenshot (6)](https://github.com/user-attachments/assets/4d266bf1-ed2a-4291-9b22-ce960480c6d4)

OUR SUBMISSION (AN OVERVIEW):

UPLOAD AND LOADING:

![Screenshot (21)](https://github.com/user-attachments/assets/98c551b3-8fc3-4e43-b191-b29d7a1c26f1)

OUTPUT SAMPLE:

![Screenshot (19)](https://github.com/user-attachments/assets/0e46c72a-3337-4ceb-aafd-045b0c55c6a4)



**PERKS OF OUR MODEL:**

1)Uses Spacy model for nlp and bert for tokenization(NO External API used here)

2)User friendly Interface 

3)Formats like .txt and .pdf are accepted 

4)Able to Upload multiple Transcripts without reload.

5)Accuracy is aboout 65% and time taken to publish result about 35 - 60 sec (depends on complexity of uploaded script)

**FUTURE WORKS AND AREA OF IMPROVEMENTS:**
1) Need to make a model which loads and interprets faster and quicker.

2) Provide most accurate results for the end user eventhough with higher complexity.


**Conclusion**
This documentation provides an overview of how to set up, run, and use the Flask application for processing customer service transcripts and overview of the performance of the model. 

SOME CREATIVE STYLING BY US:

![WhatsApp Image 2024-08-29 at 6 13 07 PM](https://github.com/user-attachments/assets/caee67c8-c386-4f33-8740-9843dca13ae2)
