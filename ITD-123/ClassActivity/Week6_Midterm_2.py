score = int(input("Input Score : "))
if score >= 101:
    print("Error")
elif score >= 80:
    print("Excellent")
elif score >= 50:
    print("PASS")
elif score >= 40:
    print("PASS with condition")
elif score <= 40:
    print("Fail, Test Again")
# Test Case 10 45 52 90