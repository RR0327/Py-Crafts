import smtplib
import schedule
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "franklin.gta.vmi@gmail.com"  # Replace with your email
SENDER_PASSWORD = "wxnx qiyf xkib cfdy"  # Replace with your password

def send_email(to_email, subject, message):
    """Send an email notification to a single recipient."""
    try:
        # Set up the email
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = to_email  # Single recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Send the email to the recipient
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)

        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Dictionary to store users with their names, emails, and reminders
users = {}

def add_user():
    """Add a new user and schedule reminders dynamically."""
    name_input = input("Enter user's name(s) (comma-separated): ").strip()
    names = name_input.split(',')
    
    emails_input = input("Enter user's email(s) (comma-separated): ").strip()
    emails = emails_input.split(',')

    # Store user information (names, email(s), and reminders)
    reminders = {
        "sleep": input("Set sleep reminder time (HH:MM, 24-hour format): ").strip(),
        "work_break": input("Set work break reminder time (HH:MM, 24-hour format): ").strip(),
        "study_break": input("Set study break reminder time (HH:MM, 24-hour format): ").strip(),
        "social_media_break": input("Set social media break reminder time (HH:MM, 24-hour format): ").strip(),
    }

    # Add the users and their emails and reminders
    for name in names:
        users[name.strip()] = {
            'emails': emails,
            'reminders': reminders
        }

    # Schedule reminders for each user
    for name in names:
        for reminder, time_str in reminders.items():
            schedule.every().day.at(time_str).do(send_reminder_to_user, name.strip(), reminder, time_str, emails)

    # Add custom reminders
    while True:
        custom = input("Add a custom reminder (or press Enter to skip): ").strip()
        if not custom:
            break
        time_str = input(f"Set time for '{custom}' (HH:MM, 24-hour format): ").strip()
        for name in names:
            schedule.every().day.at(time_str).do(send_reminder_to_user, name.strip(), custom, time_str, emails)

    print(f"Users {', '.join(names)} added and reminders scheduled successfully.")

def send_reminder_to_user(name, reminder, time_str, emails):
    """Send the reminder to all emails of a specific user."""
    subject = f"{reminder.capitalize()} Reminder"
    message = f"Hi {name}, this is your {reminder} reminder!"

    # Send the reminder to each email address individually
    for email in emails:
        send_email(email, subject, message)

def start_reminders():
    """Start the reminder service for all users."""
    print("Starting reminder service...")
    while True:
        schedule.run_pending()
        time.sleep(1)

# Main loop
def main():
    """Main function to run the reminder and scheduling system."""
    print("\n--- Reminder and Email Notification System ---\n")
    while True:
        print("1. Add User and Set Reminders")
        print("2. Start Reminder Service")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_user()
        elif choice == "2":
            start_reminders()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
