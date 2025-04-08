"""from plyer import notification
import time

notification.notify(
    title = 'You are bus schedule has been changed for today.',
    message = 'This is a notification!',
    app_name = 'Plyer Example',
    timeout = 5
)

time.sleep(5)"""

import time
from plyer import notification

time.sleep(30 * 60)

notification.notify(
    title = 'Hello',
    message = 'Hello, Bro. Time for Varsity.',
    timeout = 600
)
