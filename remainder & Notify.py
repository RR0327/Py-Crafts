import smtplib  
import schedule  
import time
from email.mime.text import MIMEText  
from email.mime.multipart import MIMEMultipart  

def send_email(to_email, subject, message): 
    sender_email = "franklin.gta.vmi@gmail.com"   
    sender_password = "wxnx qiyf xkib cfdy"

    # Set up the email  
    msg = MIMEMultipart()  
    msg['From'] = sender_email  
    msg['To'] = to_email  
    msg['Subject'] = subject  

    # Attach the message body  
    msg.attach(MIMEText(message, 'plain'))  

    try:  
        with smtplib.SMTP('smtp.gmail.com', 587) as server:  
            server.starttls()  # Start TLS encryption  
            server.login(sender_email, sender_password)  # Login  
            server.send_message(msg)  # Send email  
            print(f"Email sent successfully to {to_email}")  
    except Exception as e:  
        print(f"Failed to send email: {e}")  

def schedule_email():  
    to_email = input("Enter the recipient's email address: ")  
    schedule_time = input("Enter the schedule time (HH:MM in 24-hour format): ")  
    
    # Create message content  
    subject = "Scheduled Notification"  
    message = f"Hello,\n\nYour bus schedule has been changed. Please check on your transport website.\nThank you.\n\nRegards,\nTransport group\nTime:{schedule_time}"  

    # Schedule the email to be sent daily at the specified time  
    schedule.every().day.at(schedule_time).do(send_email, to_email, subject, message)  
    print(f"Scheduled email to be sent at {schedule_time} every day to {to_email}.")  

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting program. All schedules stopped.")


choice = input("Do you want to schedule an email notification? (y/n): ")  
if choice.lower() == 'y':  
    schedule_email()
else:  
    print("Goodbye!")