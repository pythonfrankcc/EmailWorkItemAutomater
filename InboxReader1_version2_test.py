# import the modules
import imaplib							
import email
from email.header import decode_header
import webbrowser
import os

# establish connection with Gmail
server ="imap.gmail.com"					
imap = imaplib.IMAP4_SSL(server)

# instantiate the username and the password
username = os.environ.get('EmailUser')
password = os.environ.get('EmailPassword')

# login into the gmail account
imap.login(username, password)			

# select the e-mails
res, messages = imap.select('Inbox')
#check the data format for messages
print("type of data format for messages is: ", type(messages))
print("the first element for messages is: ",messages[0]," and is of type: ", type(messages[0]))
#from the above, it is seen that messages are a list of bytes and is of length 1


#select the intended email address that you want to filter by
result, data = imap.search(None, 'FROM', '"{}"'.format(os.environ.get('EmailUser')))
#check the data format for data
print("type of data format for the data variable is: ", type(data))
print("the first element for data is: ", data[0], " and is of type: ", type(data[0]))
#from the above it is seen that data is a list of bytes and is of length 1

# calculates the total number of sent messages
messages = int(messages[0])

# determine the number of e-mails to be fetched
n = 3

# iterating over the e-mails
for i in range(messages, messages - n, -1):
	res, msg = imap.fetch(str(i), "(RFC822)")	
	for response in msg:
		if isinstance(response, tuple):
			msg = email.message_from_bytes(response[1])
			
			# getting the sender's mail id
			From = msg["From"]

			# getting the subject of the sent mail
			subject = msg["Subject"]

			# printing the details
			print("From : ", From)
			print("subject : ", subject)


#you should close the connection and also logout
imap.close()
imap.logout()