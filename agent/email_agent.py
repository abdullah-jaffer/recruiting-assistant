import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_emails_to_candidates(top: list, sender_email: str, sender_password: str, your_name: str, company_name: str, job_title: str, llm):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)

        for candidate in top:
            recipient_name = candidate["name"]
            recipient_email = candidate["email"]
            experience = candidate["experience"]

            prompt = f"""
You are a recruiter named {your_name} from {company_name}, hiring for the role of {job_title}.

Here is the candidate's name and a summary of their work experience:

Name: {recipient_name}  
Experience: {experience}

Write a concise, friendly, and professional email introducing the opportunity and expressing interest in their background highlighting thier most impressing experience. Ask them to reply if they're open to a conversation. Do not include any links or attachments.
"""

            try:
                response = llm.invoke(prompt)
                body = response.content.strip()

                subject = f"Opportunity: {job_title} at {company_name}"

                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = recipient_email
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))

                server.send_message(msg)
                print(f"Email sent to {recipient_name} at {recipient_email}")

            except Exception as e:
                print(f"Failed to send email to {recipient_email}: {e}")
