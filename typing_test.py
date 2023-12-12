import time

def typing_speed_test():
    print("Welcome to the Typing Speed Test!")
    passage = "The quick brown fox jumps over the lazy dog"  # You can change the passage here

    print("Type this: ")
    print(passage)
    input("Press Enter when you're ready to start typing...")
    
    start_time = time.time()
    user_input = input("Start typing the passage: ")
    end_time = time.time()

    time_taken = end_time - start_time
    words = len(passage.split())
    user_words = len(user_input.split())
    accuracy = sum(a == b for a, b in zip(user_input, passage)) / len(passage) * 100

    words_per_minute = (user_words / time_taken) * 60 if time_taken > 0 else 0

    print(f"\nTime taken: {time_taken:.2f} seconds")
    print(f"Your typing speed: {words_per_minute:.2f} words per minute")
    print(f"Accuracy: {accuracy:.2f}%")

typing_speed_test()