from plyer import notification

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = 'D:\\Programs\\Python\\Notification System\\icon.ico',
        timeout = 6
    )

if __name__ == "__main__":
    notifyMe("Manav", "Lets play with python.")
        