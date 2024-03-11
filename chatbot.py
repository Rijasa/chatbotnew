import random

def chatbot():
    # Greetings
    greetings = ["Hello!", "Hi there!", "Hey!", "Hi! How can I help you today?"]
    print(random.choice(greetings))

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Goodbye!")
            break
        elif "how are you" in user_input:
            print("I'm just a computer program, but thanks for asking!")
        elif "your name" in user_input:
            print("I'm just a humble chatbot.")
        elif "weather" in user_input:
            print("I'm sorry, I don't have access to real-time weather data.")
        elif "joke" in user_input:
            jokes = ["Why don't scientists trust atoms? Because they make up everything!", "Parallel lines have so much in common. It’s a shame they’ll never meet."]
            print(random.choice(jokes))
        else:
            print("I'm sorry, I didn't understand that.")

chatbot()