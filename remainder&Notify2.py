import smtplib
import schedule
import time
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load or initialize user data
USER_DATA_FILE = "user_data.json"

def load_user_data():
    """Load user data from a JSON file."""
    try:
        with open(USER_DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_user_data(users):
    """Save user data to a JSON file."""
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(users, file, indent=4)

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "hassanrakib0327@gmail.com"  # Replace with your email
SENDER_PASSWORD = "R-12"      # Replace with your password

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

# User management
def add_user():
    """Add a new user to the system."""
    users = load_user_data()

    name = input("Enter user's name: ").strip()
    email = input("Enter user's email: ").strip()
    
    if name in users:
        print("User already exists.")
        return

    # Add reminder preferences
    reminders = {
        "sleep": input("Set sleep reminder time (HH:MM, 24-hour format): ").strip(),
        "work_break": input("Set work break reminder time (HH:MM, 24-hour format): ").strip(),
        "study_break": input("Set study break reminder time (HH:MM, 24-hour format): ").strip(),
        "social_media_break": input("Set social media break reminder time (HH:MM, 24-hour format): ").strip(),
    }

    # Add custom reminders
    custom_reminders = []
    while True:
        custom = input("Add a custom reminder (or press Enter to skip): ").strip()
        if not custom:
            break
        time = input(f"Set time for '{custom}' (HH:MM, 24-hour format): ").strip()
        custom_reminders.append({"reminder": custom, "time": time})

    # Save the user
    users[name] = {
        "email": email,
        "reminders": reminders,
        "custom_reminders": custom_reminders
    }
    save_user_data(users)
    print("User added successfully.")

def add_reminder():
    """Add a new reminder for an existing user."""
    users = load_user_data()

    name = input("Enter the name of the user to add a reminder for: ").strip()
    if name not in users:
        print("User not found.")
        return

    # Add new custom reminder
    custom = input("Enter the custom reminder description: ").strip()
    time_str = input("Set time for the reminder (HH:MM, 24-hour format): ").strip()

    users[name]["custom_reminders"].append({"reminder": custom, "time": time_str})
    save_user_data(users)
    print(f"Custom reminder added for {name}.")

    # Schedule the new reminder immediately
    schedule.every().day.at(time_str).do(send_email, to_email=users[name]["email"], 
                                         subject=f"{custom} Reminder",
                                         message=f"Hi {name}, this is your '{custom}' reminder!")

def schedule_reminders():
    """Schedule reminders for all users."""
    users = load_user_data()

    for name, data in users.items():
        email = data["email"]

        # Schedule default reminders
        for reminder, time_str in data["reminders"].items():
            schedule.every().day.at(time_str).do(send_email, to_email=email, 
                                                subject=f"{reminder.capitalize()} Reminder",
                                                message=f"Hi {name}, this is your {reminder} reminder!")

        # Schedule custom reminders
        for custom in data["custom_reminders"]:
            schedule.every().day.at(custom["time"]).do(send_email, to_email=email, 
                                                      subject=f"{custom['reminder']} Reminder",
                                                      message=f"Hi {name}, this is your '{custom['reminder']}' reminder!")

# Main loop
def main():
    """Main function to run the reminder system."""
    print("\n--- Reminder and Notification System ---\n")
    while True:
        print("1. Add User")
        print("2. Add Reminder for User")
        print("3. Start Reminder Service")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_user()
        elif choice == "2":
            add_reminder()
        elif choice == "3":
            print("Starting reminder service...")
            schedule_reminders()
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
