from datetime import date
from utils import add, subtract, multiply, divide

print("Name: Istiaque Arif")
print(f"Date: {date.today().isoformat()}")
print(f"2 + 3 = {add(2, 3)}")
print(f"5 - 2 = {subtract(5, 2)}")
print(f"2 * 3 = {multiply(2, 3)}")
print(f"6 / 3 = {divide(6, 3)}")
