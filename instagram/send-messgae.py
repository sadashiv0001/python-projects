# instabot is not officially supported by Instagram and may violate their terms.
# Its functionality and stability are not guaranteed.
# Using it could lead to account restrictions.

from instabot import Bot

bot = Bot()

def send_message():
    bot.send_message("Hi Brother", ["Sadashiv Mitra"])

def perform_instagram_action():
    try:
        #  Instagram action here
        bot.login(username="test_sender", password="ABC123")
        send_message()
    except Exception as e:
        if "429" in str(e):
            print("Rate limit exceeded. Sleeping for 5 minutes.")
            time.sleep(300)  # Sleep for 5 minutes (300 seconds)
            perform_instagram_action()  # Retry the action after sleeping

# Call the function to perform the Instagram action
perform_instagram_action()
