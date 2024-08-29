Tech Stack Used

Python: The primary programming language used for this project.

Flask: A lightweight web framework for Python used to create the web server and handle HTTP requests.

spaCy: A popular Python library for natural language processing (NLP). It's used here for text processing tasks.

Hugging Face Transformers: A library providing pre-trained models for natural language understanding tasks. It is used for zero-shot classification.

PyPDF2: A Python library for reading PDF files, used to extract text from PDF documents.

re (Regular Expressions): Python’s built-in module for performing regex operations, used for text cleaning and pattern matching.

HTML: Used for creating the basic front-end interface to upload files.

Werkzeug: A WSGI utility library for Python, used here for securely handling file uploads.


**Introduction to Zero-Shot Learning**

Zero-shot learning is a machine learning technique that allows models to make predictions on tasks they were not explicitly trained for. Instead of training on every possible class or category, a zero-shot model leverages natural language understanding and generalizes to new, unseen classes by using descriptions or examples.

In this project, the zero-shot learning approach is used to classify segments of customer service transcripts into predefined categories such as customer requirements, company policies, and customer objections. This enables the application to understand and categorize new, unstructured text data without needing a specific training dataset for each category.

**Code Workflow Explanation**
Here’s a simple step-by-step explanation of how the code works:

**Setup and Imports:**

The code begins by importing necessary libraries and modules, including spaCy for NLP, transformers for zero-shot classification, Flask for creating a web application, and PyPDF2 for handling PDF files.

**Model Initialization:**

spaCy's pre-trained model (en_core_web_sm) is loaded for named entity recognition and other NLP tasks.
A zero-shot classification model from Hugging Face (facebook/bart-large-mnli) is initialized to classify text into predefined categories.
Category Definitions:

Categories for customer_requirements, company_policies, and customer_objections are defined as lists of keywords. These will be used by the zero-shot classifier to match text from transcripts to these categories.
Functions for Processing Text:

preprocess_text(): Cleans up the text by removing unwanted characters and normalizing the format.
extract_customer_requirements(): Takes a transcript, uses spaCy for entity recognition, and applies the zero-shot classifier to match customer requirements based on predefined categories.
extract_company_policies(): Identifies company policies mentioned in the transcript using the zero-shot classifier.
extract_customer_objections(): Extracts objections raised by the customer in the transcript, again using zero-shot classification.
Main Processing Function:

process_transcript(): Combines the functions to analyze the transcript, extracting customer requirements, company policies, and customer objections. This function returns a structured response with the extracted information.
Flask Web Application:

A Flask application is set up with routes to handle HTTP requests:
/: Displays a simple HTML form for file upload.
/upload: Handles the file upload, checks the file type (text or PDF), extracts text, processes the text to extract relevant information, and returns the results in JSON format.
PDF Handling:

extract_text_from_pdf(): Reads and extracts text from PDF files using PyPDF2, allowing the application to handle PDF documents as input.
Running the Application:

The application is run in debug mode, which makes it easier to identify and fix any issues during development.


**Summary**
The project leverages zero-shot learning and NLP to classify customer service transcripts into predefined categories.
The use of Flask allows for a simple web-based interface for uploading and processing files.
The application is capable of handling both text and PDF files, extracting and categorizing relevant information efficiently.
