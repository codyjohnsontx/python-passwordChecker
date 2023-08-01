# python-passwordChecker

Password Security Check <br>
This program uses the "Have I Been Pwned" API to check if your passwords have been leaked in any data breaches.

##How It Works
The program hashes the passwords and sends the first 5 characters of each hashed password to the "Have I Been Pwned" API. The API then responds with a list of known leaked hashed password suffixes and how many times they've appeared in data breaches. If the remaining characters of your hashed password are found in the API's response, then your password has been leaked.

##Requirements:
Python 3
The requests package (you can install it with pip install requests)

##How to Run
You can run this program from the command line and pass in the passwords you want to check as command-line arguments. 

##Here's an example of how to run the program:
python3 script.py password1 password2 password3

Just replace password1, password2, and password3 with the passwords you want to check.
