#_________________________________deleting the file created to make room foor the new updated___________
#before running this code delete the previous myfile in the same location as this __main__ file
import os
# try:
#     os.remove("myfile.txt")
# except FileNotFoundError as e:
#     print("File does not exist")
#_______________________________________________________________________________________________________








# Importing necessary libraries
#libraries for email manipulation
import imaplib, email

#libraries for acquiring environment variables for storing password and username
#import os
#libaries for calculation of elapsed time
import time

#the email address and password are set on machine environment variables, you can use any of the below to get the user
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
    #result, data = con.search(None, key, value)
    print("The type of data that is returned by con.search is:", type(data))
    print("Here is a sample of the data list returned: ", data[0])
    return data

# Function to get the list of emails under this label
def get_emails(result_bytes):
    msgs = [] # all the email data are pushed inside a list
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        #this is a list of bytes that now need encoding
        msgs.append(data)
 
    return msgs
#_______________________________________________________________________________________________________


#start the email connection
con = imaplib.IMAP4_SSL(imap_url)

# logging the user in
con.login(user, password)

# calling function to check for email under this label
con.select('Inbox')

msgs = get_emails(search('FROM', os.environ.get('EmailUser'), con))

#finding the required content from the messages
for msg in msgs[::-1]:
    for incoming in msg:
        if type(incoming) is tuple:
 
            # encoding set as utf-8
            content = str(incoming[1], 'utf-8')
            data = str(content)
 
            # Handling errors related to unicodencode
            try:
                indexstart = data.find("ltr")
                data2 = data[indexstart + 5: len(data)]
                indexend = data2.find("</div>")
 
                # printing the required content which we need
                # to extract from our email i.e our body
                extracted_data = data2[0: indexend]
                print(extracted_data)
                #placing the data in a file for read by the sticky notes, this is in append mode
                file1 = open(r"myfile.txt", "a")
                file1.write(extracted_data)
 
            except UnicodeEncodeError as e:
                pass
#you should close the connection and also logout
con.close()
con.logout()

#close file1 to free the memory acquired by file1
file1.close()

#calling the HtmlTagCleaner
#execfile('HtmlTagsCleaner.py')
with open('HtmlTagsCleaner.py') as infile:
    exec(infile.read())



















#_________________________________________testing part to see whether the code works before hand_________________________
#calculating the elapsed time it takes to call the function
#record start time
# start = time.perf_counter()

# # fetching emails from this user my email address
# msgs = get_emails(search('FROM', os.environ.get('EmailUser'), con))
# print(msgs)
# end = time.perf_counter()
# time_in_seconds = end - start
# print(time_in_seconds)
