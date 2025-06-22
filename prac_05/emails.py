"""
File: emails.py
Estimate: 20 minutes
Actual: 45 minutes
"""

def get_name_from_email(email):
    """Extract and return a name based on the email format."""
    parts = email.split('@')[0]  # take the part before the @
    name_parts = parts.replace('.', ' ').split()
    name = ' '.join(name_parts).title()
    return name


def main():
    """Get emails and names, confirm/correct names, and print results."""
    email_to_name = {}

    while True:
        email = input("Email: ").strip()
        if email == "":
            break

        default_name = get_name_from_email(email)
        confirm = input(f"Is your name {default_name}? (Y/n) ").strip().lower()

        if confirm not in ('', 'y', 'yes'):
            name = input("Name: ").strip()
        else:
            name = default_name

        email_to_name[email] = name

    # Print results
    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()
