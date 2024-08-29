import streamlit as st
import requests
import re
from pdfminer.high_level import extract_text

GOOGLE_API_KEY = 'AIzaSyClyJHLn2cv6l9EVwQm8TPCcw5dadpRZ_M'
CUSTOM_SEARCH_ENGINE_ID = '820463ca5a42348c9'


def process_resume(uploaded_file, skills_list):
    if uploaded_file is not None:
        text = extract_text(uploaded_file)


        skills = []
        for skill in skills_list:
            pattern = r"\b{}\b".format(re.escape(skill))
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                skills.append(skill)

        return skills
    else:
        return None

def assign_job_category(skills):
    job_categories = {
    "Data Scientist": {'Python', 'Data Analysis', 'Machine Learning', 'Deep Learning', 'SQL', 'Tableau'},
    "Web Developer": {'JavaScript', 'HTML', 'CSS', 'React', 'Node.js', 'Git'},
    "Data Analyst": {'Python', 'Data Analysis', 'SQL', 'Tableau', 'Matplotlib'},
    "Software Engineer": {'Java', 'Python', 'C++', 'Software Development', 'Git'},
    "DevOps Engineer": {'Linux', 'Docker', 'Kubernetes', 'CI/CD', 'AWS', 'Python'},
    "UX/UI Designer": {'User Research', 'Wireframing', 'Prototyping', 'Adobe XD', 'Figma', 'Sketch'},
    "Network Administrator": {'Network Security', 'Cisco', 'CCNA', 'Troubleshooting', 'VPN'},
    "Cybersecurity Analyst": {'Penetration Testing', 'Risk Assessment', 'SIEM', 'Ethical Hacking', 'Cryptography'},
    "Project Manager": {'Agile', 'Scrum', 'Project Planning', 'Risk Management', 'Stakeholder Management'},
    "Marketing Manager": {'Digital Marketing', 'SEO', 'Social Media Marketing', 'Content Strategy', 'Analytics'},
    "Financial Analyst": {'Financial Modeling', 'Excel', 'PowerPoint', 'Bloomberg Terminal', 'Accounting'},
    "Human Resources Manager": {'Recruitment', 'Employee Relations', 'Performance Management', 'Labor Laws', 'HRIS'},
    "Sales Representative": {'CRM Software', 'Negotiation', 'Presentation Skills', 'Lead Generation', 'Customer Service'},
    "Graphic Designer": {'Adobe Creative Suite', 'Typography', 'Branding', 'Illustration', 'Layout Design'},
    "Content Writer": {'Copywriting', 'SEO Writing', 'Blogging', 'Editing', 'Research'},
    "Teacher": {'Lesson Planning', 'Classroom Management', 'Assessment', 'Educational Technology', 'Differentiated Instruction'},
    "Customer Service Representative": {'Communication', 'Problem-solving', 'CRM Software', 'Empathy', 'Multi-tasking'},
    "Business Analyst": {'Requirements Gathering', 'Data Visualization', 'SQL', 'Process Modeling', 'Stakeholder Management'},
    "Product Manager": {'Product Strategy', 'User Stories', 'Market Research', 'A/B Testing', 'Roadmapping'},
    "Operations Manager": {'Process Improvement', 'Supply Chain Management', 'Inventory Management', 'Budgeting', 'Team Leadership'},
    "Cloud Architect": {'AWS', 'Azure', 'Google Cloud', 'Serverless', 'Microservices', 'Cloud Security'},
    "Machine Learning Engineer": {'TensorFlow', 'PyTorch', 'Scikit-learn', 'NLP', 'Computer Vision', 'Big Data'},
    "Full Stack Developer": {'Frontend Development', 'Backend Development', 'Database Management', 'API Design', 'Version Control'},
    "Mobile App Developer": {'iOS Development', 'Android Development', 'React Native', 'Swift', 'Kotlin', 'Mobile UI/UX'},
    "Systems Analyst": {'Systems Design', 'Business Process Modeling', 'IT Strategy', 'Change Management', 'Technical Documentation'},
    "Quality Assurance Engineer": {'Test Planning', 'Automated Testing', 'Manual Testing', 'Bug Tracking', 'Performance Testing'},
    "Database Administrator": {'SQL', 'Database Design', 'Backup and Recovery', 'Performance Tuning', 'Data Security'},
    "Digital Marketing Specialist": {'Google Analytics', 'Email Marketing', 'PPC Advertising', 'Content Marketing', 'Social Media Management'},
    "Technical Writer": {'Technical Documentation', 'API Documentation', 'User Manuals', 'Style Guides', 'Information Architecture'},
    "Accountant": {'Bookkeeping', 'Financial Reporting', 'Tax Preparation', 'Auditing', 'QuickBooks'},
    "Legal Assistant": {'Legal Research', 'Document Preparation', 'Case Management', 'Legal Ethics', 'Court Procedures'},
    "Nurse": {'Patient Care', 'Medical Records', 'Medication Administration', 'Health Assessment', 'Emergency Procedures'},
    "Chef": {'Culinary Techniques', 'Menu Planning', 'Food Safety', 'Kitchen Management', 'Nutritional Knowledge'},
    "Architect": {'AutoCAD', 'SketchUp', 'Building Codes', 'Sustainable Design', '3D Modeling'},
    "Social Media Manager": {'Content Creation', 'Community Management', 'Social Media Analytics', 'Influencer Marketing', 'Social Media Advertising'},
    "Event Planner": {'Venue Selection', 'Budget Management', 'Vendor Coordination', 'Event Marketing', 'Logistics Planning'},
    "Interior Designer": {'Space Planning', 'Color Theory', 'CAD Software', 'Furniture Selection', 'Project Management'},
    "Journalist": {'Investigative Reporting', 'News Writing', 'Interviewing', 'Fact-checking', 'Multimedia Production'},
    "Real Estate Agent": {'Property Valuation', 'Negotiation', 'Real Estate Laws', 'Marketing Properties', 'Client Relations'},
    "Physical Therapist": {'Anatomy', 'Exercise Physiology', 'Rehabilitation Techniques', 'Patient Assessment', 'Treatment Planning'}
}
    

    max_matches = 0
    assigned_category = None

    for category, category_skills in job_categories.items():
        matches = sum(1 for skill in skills if skill in category_skills)
        if matches > max_matches:
            max_matches = matches
            assigned_category = category

    return assigned_category


import requests
from bs4 import BeautifulSoup

def fetch_job_openings_naukri(query):
    base_url = 'https://template-git-main-infoziant-llcs-projects.vercel.app/jobs.html/'
    search_url = f"{base_url}{query.replace(' ', '-')}-jobs"

    try:
        response = requests.get(search_url)
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, 'html.parser')

        job_listings = []
        for job in soup.find_all('article', class_='jobTuple'):
            title = job.find('a', class_='title').get_text(strip=True)
            link = job.find('a', class_='title')['href']
            job_listings.append((title, link))

        return job_listings
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return []






























# def fetch_job_openings(query):
#     url = 'https://www.googleapis.com/customsearch/v1'
#     params = {
#         'key': GOOGLE_API_KEY,
#         'cx': CUSTOM_SEARCH_ENGINE_ID,
#         'q': f'"{query}" jobs in india'
#     }
#     try:
#         response = requests.get(url, params=params)
#         response.raise_for_status()  
#         results = response.json()
#         return [(item['title'], item['link']) for item in results.get('items', [])]
#     except requests.exceptions.RequestException as e:
#         st.error(f"An error occurred: {e}")
#         return []











def main():
    st.title("Resume Skill Extractor and Job Finder")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    skills_list = [
        'Python', 'Data Analysis', 'Machine Learning', 'Communication', 'Project Management', 'Deep Learning', 'SQL', 'Tableau',
        'Java', 'C++', 'JavaScript', 'HTML', 'CSS', 'React', 'Angular', 'Node.js', 'MongoDB', 'Express.js', 'Git',
        'Research', 'Statistics', 'Quantitative Analysis', 'Qualitative Analysis', 'SPSS', 'R', 'Data Visualization', 'Matplotlib',
        'Seaborn', 'Plotly', 'Pandas', 'Numpy', 'Scikit-learn', 'TensorFlow', 'Keras', 'PyTorch', 'NLTK', 'Text Mining',
        'Natural Language Processing', 'Computer Vision', 'Image Processing', 'OCR', 'Speech Recognition', 'Recommendation Systems',
        'Collaborative Filtering', 'Content-Based Filtering', 'Reinforcement Learning', 'Neural Networks', 'Convolutional Neural Networks',
        'Recurrent Neural Networks', 'Generative Adversarial Networks', 'XGBoost', 'Random Forest', 'Decision Trees', 'Support Vector Machines',
        'Linear Regression', 'Logistic Regression', 'K-Means Clustering', 'Hierarchical Clustering', 'DBSCAN', 'Association Rule Learning',
        'Apache Hadoop', 'Apache Spark', 'MapReduce', 'Hive', 'HBase', 'Apache Kafka', 'Data Warehousing', 'ETL', 'Big Data Analytics',
        'Cloud Computing', 'Amazon Web Services (AWS)', 'Microsoft Azure', 'Google Cloud Platform (GCP)', 'Docker', 'Kubernetes', 'Linux',
        'Shell Scripting', 'Cybersecurity', 'Network Security', 'Penetration Testing', 'Firewalls', 'Encryption', 'Malware Analysis',
        'Digital Forensics', 'CI/CD', 'DevOps', 'Agile Methodology', 'Scrum', 'Kanban', 'Continuous Integration', 'Continuous Deployment',
        'Software Development', 'Web Development', 'Mobile Development', 'Backend Development', 'Frontend Development', 'Full-Stack Development',
        'UI/UX Design', 'Responsive Design', 'Wireframing', 'Prototyping', 'User Testing', 'Adobe Creative Suite', 'Photoshop', 'Illustrator',
        'InDesign', 'Figma', 'Sketch', 'Zeplin', 'InVision', 'Product Management', 'Market Research', 'Customer Development', 'Lean Startup',
        'Business Development', 'Sales', 'Marketing', 'Content Marketing', 'Social Media Marketing', 'Email Marketing', 'SEO', 'SEM', 'PPC',
        'Google Analytics', 'Facebook Ads', 'LinkedIn Ads', 'Lead Generation', 'Customer Relationship Management (CRM)', 'Salesforce',
        'HubSpot', 'Zendesk', 'Intercom', 'Customer Support', 'Technical Support', 'Troubleshooting', 'Ticketing Systems', 'ServiceNow',
        'ITIL', 'Quality Assurance', 'Manual Testing', 'Automated Testing', 'Selenium', 'JUnit', 'Load Testing', 'Performance Testing',
        'Regression Testing', 'Black Box Testing', 'White Box Testing', 'API Testing', 'Mobile Testing', 'Usability Testing', 'Accessibility Testing',
        'Cross-Browser Testing', 'Agile Testing', 'User Acceptance Testing', 'Software Documentation', 'Technical Writing', 'Copywriting',
        'Editing', 'Proofreading', 'Content Management Systems (CMS)', 'WordPress', 'Joomla', 'Drupal', 'Magento', 'Shopify', 'E-commerce',
        'Payment Gateways', 'Inventory Management', 'Supply Chain Management', 'Logistics', 'Procurement', 'ERP Systems', 'SAP', 'Oracle',
        'Microsoft Dynamics', 'Tableau', 'Power BI', 'QlikView', 'Looker', 'Data Warehousing', 'ETL', 'Data Engineering', 'Data Governance',
        'Data Quality', 'Master Data Management', 'Predictive Analytics', 'Prescriptive Analytics', 'Descriptive Analytics', 'Business Intelligence',
        'Dashboarding', 'Reporting', 'Data Mining', 'Web Scraping', 'API Integration', 'RESTful APIs', 'GraphQL', 'SOAP', 'Microservices',
        'Serverless Architecture', 'Lambda Functions', 'Event-Driven Architecture', 'Message Queues', 'GraphQL', 'Socket.io', 'WebSockets',
        'Ruby', 'Ruby on Rails', 'PHP', 'Symfony', 'Laravel', 'CakePHP', 'Zend Framework', 'ASP.NET', 'C#', 'VB.NET', 'ASP.NET MVC', 'Entity Framework',
        'Spring', 'Hibernate', 'Struts', 'Kotlin', 'Swift', 'Objective-C', 'iOS Development', 'Android Development', 'Flutter', 'React Native', 'Ionic',
        'Mobile UI/UX Design', 'Material Design', 'SwiftUI', 'RxJava', 'RxSwift', 'Django', 'Flask', 'FastAPI', 'Falcon', 'Tornado', 'WebSockets',
        'GraphQL', 'RESTful Web Services', 'SOAP', 'Microservices Architecture', 'Serverless Computing', 'AWS Lambda', 'Google Cloud Functions',
        'Azure Functions', 'Server Administration', 'System Administration', 'Network Administration', 'Database Administration', 'MySQL', 'PostgreSQL',
        'SQLite', 'Microsoft SQL Server', 'Oracle Database', 'NoSQL', 'MongoDB', 'Cassandra', 'Redis', 'Elasticsearch', 'Firebase', 'Google Analytics',
        'Google Tag Manager', 'Adobe Analytics', 'Marketing Automation', 'Customer Data Platforms', 'Segment', 'Salesforce Marketing Cloud', 'HubSpot CRM',
        'Zapier', 'IFTTT', 'Workflow Automation', 'Robotic Process Automation (RPA)', 'UI Automation', 'Natural Language Generation (NLG)',
        'Virtual Reality (VR)', 'Augmented Reality (AR)', 'Mixed Reality (MR)', 'Unity', 'Unreal Engine', '3D Modeling', 'Animation', 'Motion Graphics',
        'Game Design', 'Game Development', 'Level Design', 'Unity3D', 'Unreal Engine 4', 'Blender', 'Maya', 'Adobe After Effects', 'Adobe Premiere Pro',
        'Final Cut Pro', 'Video Editing', 'Audio Editing', 'Sound Design', 'Music Production', 'Digital Marketing', 'Content Strategy', 'Conversion Rate Optimization (CRO)',
        'A/B Testing', 'Customer Experience (CX)', 'User Experience (UX)', 'User Interface (UI)', 'Persona Development', 'User Journey Mapping', 'Information Architecture (IA)',
        'Wireframing', 'Prototyping', 'Usability Testing', 'Accessibility Compliance', 'Internationalization (I18n)', 'Localization (L10n)', 'Voice User Interface (VUI)',
        'Chatbots', 'Natural Language Understanding (NLU)', 'Speech Synthesis', 'Emotion Detection', 'Sentiment Analysis', 'Image Recognition', 'Object Detection',
        'Facial Recognition', 'Gesture Recognition', 'Document Recognition', 'Fraud Detection', 'Cyber Threat Intelligence', 'Security Information and Event Management (SIEM)',
        'Vulnerability Assessment', 'Incident Response', 'Forensic Analysis', 'Security Operations Center (SOC)', 'Identity and Access Management (IAM)', 'Single Sign-On (SSO)',
        'Multi-Factor Authentication (MFA)', 'Blockchain', 'Cryptocurrency', 'Decentralized Finance (DeFi)', 'Smart Contracts', 'Web3', 'Non-Fungible Tokens (NFTs)'
    ]
    if uploaded_file is not None:
        extracted_skills = process_resume(uploaded_file, skills_list)
    
        if extracted_skills:
            st.write("Skills found in the resume:")
            st.write(extracted_skills)

            job_category = assign_job_category(extracted_skills)
            st.write(f"Assigned job category: {job_category}")

            st.write(f"Fetching job openings for {job_category} on Enbott")
            job_openings = fetch_job_openings_naukri(job_category)

            if job_openings:
                st.write("### **Job Openings Found:**")
                for title, link in job_openings:
                    if st.button(f"Apply for {title}"):
                        st.write(f"Redirecting to {link}...")
                        import webbrowser
                        webbrowser.open(link)
            else:
                st.write("No job openings found.")
        else:
            st.write("No skills found.")
    else:
        st.write("Please upload a PDF resume.")



























    # if uploaded_file is not None:

    #     extracted_skills = process_resume(uploaded_file, skills_list)
        
    #     if extracted_skills:
    #         st.write("Skills found in the resume:")
    #         st.write(extracted_skills)


    #         job_category = assign_job_category(extracted_skills)
    #         st.write(f"Assigned job category: {job_category}")

       
    #         st.write(f"Fetching job openings for {job_category}...")
    #         job_openings = fetch_job_openings(job_category)

    #         if job_openings:
    #             st.write("### **Job Openings Found:**")
    #             for title, link in job_openings:
    #                 if st.button(f"Apply for {title}"):
    #                     st.write(f"Redirecting to {link}...")
    #                     import webbrowser
    #                     webbrowser.open(link)
    #         else:
    #             st.write("No job openings found.")
    #     else:
    #         st.write("No skills found.")
    # else:
    #     st.write("Please upload a PDF resume.")

if __name__ == "__main__":
    main()
