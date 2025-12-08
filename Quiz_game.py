# -------------------------------
#   TEXT-BASED QUIZ GAME
# -------------------------------

print("Welcome to the Python Quiz Game!")
print("---------------------------------")

score = 0  # To count correct answers

# QUESTION 1
print("\n1. What is the capital of Germany?")
print("a) Berlin")
print("b) Munich")
print("c) Frankfurt")
answer = input("Your answer (a/b/c): ")

if answer.lower() == "a":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is: Berlin")

# QUESTION 2
print("\n2. Which number is EVEN?")
print("a) 13")
print("b) 6")
print("c) 21")
answer = input("Your answer (a/b/c): ")

if answer.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is: 6")

# QUESTION 3
print("\n3. What does CPU stand for?")
print("a) Central Processing Unit")
print("b) Central Power Unit")
print("c) Computer Processing Utility")
answer = input("Your answer (a/b/c): ")
# QUESTION 4 (NEW QUESTION ADDED)
print("\n4. Which programming language is known for data science?")
print("a) Python")
print("b) HTML")
print("c) CSS")
answer = input("Your answer (a/b/c): ")

if answer.lower() == "a":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is: Python")
if answer.lower() == "a":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is: Central Processing Unit")

# QUESTION 5 (NEW QUESTION ADDED)
print("\n5. Which device is used to store long-term data?")
print("a) RAM")
print("b) Hard Drive")
print("c) CPU")
answer = input("Your answer (a/b/c): ")

if answer.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is: Hard Drive")
if answer.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is: Hard Drive")

    # QUESTION 6
    print("\n6. Which planet is known as the Red Planet?")
    print("a) Venus")
    print("b) Mars")
    print("c) Jupiter")
    answer = input("Your answer (a/b/c): ")

    if answer.lower() == "b":
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is: Mars")

# QUESTION 7 (NEW QUESTION ADDED)
print("\n7. In Python, which keyword is used to begin an 'if' conditional statement?")
print("a) if")
print("b) else")
print("c) for")
answer = input("Your answer (a/b/c): ")

if answer.lower() == "a":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is: if")

# PRINTING FINAL SCORE
print("\n---------------------------------")
print(f"Quiz Completed! Your total score is: {score}/7")

# Feedback
if score == 7:
    print("Excellent! 🎉")
elif score >= 4:
    print("Good job! 👍 Keep improving.")
else:
    print("Don’t worry! Practice makes perfect 🙂")
