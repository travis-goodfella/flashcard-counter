def main():
    total_questions = 0
    correct_answers = 0
    wrong_answers = 0
    
    while True:
        print("Question", total_questions + 1)
        answer = input("Right or Wrong? Type 'exit' to quit: ")
        
        if answer.lower() == "exit":
            break
        
        total_questions += 1
        
        # Simulating some condition for correctness, you can replace this with your logic
        if answer.lower() == "right":
            print("Correct!")
            correct_answers += 1
        else:
            print("Incorrect!")
            wrong_answers += 1
        
        print("Total questions:", total_questions)
        print("Correct answers:", correct_answers)
        print("Wrong answers:", wrong_answers)
        print("Percentage correct:", (correct_answers / total_questions) * 100 if total_questions > 0 else 0, "%")
        print()
        
    print("Final Results")
    print("Total questions:", total_questions)
    print("Correct answers:", correct_answers)
    print("Wrong answers:", wrong_answers)
    print("Percentage correct:", (correct_answers / total_questions) * 100 if total_questions > 0 else 0, "%")
    input("Press enter to exit program")
    
if __name__ == "__main__":
    main()
