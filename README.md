# Password Strength Checker

This is a **Password Strength Checker** built in Python. The tool assesses the strength of a password based on the following criteria:

- Length of the password.
- Presence of uppercase and lowercase letters.
- Presence of numeric digits.
- Presence of special characters.

The password strength is then categorized into five levels:
1. **Very Weak**
2. **Weak**
3. **Moderate**
4. **Strong**
5. **Very Strong**

## Features

- **Length Check**: Ensures the password is at least 8 characters long.
- **Uppercase Letter Check**: Validates that the password contains at least one uppercase letter.
- **Lowercase Letter Check**: Validates that the password contains at least one lowercase letter.
- **Digit Check**: Ensures the password contains at least one numeric digit.
- **Special Character Check**: Validates that the password contains at least one special character (e.g., `!@#$%^&*()`).

## Code Overview

The code works by checking the password against the following rules:
1. **Length**: The password should have a minimum length of 8 characters.
2. **Uppercase**: The password must contain at least one uppercase letter.
3. **Lowercase**: The password must contain at least one lowercase letter.
4. **Digit**: The password must contain at least one number.
5. **Special Character**: The password must contain at least one special character.

If the password meets all criteria, it will be marked as "Very Strong." Otherwise, a description of what needs to be improved will be displayed.
