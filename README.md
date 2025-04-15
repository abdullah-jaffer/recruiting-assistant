# 📄 Resume Ranking & Outreach Streamlit App

This Streamlit app processes a ZIP file of PDF resumes, ranks candidates based on job requirements using OpenAI, and allows you to send personalized outreach emails to top candidates.

---

## 🚀 Features

- Upload ZIP of PDF resumes  
- Extract structured candidate info using LLM  
- Rank candidates based on job criteria  
- Send personalized emails to top matches  
- View ranked candidates in a table with individual or bulk email options

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create and Activate Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env` File

In the root directory of the project, create a `.env` file and add the following:

```env
OPENAI_API_KEY="your-openai-api-key"
EMAIL_ADDRESS="your-email@gmail.com"
EMAIL_APP_PASSWORD="your-email-app-password"
```

> 📧 Use an **App Password** for your Gmail account instead of your actual password. You can generate it from your [Google Account > Security > App Passwords](https://myaccount.google.com/apppasswords).

---

## 🧪 Run the App

```bash
streamlit run app.py
```

This will open the app in your default browser (usually at `http://localhost:8501`).

---

## 🗂️ Project Structure

```bash
├── app.py
├── agent/
│   ├── pdf_agent.py
│   ├── ranking_agent.py
│   └── email_agent.py
├── model/
│   └── Candidate.py
├── .env
├── requirements.txt
└── README.md
```

---

## 🧪 Deploy (Optional)

### 🌍 Streamlit Cloud

1. Push your repo to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) and deploy your repo
3. Set the following **secrets** in Streamlit Cloud:
   - `OPENAI_API_KEY`
   - `EMAIL_ADDRESS`
   - `EMAIL_APP_PASSWORD`

---

## 📬 Contact

For any questions or contributions, feel free to open an issue or reach out.
