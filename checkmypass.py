import requests
import hashlib
import sys

# Function to send a request to the Pwned Passwords API and get the response
def request_api_data(query_char):
	url = 'https://api.pwnedpasswords.com/range/' + query_char
	res = requests.get(url)
	if res.status_code != 200:
		raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again.')
	return res

# Function to check if a password is in the API's response and get the count of how many times it's been seen in data breaches
def get_password_leaks_count(hashes, hash_to_check):
	hashes = (line.split(':') for line in hashes.text.splitlines())
	for h, count in hashes:
		if h == hash_to_check:
			return count
	return 0

# Function to hash a password, send the first 5 characters of the hash to the API, and check if the rest of the hash is in the API's response
def pwned_api_check(password):
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	first5_char, tail = sha1password[:5], sha1password[5:]
	response = request_api_data(first5_char)
	return get_password_leaks_count(response, tail)

# Main function to loop through each password, check if it's been leaked, and print the result
def main(args):
	for password in args:
		count = pwned_api_check(password)
		if count:
			print(f'{password} was found {count} times. You should change to a better password')
		else:
			print(f'{password} was not found. It is a strong password')
	return 'Check complete'

# This is the entry point for the program. The main function is called with command-line arguments as the passwords to check.
if __name__ == "__main__":
	sys.exit(main(sys.argv[1:]))
