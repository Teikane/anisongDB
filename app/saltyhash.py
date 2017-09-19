from passlib.hash import argon2



###
# Input: A single string
# Output: A string 
# Desc: Generate a salt and hash the salted password.
###
def hash_password(password):
	return argon2.hash(str(password))
###
# Input: A hashed password
# Output: boolean 1 if matching password, 0 if not
# Desc: verify a stored password vs recently entered password.
###
def check_password(entered_password, stored_password):
	return argon2.verify(entered_password, stored_password)
