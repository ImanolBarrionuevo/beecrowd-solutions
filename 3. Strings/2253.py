# Function to validate a password based on length and character composition
def validate_password(password):
    # Check password length
    if len(password) < 6 or len(password) > 32:
        return "Senha invalida."

    # Check that password contains only letters and digits
    elif not password.isalnum():
        return "Senha invalida."

    # Check for at least one uppercase letter, one lowercase letter, and one digit
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    if not has_upper or not has_lower or not has_digit:
        return "Senha invalida."
    else:
        return "Senha valida."

# Continuously read and validate passwords until EOF
while True:
    try:
        print(validate_password(input()))
    except EOFError:
        break