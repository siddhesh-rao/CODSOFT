import re

def chatbot():
    print("Chatbot: Hello! I'm RuleBot. How can I help you? (type 'bye' to exit)\n")
    
    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day 😊")
            break

        # Greeting patterns
        elif re.search(r"\b(hi|hello|hey)\b", user_input):
            print("Chatbot: Hello! How can I assist you?")

        # Asking name
        elif "your name" in user_input:
            print("Chatbot: I'm a simple chatbot built using rule-based logic!")

        # Basic feelings
        elif "how are you" in user_input:
            print("Chatbot: I'm doing great! Thanks for asking 😊")

        # Time query
        elif "time" in user_input:
            print("Chatbot: I can’t check real time yet, but I know it’s always a good time to learn 😄")

        # Weather query
        elif "weather" in user_input:
            print("Chatbot: I can’t check weather, but I hope it's sunny wherever you are!")

        # Default fallback
        else:
            print("Chatbot: Sorry, I didn’t understand that. Can you rephrase?")

# Run the chatbot
chatbot()
