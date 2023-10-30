print("Welcome to my quiz!")
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
else:
    print("Okay! Lets play :)")
    score = 0
    correct_answer = 0

answer = input("what does CPU stands for? ")
if answer.lower() == "control processing unit":
    print("Correct")
    score += 2
    correct_answer += 1
else:
    print("Incorrect!")

answer = input("what does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("Correct")
    score += 2
    correct_answer += 1
else:
    print("Incorrect!")

answer = input("what does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct")
    score += 2
    correct_answer += 1
else:
    print("Incorrect!")

answer = input("what does PSU stands for? ")
if answer.lower() == "power supply":
    print("Correct")
    score += 2
    correct_answer += 1
else:
    print("Incorrect!")

answer = input("father of computer? ")
if answer.lower() == "charles babbage":
    print("Correct")
    score += 2
    correct_answer += 1
else:
    print("Incorrect!")

print(f"You give {correct_answer} answers. ")
print(f"you score {score} marks. ")
print(f"you got {(score/10) *100}% marks")

