import random

questions = [
    ["1. What is the capital city of Canada?", "A. Toronto", "B. Vancouver", "C. Montreal", "D. Ottawa", 4],
    ["2. Who developed the theory of general relativity?", "A. Isaac Newton", "B. Albert Einstein", "C. Galileo Galilei", "D. Stephen Hawking", 2],
    ["3. What is the hardest natural substance on Earth?", "A. Gold", "B. Iron", "C. Diamond", "D. Quartz", 3],
    ["4. In which country is the Great Pyramid of Giza located?", "A. Mexico", "B. Egypt", "C. Peru", "D. India", 2],
    ["5. What element does 'O' represent on the periodic table?", "A. Oxygen", "B. Osmium", "C. Ozone", "D. Olivine", 1],
    ["6. How many degrees are there in a circle?", "A. 360", "B. 180", "C. 90", "D. 270", 1],
    ["7. Who painted 'The Starry Night'?", "A. Leonardo da Vinci", "B. Claude Monet", "C. Vincent van Gogh", "D. Salvador Dalí", 3],
    ["8. What is the largest mammal in the world?", "A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus", 2],
    ["9. Which gas do plants absorb from the atmosphere?", "A. Oxygen", "B. Nitrogen", "C. Hydrogen", "D. Carbon Dioxide", 4],
    ["10. Which number is the only even prime number?", "A. 0", "B. 2", "C. 4", "D. 6", 2]
]

prizes = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]

def apply_5050(question):
    correct_index = question[5]
    options = [1, 2, 3, 4]
    options.remove(correct_index)
    to_remove = random.sample(options, 2)
    display_options = []
    for i in range(1, 5):
        if i not in to_remove:
            display_options.append(question[i])
    return display_options

def run_quiz():
    used_5050 = False
    used_skip = False

    for i, question in enumerate(questions):
        print(f"\n{question[0]}")

        while True:
            print("Options:")
            for j in range(1, 5):
                print(question[j])

            print("\nAvailable lifelines:")
            if not used_5050:
                print("- 5050 : Removes two incorrect options")
            if not used_skip:
                print("- skip : Skip this question")

            answer = input("Enter your answer (a, b, c, d, 5050, skip): ").strip().lower()

            if answer == "5050":
                if used_5050:
                    print("❌ You have already used the 50:50 lifeline.")
                else:
                    options_5050 = apply_5050(question)
                    print("\n50:50 Lifeline activated! Remaining options:")
                    for opt in options_5050:
                        print(opt)
                    used_5050 = True
                continue

            if answer == "skip":
                if used_skip:
                    print("❌ You have already used the skip lifeline.")
                else:
                    print("⏩ Question skipped.")
                    used_skip = True
                    break  # Skip to next question

            elif answer in ['a', 'b', 'c', 'd']:
                user_choice = {'a': 1, 'b': 2, 'c': 3, 'd': 4}[answer]

                if user_choice == question[5]:
                    print("✅ Correct Answer!")
                    print(f"🎉 You won ₹{prizes[i]}")
                else:
                    correct_option = ['A', 'B', 'C', 'D'][question[5] - 1]
                    print(f"❌ Wrong! The correct answer was {correct_option}.")
                    print("💔 Better luck next time!")
                    return  # Exit the game
                break  # Proceed to next question
            else:
                print("❌ Invalid input. Please enter a, b, c, d, 5050, or skip.")

    print("\n🏆 Congratulations! You have completed the quiz.")
    print(f"💰 Total Prize Money Won: ₹{prizes[-1]}")

# Start the game
run_quiz()
