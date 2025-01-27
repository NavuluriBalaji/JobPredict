*Job Prediction System*
This project aims to build a job prediction system that automatically scans resumes, parses the necessary details, assigns a relevant job category, and displays job openings around the world. The system leverages generative AI and resume parsing technologies to make job recommendations.

**Features**
Resume Parsing: Automatically extract key information such as skills, certifications, education, work experience, and personal details from resumes.
Job Category Assignment: The system assigns a job category based on the parsed information, such as software engineering, data science, or marketing.
Global Job Listings: Once a job category is assigned, the system fetches relevant job openings worldwide using APIs (e.g., LinkedIn, Indeed, Google Jobs).
Generative AI Integration: Uses generative AI models for parsing and assigning job categories, leveraging NLP technologies.

T**echnologies**

Python: Programming language used for the system.
Flask: For web application and API setup.
Resume Parser: Using libraries like spacy, PyResparser, or custom-built solutions.
Job APIs: For job opening retrieval, such as LinkedIn or Indeed.
Generative AI: Using models from platforms like Hugging Face, Google Cloud AI, etc.
Frontend (Optional): React or HTML/CSS for displaying the parsed data and job openings.

**Installation**
To set up the Job Prediction System locally, follow the steps below:

1. Clone the Repository
git clone https://github.com/yourusername/job-prediction-system.git
cd job-prediction-system

3. Install Dependencies
You can install the necessary dependencies using pip:
pip install -r requirements.txt

3. Setup API Keys
For retrieving job listings from external sources, you will need to sign up for job listing APIs (e.g., LinkedIn, Indeed). Add your API keys to a .env file or directly into the code.

4. Run the Application
python app.py
This will start the application locally. Open your browser and go to http://127.0.0.1:5000 to access the system.

Usage
1. Upload Resume
To use the system, upload a resume in .pdf, .docx, or .txt format. The system will automatically parse the resume and display the extracted details, including:
Name
Contact Information
Education
Work Experience
Skills
Certifications

3. Job Category Assignment
After parsing, the system assigns a job category based on the parsed data. The category could be a profession like Software Developer, Data Scientist, Marketing Specialist, etc.

4. View Job Openings
Once the job category is assigned, the system fetches relevant job openings globally and displays them. You can view job titles, locations, company names, and other relevant information.

5. Apply for Jobs (Optional)
Users can be redirected to the job listing platforms (LinkedIn, Indeed, etc.) for applying directly.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributors
Balaji - Project Lead
