""" 
A: >80%
B: <80%, >=70%
C: <70%, >=60%
D: <60%, >=50%
E: <50%, >=40%
F: <40%
We also assume that four students have achieved the following scores:
Dave: 64%
Helen: 85%
Andy: 42%
Jane: 29%



Assign pupil scores:
dave_score
helen_score
andy_score
jane_score

write if elif else statements to assign grades to Dave

store 4 vars for students score in a list
add statement above the if elif else statement
 """

dave_score = 64
helen_score = 85
andy_score = 42
jane_score = 29

def GradeStudent(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"

StudentScores = [dave_score, helen_score, andy_score, jane_score]

for score in StudentScores:
    print(f"Student score: {score} Grade: {GradeStudent(score)}")

# Assume that jane resits her exam until she achieves a B grade... She performs 20% better each time she resits
# Replace for statement with while statement, loop until she achieves a B grade.
# Print janes score after the while loop has finished, how many resits does she need to get a B grade?

achievedB = False
iterations = 0
while not achievedB:
    jane_score *= 1.2
    iterations += 1
    if GradeStudent(jane_score) == "B":
        achievedB = True

print(f"Jane's score after {iterations} resits: {jane_score}")