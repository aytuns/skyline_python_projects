import smtplib, ssl
from email.message import EmailMessage
import time

#email to send messages to multiple poeple every 2 minutes
#draft email configuration
sender = "mail@gmail.com"
recepient  = ["mail1@gmail.com","mail2@gmail.com","mail3@yahoo.com"]
password = "password"
subject = "TEST2"
mail_content = "this is my second message"


#call the mail class
message = EmailMessage()

message['subject'] = subject
message['from'] = sender
message['to'] = ','.join(recepient)
message.set_content(mail_content)

# Connect to the Gmail SMTP server and Send Email
  # Create a secure default settings context
context = ssl.create_default_context()
def send_mail():

	with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as server:
		server.login(sender,password)
		server.send_message(message)

while True:
	send_mail()
	print('Mail sent')
	#time.sleep(120)