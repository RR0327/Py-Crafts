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
    """Send an email notification."""
    try:
        # Set up the email
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)

        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def add_user():
    """Add a new user and schedule reminders dynamically."""
    name = input("Enter user's name: ").strip()
    email = input("Enter user's email: ").strip()

    # Add reminder preferences
    reminders = {
        "sleep": input("Set sleep reminder time (HH:MM, 24-hour format): ").strip(),
        "work_break": input("Set work break reminder time (HH:MM, 24-hour format): ").strip(),
        "study_break": input("Set study break reminder time (HH:MM, 24-hour format): ").strip(),
        "social_media_break": input("Set social media break reminder time (HH:MM, 24-hour format): ").strip(),
    }

    # Schedule default reminders
    for reminder, time_str in reminders.items():
        schedule.every().day.at(time_str).do(send_email, to_email=email, 
                                             subject=f"{reminder.capitalize()} Reminder",
                                             message=f"Hi {name}, this is your {reminder} reminder!")

    # Add custom reminders
    while True:
        custom = input("Add a custom reminder (or press Enter to skip): ").strip()
        if not custom:
            break
        time_str = input(f"Set time for '{custom}' (HH:MM, 24-hour format): ").strip()
        schedule.every().day.at(time_str).do(send_email, to_email=email, 
                                             subject=f"{custom} Reminder",
                                             message=f"Hi {name}, this is your '{custom}' reminder!")

    print("User added and reminders scheduled successfully.")

def schedule_email():
    """Schedule a bus schedule notification email."""
    to_email = input("Enter the recipient's email address: ")
    schedule_time = input("Enter the schedule time (HH:MM in 24-hour format): ")

    # Create message content
    subject = "Scheduled Notification"
    message = f"Hello,\n\nYour bus schedule has been changed. Please check your transport website.\nThank you.\n\nRegards,\nTransport group\nTime: {schedule_time}"

    # Schedule the email to be sent daily at the specified time
    schedule.every().day.at(schedule_time).do(send_email, to_email=to_email, subject=subject, message=message)
    print(f"Scheduled email to be sent at {schedule_time} every day to {to_email}.")

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting program. All schedules stopped.")

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
            print("Starting reminder service...")
            while True:
                schedule.run_pending()
                time.sleep(1)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
