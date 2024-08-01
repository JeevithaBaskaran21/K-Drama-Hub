import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_email, subject, message):
    # Your email credentials
    email_address = "jeevithabaskaran964@gmail.com"
    email_password = ""

    # Set up the MIME
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the message
    msg.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(email_address, email_password)
        server.sendmail(email_address, to_email, msg.as_string())

# Streamlit App
st.title("Drama World Inquiry")

# User Input
user_email = st.text_input("Enter your email:")
inquiry_subject = st.text_input("Subject:")
inquiry_message = st.text_area("Your Inquiry:")

# Button to send email
if st.button("Send Inquiry"):
    if user_email and inquiry_subject and inquiry_message:
        send_email(user_email, inquiry_subject, inquiry_message)
        st.success("Inquiry sent successfully!")
    else:
        st.warning("Please fill in all fields.")

# Display additional information or content about the drama world website here if needed.
