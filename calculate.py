# calculate.py
def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

si = calculate_simple_interest(p, r, t)
print("Simple Interest is:", si)
