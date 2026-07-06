from getpass import getpass
from checker import check_length
from checker import check_uppercase
from checker import check_lowercase
password = getpass("Enter password: ")
length_ok = check_length(password)
print(length_ok)
upper_ok = check_uppercase(password)
print(upper_ok) 
lower_ok = check_lowercase(password)
print(lower_ok)     