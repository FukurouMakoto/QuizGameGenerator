import json


def open_json(subject):
    with open('questions.json', 'r') as f:
        questions = json.load(f)
        filtered_questions = []
        for i in range(0, len(questions)):
            if questions[i]['subject'] == subject:
                filtered_questions.append(questions[i])

    return filtered_questions


def print_question(question, num):
    print(question[num]['question'])
    print(f"a: {question[num]['a']}")
    print(f"b: {question[num]['b']}")
    print(f"c: {question[num]['c']}")
    print(f"d: {question[num]['d']}")


def choose_subject():
    subjects = ['Literature', 'Science', 'History', 'Geography', 'Hololive']
    for i in range(0, len(subjects)):
        print(f"{subjects[i]}")
    print("Please choose a subject")
    subject = input("")
    if subject not in subjects:
        print("Please choose one of the subjects above")
        choose_subject()
    return subject


def main():
    questions = open_json(choose_subject())
    correct = 0
    incorrect = 0
    current_idx = 0

    while current_idx < len(questions):
        print_question(questions, current_idx)
        answer = input("").lower()
        if answer not in ['a', 'b', 'c', 'd']:
            print("Please choose either 'a', 'b', 'c', or 'd'")
            answer = input("")
        if answer == questions[current_idx]['correct answer']:
            print("Correct!\n")
            correct += 1
        else:
            print("Incorrect!\n")
            incorrect += 1

        current_idx += 1
    print(f"Correct answers: {correct}")
    print(f"Incorrect answers: {incorrect}")


if __name__ == '__main__':
    main()
