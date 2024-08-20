import re

# Function to check password complexity
def check_password_complexity(password):
    # Minimum length requirement
    min_length = 8

    # Criteria for a strong password
    length_criteria = len(password) >= min_length
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Count how many criteria are met
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])

    # Feedback messages
    feedback = []

    if not length_criteria:
        feedback.append(f"Password should be at least {min_length} characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not digit_criteria:
        feedback.append("Password should include at least one digit.")
    if not special_char_criteria:
        feedback.append("Password should include at least one special character.")

    # Password strength rating
    if criteria_met == 5:
        rating = "Strong"
    elif criteria_met == 4:
        rating = "Moderate"
    elif criteria_met == 3:
        rating = "Weak"
    else:
        rating = "Very Weak"

    return rating, feedback

# Command-Line Interface
def cli():
    print("Welcome to the Password Complexity Checker")
    while True:
        password = input("Enter a password to check its complexity (or type 'exit' to quit): ")
        
        if password.lower() == 'exit':
            break

        rating, feedback = check_password_complexity(password)
        print(f"\nPassword Rating: {rating}")
        if feedback:
            print("Suggestions to improve your password:")
            for suggestion in feedback:
                print(f"- {suggestion}")
        else:
            print("Your password is strong!")
        print("\n")

if __name__ == "__main__":
    cli()
