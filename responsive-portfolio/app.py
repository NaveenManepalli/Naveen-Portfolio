from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    user_dtls = request.form['user_dtls']
    
    # Here you can process the data, e.g., send an email
    send_email(name, email, subject, user_dtls)
    
    return 'Form submitted successfully!'

def send_email(name, email, subject, message):
    to = "manepallinaveen10@gmail.com"  
    msg = MIMEText(f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}")
    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = to
    
    
    smtp_server = 'your smpt server'
    smtp_port = 587
    smtp_user = 'your mail id'
    smtp_password = 'your pearsonal password'
    
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(email, [to], msg.as_string())

if __name__ == '__main__':
    app.run(debug=True)
