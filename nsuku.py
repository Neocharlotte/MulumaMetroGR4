def summarize_results(responses, questions):
    summary = {question: {'yes': 0, 'no': 0} for question in questions}
    for response in responses:
        for question in questions:
            answer = response.get(question)
            if answer:
                summary[question][answer] += 1

    print("\nSurvey Results Summary:")
    for question, counts in summary.items():
        print(f"\n{question}")
        print(f"Yes: {counts['yes']} | No: {counts['no']}")