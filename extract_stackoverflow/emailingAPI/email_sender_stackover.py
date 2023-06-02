# Import modules
import stackoverhtml as so
import smtplib, ssl, datetime
## email.mime subclasses
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
### Add new subclass for adding attachments
from email.mime.application import MIMEApplication
import sys


# Define the HTML document
try:
	html = so.writeHTML()
except Exception as e:
     sys.exit(input(f'Error occurred: {e}. Press Enter to end the process'))
##############################################################

# Define a function to attach files as MIMEApplication to the email
    ## Add another input extra_headers default to None
##############################################################
def attach_file_to_email(email_message, filename):
    # Open the attachment file for reading in binary mode, and make it a MIMEApplication class
    with open(filename, "rb") as f:
        file_attachment = MIMEApplication(f.read())
    # Add header/name to the attachments    
    file_attachment.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    # Attach the file to the message
    email_message.attach(file_attachment)
##############################################################    

# Set up the email addresses and password. Please replace below with your email address and password
email_from = input("Input Sender's Email: ")
password = input("Input Sender's Password: ")
email_to = input("Input Recepient Emails: ")
print("PROCESSING.....")
# Generate today's date to be included in the email Subject
date_str = datetime.datetime.today()

# Create a MIMEMultipart class, and set up the From, To, Subject fields
email_message = MIMEMultipart()
email_message['From'] = email_from
email_message['To'] = email_to
email_message['Subject'] = f'StackOverFlow API - {date_str}'

# Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
email_message.attach(MIMEText(html, "html"))

# Attach more (documents)
  ## Apply function with extra_header on chart.png. This will render chart.png in the html content
##############################################################
attach_file_to_email(email_message, so.outputFile+'.pdf')
print("Adding Attachments.....")
# Convert it as a string
email_string = email_message.as_string()

# Connect to the Gmail SMTP server and Send Email
context = ssl.create_default_context()
try:
	with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
		server.login(email_from, password)
		server.sendmail(email_from, email_to, email_string)
except Exception as e:
     sys.exit(input(f'Error occurred: {e}. Press Enter to end the process'))

print("Mail sent successfully with attachment\n")
sys.exit(input("Press ENTER to close the application"))