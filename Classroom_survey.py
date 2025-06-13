def get_questions():
    return [
        "Do you like Python? (yes/no)",
        "Have you used input() before? (yes/no)",
        "Do you enjoy group projects? (yes/no)",
        "Would you like to learn more about dictionaries? (yes/no)",
        "Is programming fun for you? (yes/no)"
    ]

def ask_questions_to_user(questions):
    print("\nPlease answer the following questions:")
    answers = []
    for question in questions:
        while True:
            answer = input(question + " ").strip().lower()
            if answer in ['yes', 'no']:
                answers.append(answer)
                break
            else:
                print("Please enter 'yes' or 'no'.")
    return answers

def summarize_results(responses, questions):
    summary = {question: {'yes': 0, 'no': 0} for question in questions}
    total_yes = 0
    total_no = 0

    for response in responses:
        for i, answer in enumerate(response):
            if answer in summary[questions[i]]:
                summary[questions[i]][answer] += 1
                if answer == 'yes':
                    total_yes += 1
                elif answer == 'no':
                    total_no += 1

    print("\nSurvey Results Summary:")
    for question, counts in summary.items():
        print(f"\n{question}")
        print(f"Yes: {counts['yes']} | No: {counts['no']}")

    print("\nOverall Totals:")
    print(f"Total Yes answers: {total_yes}")
    print(f"Total No answers: {total_no}")

def main():
    print("=== Classroom Survey Tool ===")
    questions = get_questions()
    all_responses = []
<<<<<<< HEAD
    for i in range (num_participants):
        print(f"\nParticipants {i + 1}, please answer the following questions:")
        participant_answers = []
        for q in questions :
            answer = input (q +" ").strip().lower()
            participant_answers.append(answer)
            all_responses.append(participant_answers)
            return all_responses
=======

    while True:
        user_input = input("\nWould you like to start the survey? (yes/no): ").strip().lower()
        if user_input == 'yes':
            response = ask_questions_to_user(questions)
            all_responses.append(response)
        elif user_input == 'no':
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

    if all_responses:
        summarize_results(all_responses, questions)
    else:
        print("No survey data to display.")

if __name__ == "__main__":
    main()

>>>>>>> fae3546950bfc253462c0f3848d0834eea6f235d
