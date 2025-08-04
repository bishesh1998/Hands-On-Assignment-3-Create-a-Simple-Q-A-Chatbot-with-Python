from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chatbot instance
chatbot = ChatBot('TerminalBot')

# Create a new trainer for the chatbot
trainer = ListTrainer(chatbot)

# Train the chatbot on a custom list of conversations
trainer.train([
    "Hi there!",
    "Hello",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
])

print("TerminalBot is ready to chat! Type 'exit' to end the conversation.\n")

# Terminal chat loop
while True:
    try:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("TerminalBot: Goodbye!")
            break
        response = chatbot.get_response(user_input)
        print(f"TerminalBot: {response}")
    except (KeyboardInterrupt, EOFError, SystemExit):
        break