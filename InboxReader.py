# Importing libraries
import imaplib, email

import os

#the email address and password are set on machine environment variables
#user = os.getenv("EmailUser", default=None)
user = os.environ.get('EmailUser')

#password = os.getenv("EmailPassword", default=None), app password created in google
password = os.environ.get('EmailPassword')
imap_url = 'imap.gmail.com'

#__________modular functions for automating the work _______________________________________________
# Function to get email content
#pep 8 standards function names should be lowercase separated by underscores in the case where they are multiple words
def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)

# Function to search for a key value pair
def search(key, value, con):
    result, data = con.search(None, key, '"{}"'.format(value))
    return data

# Function to get the list of emails under this label
def get_emails(result_bytes):
    msgs = [] # all the email data are pushed inside an array
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)
 
    return msgs[0:5]

#_______________________________________________________________________________________________________


#start the email connection
con = imaplib.IMAP4_SSL(imap_url)

# logging the user in
con.login(user, password)

# calling function to check for email under this label
con.select('Inbox')

# fetching emails from this user my email address
msgs = get_emails(search('FROM', os.environ.get('EmailUser'), con))
print(msgs)