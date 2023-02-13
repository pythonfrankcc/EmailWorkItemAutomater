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

#function of the user's email that you want to use
def search(key, value, con):
    result, data = imap.search(None, key, '"{}"'.format(value))
    #result, data = imap.search(None, key, value)
    print("The type of data that is returned by imap.search is:", type(data[0]))
    print("Here is a sample of the data list returned: ", data[0])
    #the data returned by data[0] is bytes but data is a list of bytes
    return data

# select the e-mail label you want to focus on
#imap.select('Inbox')
res, messages = imap.select('Inbox')#this returns a list
#messages = imap.select('Inbox')#this returns a tuple
print("This is after the select label statement ",type(messages[0]))
print("This is a sample after the select label statement ",messages[0])
print("This is a sample after the select label statement ",int(messages[0]))

msgs = search('FROM', os.environ.get('EmailUser'), imap)
# calculates the total number of Incoming messages
#inbox_messages = int(msgs[0])
inbox_messages = len(msgs[0])

# determine the number of e-mails to be fetched
n = 3
# iterating over the e-mails
for i in range(inbox_messages, inbox_messages - n, -1): 
    for response in mseg:
        if isinstance(response, tuple):
            mseg = email.message_from_bytes(response[1])
            #print the whole message to see what you get
            #print(msg)
            
            # getting the sender's mail id
            From = mseg["From"]

            # getting the subject of the sent mail
            subject = mseg["Subject"]

            #placing the data in a file for read by the sticky notes, this is in append mode
            file1 = open(r"StickyNoteFile.txt", "a")
            file1.write(subject)

            # printing the details
            print("From : ", From)
            print("subject : ", subject)



#close file1 to free the memory acquired by file1
file1.close()
