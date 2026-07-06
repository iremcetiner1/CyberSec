def check_length(password):
    if len(password) < 12:
       return print("Password Analysis Length: FAIL (Minimum 12 characters required)")
    return print("Password Analysis Length: PASS (Minimum 12 characters met)")
def check_uppercase(password):
    if not any(c.isupper() for c in password):
        return print("Password Analysis Uppercase: FAIL (At least one uppercase letter required)")
    return print("Password Analysis Uppercase: PASS (Uppercase letter found)")
def check_lowercase(password):
    if not any(c.islower() for c in password):
        return print("Password Analysis Lowercase: FAIL (At least one lowercase letter required)")
    return print("Password Analysis Lowercase: PASS (Lowercase letter found)")