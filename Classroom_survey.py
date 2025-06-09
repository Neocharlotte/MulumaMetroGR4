questions = [
    "Do you like Python? (yes/no)",
    "Have you used input() before? (yes/no)",
    "Do you enjoy group projects? (yes/no)",
    "Would you like to learn more about dictionaries? (yes/no)",
    "Is programming fun for you? (yes/no)"
]

def collect_responses(questions, num_participants):
    all_responses = []
    for i in range (num_participants):
        print(f"\nParticipants {i + 1}, please answer the following questions:")
        participant_answers = []
        for q in questions :
            answer = input (q +" ").strip().lower()
            participant_answers.append(answer)
            all_responses.append(participant_answers)
            return all_responses