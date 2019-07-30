import smtplib
import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText as MT
import base64
# most of this is based on:
# https://varunver.wordpress.com/2017/08/10/python-smtplib-send-email-with-attachments/


def emailFile(user_name, user_email, user_email_password, filename, subjectTitle):
	if not user_email:
		print("Could not find \"user_email\" in env")
	if not user_email_password:
		print("Could not find \"user_email_password\" in env")



	text="This is your workout for the week"
	outer = get_outer(user_name, user_email, subjectTitle, user_name, user_email) 
	attach_pdf(outer, filename, text)
	composed = outer.as_string()

	try:
		server = attempt_login(user_email, user_email_password)
		server.sendmail(user_email, user_email, composed)
	except:
		print ('Something went wrong...')
		return 
def get_env_var(env_var):
	return os.environ.get(env_var, None)

def attach_pdf(outer, filename, text):
	with open(filename, 'rb') as fp:
		msg = MIMEBase('application', "octet-stream")
		msg.set_payload(fp.read())
		encoders.encode_base64(msg)
		msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(filename))
		outer.attach(MT(text))
		outer.attach(msg)

def attempt_login(email, password):
		try:  

			server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
			server.ehlo()
			server.login(email, password)
			#writer.writerow([name, email, company])
			return server
		except:  
			return None 


def get_outer(other_full_name, other_email, subject, your_full_name, your_email):
	outer = MIMEMultipart()
	outer['Subject'] = subject 
	outer['To'] =  other_full_name + "<" + other_email + ">"
	outer['From'] = your_full_name + " <" + your_email + ">"
	return outer



