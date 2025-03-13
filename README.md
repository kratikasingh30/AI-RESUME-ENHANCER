# AI-RESUME-ENHANCER

📄 AI-Powered Resume Analyzer
This project is an AI-driven resume analyzer that extracts text from a PDF resume and provides improvement suggestions using OpenAI's GPT-4.

🚀 Features
✅ Extracts text from a PDF resume using PyMuPDF (fitz).
✅ Uses GPT-4 to analyze the resume and suggest improvements.
✅ Provides structured feedback on skills, formatting, and content.

📂 Project Structure
bash
Copy
Edit
📁 resume-analyzer
│── 📄 app.py                  # Main script to extract and analyze resumes
│── 📄 resume_extractor.py      # Extracts text from PDF resumes
│── 📄 resume_analyzer.py       # Analyzes resume content using OpenAI GPT-4
│── 📂 samples                  # Folder to store sample resumes
│── 📄 requirements.txt         # List of dependencies
│── 📄 README.md                # Project documentation
🛠 Installation
1️⃣ Clone the Repository
sh
Copy
Edit
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
2️⃣ Set Up a Virtual Environment (Recommended)
sh
Copy
Edit
# Using venv (for Windows)
python -m venv venv
venv\Scripts\activate

# Using venv (for macOS/Linux)
python3 -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
💻 Usage
1️⃣ Provide Your Resume PDF
Place your resume inside the samples folder.

2️⃣ Run the Script
sh
Copy
Edit
python app.py
3️⃣ View AI Suggestions
The script will analyze your resume and provide feedback in the terminal.

🔧 Configuration
🔑 Set Your OpenAI API Key
Replace "your_openai_api_key" in resume_analyzer.py with your actual OpenAI API key:

python
Copy
Edit
import openai
openai.api_key = "your_openai_api_key"
Alternatively, you can store it in an environment variable:

sh
Copy
Edit
export OPENAI_API_KEY="your_openai_api_key"  # macOS/Linux
set OPENAI_API_KEY="your_openai_api_key"    # Windows
📜 Requirements
Install dependencies using:

sh
Copy
Edit
pip install -r requirements.txt
Or manually install:

sh
Copy
Edit
pip install pymupdf openai
📌 Example Output
vbnet
Copy
Edit
🔍 Extracted Resume Text:
John Doe, Software Engineer, skilled in Python, AI, and Database Management.

💡 Resume Analysis & Suggestions:
- Add a dedicated "Skills" section for better clarity.
- Improve bullet points with quantifiable achievements.
- Optimize formatting for better readability.
🛠 Tech Stack
Python 3.8+
PyMuPDF (fitz) – For extracting text from PDFs
OpenAI GPT-4 – For analyzing and suggesting improvements
