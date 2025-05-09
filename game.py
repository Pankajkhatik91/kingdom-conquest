def main():
    print("Welcome to Kingdom Conquest!")
    print("This is a test to verify the game is working")
    
    while True:
        choice = input("Choose difficulty (easy/normal/hard): ").lower()
        if choice in ["easy", "normal", "hard"]:
            print(f"\nYou selected: {choice}")
            print("Game is working! 🎉")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()