name = "Youssef"
age = 16
graduation = 2028
major = "Handasa"

print(f"Hello {name}!")
print(f"Major: {major}")

years_left = graduation - 2026
print(f"Left {years_left} years")

gpa = 95
if gpa >= 90:
    print(f"Your score {gpa}% - Excellent! Ready for KSA scholarship")
    print("InshaAllah Handasa scholarship in KSA!")
else:
    print("Keep working hard")

print("--- My Plan ---")
for i in range(1, years_left + 1):
    print(f"Year {i}: Study hard")

print("Good luck Saudi is waiting!")
