# email Validator

def validate_email(email):
    if len(email) < 6:
        return False, "Too Short (minimum 6 characters)"
    if " " in email:
        return False, "Must not contain spaces"
    if email.count("@") != 1:
        return False, "Must Contain exactly one @"

    local, domain = email.split("@")

    if not local:
        return False, "Missing name before the @"
    if "." not in domain:
        return False, "Domain needs a dot"
    if domain.startswith(".") or domain.endswith("."):
        return False, "Domain can't start or end with a dot"

    return True, "Valid Email Address!"


def main():

    print("*** Welcome to Email Validator ***")
while True:
    email = input("Enter your email address: ").strip()
    is_valid, message = validate_email(email)
    print(message)
    if is_valid:
        break
