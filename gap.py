import os
import json
import spacy
import PyPDF2
import docx
import nltk
import csv
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

# Ensure you have the required NLTK stopwords
nltk.download('stopwords')

# Load Spacy model
nlp = spacy.load('en_core_web_sm')

# Function to read PDF content
def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

# Function to read DOCX content
def read_docx(file_path):
    doc = docx.Document(file_path)
    return '\n'.join([para.text for para in doc.paragraphs])

# Function to preprocess text
def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc if token.is_alpha and not token.is_stop]
    return ' '.join(tokens)

# Function to load ISO 27001 requirements from a JSON file
def load_iso_requirements(json_path):
    with open(json_path, 'r') as file:
        return json.load(file)

# Function to compare policy text with ISO requirements
def compare_with_iso(policy_text, iso_requirements):
    vectorizer = TfidfVectorizer()
    requirements = [req['requirement'] for req in iso_requirements]
    all_texts = requirements + [policy_text]
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    
    cosine_similarities = (tfidf_matrix * tfidf_matrix.T).toarray()
    policy_similarities = cosine_similarities[-1, :-1]
    
    gaps = []
    for i, similarity in enumerate(policy_similarities):
        if similarity < 0.5:
            gaps.append({
                'requirement': iso_requirements[i]['requirement'],
                'description': iso_requirements[i]['description'],
                'similarity': similarity
            })
    return gaps

# Function to save gaps to a CSV file
def save_gaps_to_csv(gaps, output_path):
    with open(output_path, 'w', newline='') as csvfile:
        fieldnames = ['requirement', 'description', 'similarity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for gap in gaps:
            writer.writerow(gap)

def main():
    iso_json_path = 'iso_27001_requirements.json'
    policy_folder = '/path_to_file' #replace folder path where policies are present
    output_csv = 'gap_analysis_report.csv'
    
    iso_requirements = load_iso_requirements(iso_json_path)
    
    # Print the loaded ISO requirements to verify content
    print(iso_requirements)
    
    policies = []
    for file_name in os.listdir(policy_folder):
        file_path = os.path.join(policy_folder, file_name)
        if file_path.endswith('.pdf'):
            policies.append(preprocess_text(read_pdf(file_path)))
        elif file_path.endswith('.docx'):
            policies.append(preprocess_text(read_docx(file_path)))
    
    all_gaps = []
    for i, policy_text in enumerate(policies):
        gaps = compare_with_iso(policy_text, iso_requirements)
        all_gaps.extend(gaps)
        print(f'Gaps for policy {i + 1}:')
        for gap in gaps:
            print(f"Requirement: {gap['requirement']}\nDescription: {gap['description']}\nSimilarity: {gap['similarity']}\n")
    
    # Save all gaps to CSV
    save_gaps_to_csv(all_gaps, output_csv)
    print(f'Gap analysis report saved to {output_csv}')

if __name__ == '__main__':
    main()
