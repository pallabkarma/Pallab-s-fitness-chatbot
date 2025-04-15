
def personal_trainer():
    print("Welcome to Pallab's Personal Trainer Chatbot!")
    print("Tell me your goal. For example: 'I want to lose weight'")

    user_input = input("You: ").lower()

    if "lose weight" in user_input:
        print("\nHere's a sample 30-Day Weight Loss Plan for you:\n")
        print("Day 1: Brisk walking, Squats, Push-ups, Plank, Stretching (30 mins)")
        print("Day 2: Cycling, Lunges, Incline Push-ups, Side Plank, Stretching (30 mins)")
        print("Day 3: Rest - Light walk or yoga\n")
        print("...and so on. (You can extend this plan!)")
    else:
        print("I'm still learning how to help with that goal. Try typing: 'I want to lose weight'")

if __name__ == "__main__":
    personal_trainer()


