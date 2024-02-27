def show_messages(messages):
    for message in messages:
        print(f'Message: {message}')


def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"Sending: {current_message}")
        sent_messages.append(current_message)


short_messages = [
    "Hello!",
    "How are you?",
    "I'm good, thank you.",
    "What's up?",
    "Not much, just chilling.",
    "Wanna hang out later?",
    "Sure, that sounds like fun!",
    "See you soon!",
    "Bye!",
    "Take care!"
]
# archive short messages
# messages_copy = short_messages[:]
sent_messages = []

send_messages(short_messages, sent_messages)

print("\nList of Short Messages:")
show_messages(short_messages)

print("\nList of Sent Messages:")
show_messages(sent_messages)