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

if answer.lower() == "a":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is: Central Processing Unit")

# PRINTING FINAL SCORE
print("\n---------------------------------")
print(f"Quiz Completed! Your total score is: {score}/3")

# Feedback
if score == 3:
    print("Excellent! 🎉")
elif score == 2:
    print("Good job! 👍 Keep improving.")
else:
    print("Don’t worry! Practice makes perfect 🙂")

