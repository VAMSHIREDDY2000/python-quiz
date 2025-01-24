# Define the questions, options, and the correct answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["Shakespeare", "Dickens", "Austen", "Hemingway"],
        "answer": "Shakespeare"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Jupiter"
    },
    {
        "question": "What is the boiling point of water in Celsius?",
        "options": ["90", "100", "110", "120"],
        "answer": "100"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Van Gogh", "Picasso", "Da Vinci", "Rembrandt"],
        "answer": "Da Vinci"
    }
]

def ask_question(q):
    """Ask a single question and return whether the user's answer is correct."""
    print(f"Question: {q['question']}")
    for i, option in enumerate(q['options']):
        print(f"{i + 1}. {option}")
    
    # Get the user's answer
    while True:
        try:
            user_choice = int(input("Enter your choice (1/2/3/4): "))
            if user_choice in [1, 2, 3, 4]:
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
    
    # Check if the answer is correct
    user_answer = q['options'][user_choice - 1]
    if user_answer == q['answer']:
        print("Correct!\n")
        return True
    else:
        print(f"Wrong! The correct answer is: {q['answer']}\n")
        return False

def run_quiz():
    """Run the GK quiz and return the user's score."""
    score = 0
    total_questions = len(questions)
    
    print("Welcome to the General Knowledge Quiz!")
    print(f"You will be asked {total_questions} questions.\n")

    for question in questions:
        if ask_question(question):
            score += 1

    # Display the final score
    print(f"Your final score is: {score} out of {total_questions}")
    percentage = (score / total_questions) * 100
    print(f"Your score percentage is: {percentage}%")

if __name__ == "__main__":
    run_quiz()
