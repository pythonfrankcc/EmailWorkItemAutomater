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
user = os.environ.get('EmailUser')
password = os.environ.get('EmailPassword')

# login into the gmail account
imap.login(user, password)          

# select the e-mails
res, messages = imap.select('Inbox')


#functionof the user's email that you want to use
def search(key, value, con):
    result, data = con.search(None, key, '"{}"'.format(value))
    #result, data = con.search(None, key, value)
    print("The type of data that is returned by con.search is:", type(data))
    print("Here is a sample of the data list returned: ", data[0])
    return data

msgs = search('FROM', os.environ.get('EmailUser'), messages)
# calculates the total number of Incoming messages
inbox_messages = int(msgs[0])

# determine the number of e-mails to be fetched
n = 3

# iterating over the e-mails
for i in range(inbox_messages, inbox_messages - n, -1):
    res, msg = imap.fetch(str(i), "(RFC822)")   
    for response in msg:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            #print the whole message to see what you get
            print(msg)
            
            # getting the sender's mail id
            From = msg["From"]

            # getting the subject of the sent mail
            subject = msg["Subject"]

            #placing the data in a file for read by the sticky notes, this is in append mode
            file1 = open(r"StickyNoteFile.txt", "a")
            file1.write(subject)

            # printing the details
            print("From : ", From)
            print("subject : ", subject)

#you should close the connection and also logout
imap.close()
imap.logout()

#close file1 to free the memory acquired by file1
file1.close()
