from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_application():
    """Generates a formatted application based on user inputs and saves it to a text and PDF file."""
    print("\n--- Application Generator ---\n")

    # Gather user inputs
    application_name = input("Enter the application name (e.g., Leave Application): ").strip()
    receiver_name = input("Enter the receiver's name (e.g., HR Manager): ").strip()
    sender_name = input("Enter your name: ").strip()
    sender_address = input("Enter your address: ").strip()
    sender_designation = input("Enter your designation (optional, press Enter to skip): ").strip()
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
    {sender_address}
    {sender_designation if sender_designation else ""}
    {contact_info if contact_info else ""}
    """

    # Display the application
    print("\n--- Generated Application ---\n")
    print(application_template)

    # Save the application to a text file
    file_name_txt = f"{application_name.replace(' ', '_')}.txt"
    with open(file_name_txt, 'w') as file:
        file.write(application_template)

    print(f"\nApplication saved to text file: {file_name_txt}")

    # Save the application to a PDF file
    file_name_pdf = f"{application_name.replace(' ', '_')}.pdf"
    c = canvas.Canvas(file_name_pdf, pagesize=letter)
    c.setFont("Helvetica", 12)

    # Write the content line by line in the PDF
    y_position = 750  # Start position for writing text
    line_spacing = 15

    for line in application_template.splitlines():
        if line.strip():  # Avoid empty lines
            c.drawString(72, y_position, line)
            y_position -= line_spacing

    c.save()
    print(f"Application saved to PDF file: {file_name_pdf}")

# Run the application generator
if __name__ == "__main__":
    generate_application()
