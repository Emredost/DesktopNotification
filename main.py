from pync import Notifier

if __name__ == "__main__":
    notification_title = "Scheduled Reminder"
    notification_message = "Your scheduled notification has triggered!"

    Notifier.notify(notification_message, title=notification_title, timeout=10)

import plyer
from datetime import datetime
import time

# Ask the user to enter the time for the notification
user_time = input("Enter the time for the notification in HH:MM format: ")
try:
    user_time = datetime.strptime(user_time, "%H:%M").time()
except ValueError:
    print("Invalid time format. Please use HH:MM.")
    exit(1)

# Combine the user's time with today's date
scheduled_time = datetime.combine(datetime.today(), user_time)

# Calculate the delay in seconds until the scheduled time
current_time = datetime.now()
time_difference = scheduled_time - current_time
delay_seconds = time_difference.total_seconds()

if delay_seconds > 0:
    time.sleep(delay_seconds)
    notification_title = "Scheduled Reminder"
    notification_message = "Your scheduled notification has triggered!"
    notification_timeout = 10  # Notification will stay for 10 seconds

    plyer.notification.notify(
        title=notification_title,
        message=notification_message,
        timeout=notification_timeout
    )
else:
    print("Scheduled time is in the past.")
