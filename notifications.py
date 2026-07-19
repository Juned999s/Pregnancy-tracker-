"""
Local notification helper using plyer.

Note: this fires a notification only while the app is open/running.
True scheduled/background reminders (e.g. "notify me at 8am even if the
app is closed") require an Android foreground service or AlarmManager
access via pyjnius - that's a good next step once this base app works,
not included in this starter to keep the first build simple.
"""
from plyer import notification


def notify(title, message):
    try:
        notification.notify(
            title=title,
            message=message,
            app_name="Pregnancy Tracker",
            timeout=10
        )
    except Exception as e:
        print(f"Notification failed: {e}")
