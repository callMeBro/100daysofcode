def guess_quiz():
    #create question tuple
    questions = ("How many elements are in the periodic table?: ",
                 "Which animal lays the largest eggs?: ",
                 "What is the most abundant gas in Earth's atmosphere?: ",
                 "How many bones are in the human body?: ",
                 "Which planet in the solar system is the hottest?: ")
    #create option tuple
    options = (("A. 116", "B. 117", "C. 118", "D. 119"),
               ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
               ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
               ("A. 206", "B. 207", "C. 208", "D. 209"),
               ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

    #create answer tuple
    answers = ("C", "D", "A", "A", "B")
    guesses = []                #empty guest list 
    score = 0

    # loop through the question with corresponding index
    for i, question in enumerate(questions):
        print("----------------------")
        print(question)
        for option in options[i]:               #loop through options
            print(option)

        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)
        if guess == answers[i]:             #add guest to empty guest list 
            score += 1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f"{answers[i]} is the correct answer")

    print("----------------------")
    print("       RESULTS        ")
    print("----------------------")

    print("answers: ", " ".join(answers))
    print("guesses: ", " ".join(guesses))

    percentage_score = (score / len(questions)) * 100
    print(f"Your score is: {percentage_score:.2f}%")


def questions():
    print("TRUE OR FALSE: Reply with either T or F to indicate your answer.")

    # create dictionary with question and answers
    my_dict = {
        "q1": {"question": "Tuples are immutable", "answer": "T"},  
        "q2": {"question": "Tuples are an ordered sequence", "answer": "T"},
        "q3": {"question": "Strings can be a combination of spaces and digits", "answer": "F"},
        "q4": {"question": "When you perform division with a '/' operator even if the operands are integers and the result is a whole number it will be represented as a float", "answer": "T"},
        "q5": {"question": "Strings can do negative indexing", "answer": "F"},
        "q6": {"question": "You can iterate over the elements of a list using loops, such as for loops.", "answer": "T"}
    }

    correct_count = 0  

    for key, data in my_dict.items():
        question = data["question"]
        correct_answer = data["answer"]

        while True:
            user_input = input(question + ": ").upper()  

            if user_input == "T" or user_input == "F":
                if user_input == correct_answer:
                    print("Correct!")
                    correct_count += 1  
                else:
                    print("Incorrect.")
                break  
            else:
                print("Please enter T or F.")

    # Calculate the percentage 
    total_questions = len(my_dict)
    percentage_correct = (correct_count / total_questions) * 100

    print(f"You answered {correct_count} out of {total_questions} questions correctly.")
    print(f"Percentage correct: {percentage_correct:.2f}%")

questions()
