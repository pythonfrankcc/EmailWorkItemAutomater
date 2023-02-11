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
print("\n")
#from the above, it is seen that messages are a list of bytes and is of length 1


#select the intended email address that you want to filter by
result, data = imap.search(None, 'FROM', '"{}"'.format(os.environ.get('EmailUser')))
#check the data format for data
print("type of data format for the data variable is: ", type(data))
print("the first element for data is: ", data[0], " and is of type: ", type(data[0]))
print("the length of data is: ", len(data[0]))
print("\n")


#from the above it is seen that data is a list of bytes and is of length 1


#This will help reduce the computational time by getting the last emails in the search batch
data1 = data[0][-30:]
print("the value of data1: ",data1," and the type of data1 is: ", type(data1))
for i in data1.split():
	typ, msg = imap.fetch(i, '(RFC822)')
	for response in msg:
		if isinstance(response, tuple):
			msg = email.message_from_bytes(response[1])

			# getting the sender's mail id
			From = msg["From"]

			# getting the subject of the sent mail
			subject = msg["Subject"]

			print("subject : ", subject)
			print("From : ", From,"\n")

			#transfer the same to a file where the sticky notes will read from
			file1 = open(r"myfile.txt", "a")
			file1.write(subject)
			file1.write("\n")




# when you want to extract the whole batch of data from the search pattern that you have just created
# for i in data[0].split():
# 	typ, msg = imap.fetch(i, '(RFC822)')
# 	for response in msg:
# 		if isinstance(response, tuple):
# 			msg = email.message_from_bytes(response[1])
# 			# getting the sender's mail id
# 			From = msg["From"]

# 			# getting the subject of the sent mail
# 			subject = msg["Subject"]

# 			print("subject : ", subject)
# 			print("subject : ", subject)

# print("messages before the int conversion to check for the endianess", messages[0])
# int_val = int.from_bytes(messages[0], "big", signed = "False")
# print("the value of int_val is: ", int_val)
# print("\n")

# # calculates the total number of sent messages
# messages = int(messages[0])
# print("messages after the int conversion", messages)
# print("\n")
# #using the int.from_bytes returned sth different to using the int and thus could not be used



#you should close the connection and also logout
imap.close()
imap.logout()

#close file1 to free the memory acquired by file1
#always remember to close the file on completion
file1.close()