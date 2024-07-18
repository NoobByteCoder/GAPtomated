# GAPtomated
This GitHub repository contains a Python-based tool designed to automate the gap analysis between existing organizational policies and ISO 27001 requirements. It reads policies from PDF and DOCX files, preprocesses the text, compares it with ISO 27001 requirements, identifies gaps, and saves the results to a CSV file.

## Gap Analysis Tool for ISO 27001 Compliance
This tool is designed to automate the process of gap analysis between existing organizational policies and ISO 27001 requirements. The tool reads policies in PDF and DOCX formats, preprocesses the text, and compares it with the ISO 27001 requirements. It identifies gaps and saves the findings in a CSV file.

## Features
Reads policies from PDF and DOCX files.
Preprocesses text using NLP techniques.
Compares policy content with ISO 27001 requirements.
Identifies gaps and calculates similarity scores.
Saves gap analysis results to a CSV file.

## Requirements
Python 3.8 or higher

Required Python libraries:

spacy

PyPDF2

python-docx

nltk

scikit-learn

## Installation
Clone the repository:

git clone https://github.com/yourusername/gap-analysis-tool.git

cd gap-analysis-tool

Create a virtual environment:

python -m venv venv

source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

Install the required packages as given under requirements section.

Download the NLTK stopwords:

python -c "import nltk; nltk.download('stopwords')"

Download the SpaCy language model:

python -m spacy download en_core_web_sm

## Usage
Place your policy documents (PDF or DOCX) in the policy_folder directory.

Ensure you have the iso_27001_requirements.json file in the same directory as the script. This JSON file should contain the ISO 27001 requirements in the following format:

[
    {
        "requirement": "Requirement 1",
        "description": "Description of requirement 1"
    },
    {
        "requirement": "Requirement 2",
        "description": "Description of requirement 2"
    }
    ...
]
Run the script:

python gap.py

The tool will process the policies, compare them with ISO 27001 requirements, and save the findings to gap_analysis_report.csv.

Example

Place your policy documents in the specified folder.

Run the script:

python gap.py

Check the generated gap_analysis_report.csv for the gap analysis results.

## Contributing
Contributions are welcomed to enhance the functionality and features of this tool. Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

