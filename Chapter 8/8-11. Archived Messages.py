def send_message(messages, sent_messages):
    for message in messages:
        print(message)
    while messages:
        sent = messages.pop()
        sent_messages.append(sent)


messages = ['Hello world!', 'Hi there!', 'salam!', "What's up guys!"]
sent_messages = []
send_message(messages[:], sent_messages)
print(messages)
print(sent_messages)

