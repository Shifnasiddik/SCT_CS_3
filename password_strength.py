import re
def password_strength(password):
    strength = 0
    feedback = []
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("\nPassword should be at least 8 characters long.\n")
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("\nPassword should contain at least one uppercase letter.\n")
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("\nPassword should contain at least one lowercase letter.\n")
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("\nPassword should contain at least one digit.\n")
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("\nPassword should contain at least one special character.\n")
    if strength == 5:
        feedback.append("Password is Very Strong.")
    elif strength == 4:
        feedback.append("Password is Strong.")
    elif strength == 3:
        feedback.append("Password is Moderate.")
    elif strength == 2:
        feedback.append("Password is Weak.")
    else:
        feedback.append("Password is Very Weak.")
    return feedback
password = input("Enter a password to check its strength: ")
result = password_strength(password)
for message in result:
    print(message)
