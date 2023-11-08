#!/usr/bin/end python3

import requests
import html
import random
import os

DEFAULT_URL = "https://opentdb.com/api.php?amount=10&category=15&difficulty=easy"


def handle_boolean(question_obj):
    question = html.unescape(question_obj["question"])
    print(f"True or False:\n{question}")
    user_guess = input("> ").strip().lower()

    if user_guess == question_obj["correct_answer"].lower():
        print("Correct!")
    else:
        print(f"incorrect, the answer is: {question_obj['correct_answer']}")

    print()


def handle_multiple_choice(question_obj):
    question = html.unescape(question_obj["question"])
    print(f"Multiple Choice:\n{question}")
    options = [question_obj["correct_answer"]]
    for incorrect in question_obj["incorrect_answers"]:
        options.append(incorrect)

    random.shuffle(options)

    for index, option in enumerate(options):
        print(f"{index + 1}. {option}")

    user_guess = input("> ").strip().lower()

    int_guess = -1
    if user_guess.isdigit():
        int_guess = int(user_guess)

    if (int_guess != -1 and options[int_guess - 1] == question_obj['correct_answer']) or\
        user_guess == question_obj["correct_answer"].lower():
        print("Correct!")
    else:
        print(f"incorrect, the answer is: {question_obj['correct_answer']}")

    print()


def main():
    os.system("clear")
    response = requests.get(DEFAULT_URL, timeout=10)
    response_json = response.json()

    if response_json["response_code"] == 0:
        questions = response_json["results"] # list of questions
    else:
        print(f"something went wrong: {response_json}")
        return

    for question in questions:
        match question["type"]:
            case "boolean":
                handle_boolean(question)
            case "multiple":
                handle_multiple_choice(question)


if __name__ == "__main__":
    main()
