import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a great programming language for beginners.",
    "Typing speed can be improved with regular practice.",
    "Artificial Intelligence is changing the world.",
    "Consistency is the key to mastering any skill."
]

def calculate_accuracy(original, typed):
    original = original.strip()
    typed = typed.strip()
    
    correct = 0
    for i in range(min(len(original), len(typed))):
        if original[i] == typed[i]:
            correct += 1
    total = max(len(original), len(typed))
    return round((correct / total) * 100, 2)

def typing_test():
    print("\n💬 Welcome to the Typing Speed Test!")
    print("Made by Ghanashyam Budhathoki!\n")
    input("Press Enter when you're ready to start...")

    test_sentence = random.choice(sentences)
    print("\n📝 Type this sentence:\n")
    print(f"👉 {test_sentence}\n")

    input("Press Enter to begin typing...")
    start_time = time.time()
    typed_input = input("\nStart typing here:\n\n")
    end_time = time.time()

    time_taken = end_time - start_time
    time_taken = max(time_taken, 1)  # Avoid division by zero

    word_count = len(test_sentence.split())
    wpm = round((word_count / time_taken) * 60, 2)
    accuracy = calculate_accuracy(test_sentence, typed_input)

    print("\n⌛ Time taken:", round(time_taken, 2), "seconds")
    print("🔤 Words per minute (WPM):", wpm)
    print("🎯 Accuracy:", accuracy, "%")

    if accuracy == 100:
        print("🏆 Perfect! Great job!")
    elif accuracy >= 80:
        print("👍 Well done! Keep practicing!")
    else:
        print("🛠️ Needs improvement. Keep typing!")

if __name__ == "__main__":
    typing_test()
