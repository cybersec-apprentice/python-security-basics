def check_password_strength(password):
    has_upper = False
    has_lower = False
    has_number = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_number = True

    if len(password) < 10:
        return "Password must be at least 10 characters long."
    if " " in password:
        return "Password cannot contain spaces."
    if not has_upper:
        return "Password must inlude an uppercase letter"
    if not has_lower:
        return "Password must include a lowercase letter"
    if not has_number:
        return "Password must include a number"

    return "Password meets all requirements"


def main():
    password = input("Enter Password: ")
    result = check_password_strength(password)
    print(result)


if __name__ == "__main__":
    main()
