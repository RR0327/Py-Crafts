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

def send_email(to_emails, subject, message):
    """Send an email notification to multiple recipients."""
    try:
        # Set up the email
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Send to each recipient
        for to_email in to_emails:
            msg['To'] = to_email  # Set the recipient's email
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(SENDER_EMAIL, SENDER_PASSWORD)
                server.send_message(msg)

            print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Dictionary to store users and their email addresses with reminders
users = {}

def add_user():
    """Add a new user and schedule reminders dynamically."""
    name = input("Enter user's name: ").strip()
    emails = input("Enter user's email(s) (comma-separated): ").strip().split(',')

    # Store user information (name, email(s), and reminders)
    reminders = {
        "sleep": input("Set sleep reminder time (HH:MM, 24-hour format): ").strip(),
        "work_break": input("Set work break reminder time (HH:MM, 24-hour format): ").strip(),
        "study_break": input("Set study break reminder time (HH:MM, 24-hour format): ").strip(),
        "social_media_break": input("Set social media break reminder time (HH:MM, 24-hour format): ").strip(),
    }

    # Add the user and their email addresses and reminders
    users[name] = {
        'emails': emails,
        'reminders': reminders
    }

    # Schedule reminders for the user
    for reminder, time_str in reminders.items():
        schedule.every().day.at(time_str).do(send_email, to_emails=emails, 
                                             subject=f"{reminder.capitalize()} Reminder",
                                             message=f"Hi {name}, this is your {reminder} reminder!")

    # Add custom reminders
    while True:
        custom = input("Add a custom reminder (or press Enter to skip): ").strip()
        if not custom:
            break
        time_str = input(f"Set time for '{custom}' (HH:MM, 24-hour format): ").strip()
        schedule.every().day.at(time_str).do(send_email, to_emails=emails, 
                                             subject=f"{custom} Reminder",
                                             message=f"Hi {name}, this is your '{custom}' reminder!")

    print(f"User {name} added and reminders scheduled successfully.")

def schedule_email():
    """Schedule a bus schedule notification email to multiple users."""
    emails = input("Enter the recipient's email(s) (comma-separated): ").strip().split(',')
    schedule_time = input("Enter the schedule time (HH:MM in 24-hour format): ")

    # Create message content
    subject = "Scheduled Notification"
    message = f"Hello,\n\nYour bus schedule has been changed. Please check your transport website.\nThank you.\n\nRegards,\nTransport group\nTime: {schedule_time}"

    # Schedule the email to be sent daily at the specified time
    schedule.every().day.at(schedule_time).do(send_email, to_emails=emails, subject=subject, message=message)
    print(f"Scheduled email to be sent at {schedule_time} every day to {', '.join(emails)}.")

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting program. All schedules stopped.")

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
        print("2. Schedule a Bus Schedule Email")
        print("3. Start Reminder Service")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_user()
        elif choice == "2":
            schedule_email()
        elif choice == "3":
            start_reminders()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
