import json

def load_questions(filename):
    with open(filename, 'r') as file:
        questions = json.load(file)
    return questions

def ask_question(question_data):
    print("\n" + question_data["question"])
    for idx, choice in enumerate(question_data["choices"], start=1):
        print(f"{idx}. {choice}")
    answer = input("Enter the number of your answer: ")
    return question_data["choices"][int(answer) - 1] == question_data["answer"]

def run_quiz(questions):
    score = 0
    for question_data in questions:
        if ask_question(question_data):
            score += 1
    return score

def main():
    questions = load_questions('questions.json')
    print("Welcome to the Cybersecurity Quiz!")
    print("You will be asked 50 questions.")
    print("Let's begin...\n")
    score = run_quiz(questions)
    print(f"\nYour final score is: {score} out of {len(questions)}")

if __name__ == "__main__":
    main()
