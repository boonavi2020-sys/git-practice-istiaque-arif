from datetime import date
from utils import add, subtract

print("Name: Istiaque Arif")
print(f"Date: {date.today().isoformat()}")
print(f"2 + 3 = {add(2, 3)}")
print(f"5 - 2 = {subtract(5, 2)}")