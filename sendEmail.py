import maya.cmds as cmds
import smtplib
import email
import email.mime.application

from datetime import datetime
import getpass

def sendEmail():
	print '# Attempting to send email notification'
	scene = cmds.file(q=True, sn=True, shn=True)
	artist = getpass.getuser()
	
	# Basic information
	msg = email.mime.Multipart.MIMEMultipart()
	msg['Subject'] = 'Render Complete - %s' %(scene)
	msg['From'] = '' #Insert Sender
	msg['To'] = '' #Insert Receiver
	password = '' #Insert Sender's password
	
	body = email.mime.Text.MIMEText("""
	Artist: """ + artist + """
	Scene: """ + scene + """
	Timestamp: """ + datetime.now().strftime('%d/%m/%Y, %H:%M:%S') + """
	""")
	
	msg.attach(body)
	
	# Attachment
	#renderPath = cmds.renderSettings(fin=True, fp=True)[0]
	#filename = cmds.renderSettings(fin=True)[0]
	
	#fp = open(renderPath, 'rb')
	
	#attachment = email.mime.application.MIMEApplication(fp.read())
	#fp.close()
	#attachment.add_header('Content-Disposition', 'attachment', filename = filename)
	#msg.attach(attachment)
	
	# Send email via gmail server
	s = smtplib.SMTP('smtp.gmail.com:587')
	s.starttls()
	s.login(msg['From'], password)
	s.sendmail(msg['From'], [msg['To']], msg.as_string())
	s.quit()
	
	print '#Successfully sent email notification'