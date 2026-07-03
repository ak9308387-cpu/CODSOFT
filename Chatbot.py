print("\n==============================")
print("🤖 Welcome to ArmaanBot")
print("A simple chatbot made by Armaan")
print("Type 'exit' whenever you want to end the chat.")
print("==============================")

while True:
    message = input("\nYou: ").strip().lower()

    if message in ("hi", "hello", "hey"):
        print("ArmaanBot: Hey!  Nice to see you. How can I help you today?")

    elif "how are you" in message:
        print("ArmaanBot: I'm doing well. Thanks for asking! Hope you're having a great day too.")

    elif "your name" in message or "who are you" in message:
        print("ArmaanBot: I'm ArmaanBot, a beginner-friendly chatbot created by Armaan using Python.")

    elif "python" in message:
        print("ArmaanBot: Python is one of the easiest programming languages to learn. It's used for AI, websites, automation, and data science.")

    elif "college" in message:
        print("ArmaanBot: College life is a great time to learn new skills and build projects.")

    elif "internship" in message:
        print("ArmaanBot: Internships are a good way to gain practical experience and improve your coding skills.")

    elif "help" in message:
        print("ArmaanBot: You can ask me about Python, my name, college, internship, or simply greet me.")

    elif "thank" in message:
        print("ArmaanBot: You're always welcome! ")

    elif message in ("bye", "exit"):
        print("ArmaanBot: It was nice chatting with you. Goodbye and take care! 👋")
        break

    else:
        print("ArmaanBot: Hmm... I don't have an answer for that yet. Try asking something different.")
