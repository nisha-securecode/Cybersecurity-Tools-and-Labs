password = input("enter password: ")
score = 0
feedback = []

if len(password) >= 8:
    score += 1
else:
    feedback.append("[-] password should be 8 characters long ")

if any(char.isdigit() for char in password):
    score += 1
else:
    feedback.append("[-] password should contain numbers")

if any(char.isupper() for char in password):
    score += 1
else:
    feedback.append("[-] password should contain uppercase")

special = "@#$%^!&*"

if any(char in special for char in password):
    score += 1
else:
    feedback.append("[-] password should contain special char")

print(f"\n password score: {score}/4")
if score == 4:
    print("[+] STRONG PASSWORD")
elif score >=2:
    print("[-] MEDIUM PASSWORD")
else:
    print("[-] WEAK PASSWORD")


if feedback:
    print(f"\n error:")
    for tip in feedback:
        print(tip)
