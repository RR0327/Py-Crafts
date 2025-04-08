def generate_application():
    """Generates a formatted application based on user inputs and saves it to a text file."""
    print("\n--- Application Generator ---\n")

    # Gather user inputs
    application_name = input("Enter the application name (e.g., Leave Application): ").strip()
    receiver_name = input("Enter the receiver's name (e.g., HR Manager): ").strip()
    sender_name = input("Enter your name: ").strip()
    date = input("Enter the date (e.g., 25 January 2025): ").strip()
    subject = input("Enter the subject (optional, press Enter to skip): ").strip()
    body = input("Enter the body of the application: ").strip()
    contact_info = input("Enter your contact information (optional, press Enter to skip): ").strip()

    # Create the application template
    application_template = f"""
    {application_name}

    To,
    {receiver_name}

    Date: {date}

    Subject: {subject if subject else "(No Subject)"}

    Dear {receiver_name},

    {body}

    Sincerely,
    {sender_name}
    {contact_info if contact_info else ""}"""
    

    # Display the application
    print("\n--- Generated Application ---\n")
    print(application_template)

    # Save the application to a text file
    file_name = f"{application_name.replace(' ', '_')}.txt"
    with open(file_name, 'w') as file:
        file.write(application_template)

    print(f"\nApplication saved to file: {file_name}")

# Run the application generator
if __name__ == "__main__":
    generate_application()