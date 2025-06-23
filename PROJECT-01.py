#importing necessary utilities
import random

quiz_app = {
    "What keyword is used to define a function in Python?": "def",
    "What symbol is used to comment a line in Python?": "#",
    "Which data type is used to store text?": "str",
    "What is the output type of input() function?": "str",
    "Which keyword is used to create a loop?": "for",
    "What is used to store multiple items in a single variable?": "list",
    "Which keyword is used for a conditional statement?": "if",
    "How do you start a Python class?": "class",
    "Which keyword is used to import modules?": "import",
    "What do you use to handle errors?": "try",
    "Which loop runs while a condition is true?": "while",
    "How do you end a function and return a value?": "return",
    "What is the value of None type?": "None",
    "Which operator is used for exponentiation?": "**",
    "How do you create a comment?": "#",
    "Which data type is used to store True or False?": "bool",
    "How do you get the length of a list?": "len",
    "What do you call a block of reusable code?": "function",
    "What is the keyword to define a constant variable in Python?": "None",
    "What file extension is used for Python files?": ".py"
}

def python_quizz():
    questions = list(quiz_app.keys())
    total_questions = 5
    score = 0

    generate = random.sample(questions,total_questions)
    
    for idx,quest in enumerate(generate):
        print(f"{idx+1}.{quest}")
        user = input("Enter the answer : ").lower().strip()
        correct_answer = quiz_app[quest]

        if user == correct_answer:
            print(f"COOL ANSWER IS CORRECT {user}")
            score = score+1
        else:
            print(f"ANSWER IS WRONG... BUT RIGHT ANSWER IS {correct_answer}")
    
    print(f"FINAL SCORE {score}/{total_questions}!")
python_quizz()