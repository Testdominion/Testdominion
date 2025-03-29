import re
import requests
import hashlib

def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase and lowercase letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Use both uppercase and lowercase letters.")

    # Check for numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")

    return score, feedback

def check_password_leak(password):
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()
    first5, rest = sha1_password[:5], sha1_password[5:]
    
    response = requests.get(f"https://api.pwnedpasswords.com/range/{first5}")
    if rest in response.text:
        return True
    return False

def main():
    password = input("Enter a password to check: ")
    
    score, feedback = check_password_strength(password)
    print(f"\nPassword Strength Score: {score}/4")

    if score < 4:
        print("Weak password! Suggestions:")
        for tip in feedback:
            print(f"- {tip}")

    if check_password_leak(password):
        print("\n⚠ WARNING: This password has been found in leaked databases! Use a different one.")
    else:
        print("\n✅ This password has not been leaked.")

if __name__ == "__main__":
    main()
