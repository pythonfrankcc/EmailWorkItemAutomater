This is the creation of a gmail sticky note task automater


IMAP should be enabled on gmail account before beginning


Documentation on the use of Imap can be found on the following link
https://docs.python.org/3/library/imaplib.html


PEP naming conventions as a standard
https://www.python.org/dev/peps/pep-0008/#function-and-variable-names


For this to work you will need to use an app password and it is important to note that on changing the password of your gmail account you will need to create a new app password, ie , if you ever change your password.
The password used in the script is an app password

Link for the same:
https://support.google.com/accounts/answer/185833#zippy=%2Capp-passwords-revoked-after-password-change


Here is a link on how to take advantage of your environment variables to store the username and password and avoid using them in code: https://www3.ntu.edu.sg/home/ehchua/programming/howto/Environment_Variables.html#:~:text=2.2%20Set%2FUnset%2FChange%20an,it%20to%20an%20empty%20string.

For it to take effect on test restart the interpreter and list the variables using the below code:
for key in os.environ:
    print(key, '=>', os.environ[key])


On using the per_counter on the script, I found that the rough execution time is 8.44 minutes which is roughly 9 minutes
