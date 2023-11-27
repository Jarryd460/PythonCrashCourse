def show_messages(messages, sent_messages):
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)

messages = ["Hello World!", "How are you?", "Isn't the weather beautiful today"]
sent_messages = []

show_messages(messages, sent_messages)
print()
print(messages)
print(sent_messages)

messages = ["Hello World!", "How are you?", "Isn't the weather beautiful today"]
sent_messages = []

print()
show_messages(messages[:], sent_messages)
print()
print(messages)
print(sent_messages)