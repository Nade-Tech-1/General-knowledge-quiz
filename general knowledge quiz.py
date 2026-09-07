print("Welcome To The General knowledge Quiz!")
score = 0

# question 1
answer = input("What is the capital of Nigeria?\nYour answer: ")
if answer.lower() == "abuja":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Abuja")


# question 2
answer = input("How many classes of food do we have?\nYour answer: ")
if answer.lower() == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 7")

# question 3
answer = input("What is the largest planet?\nYour answer: ")
if answer.lower() == "jupiter":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Jupiter")

print(f"\nYour final score is: {score} out of 3")
