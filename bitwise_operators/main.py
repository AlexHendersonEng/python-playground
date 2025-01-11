# Define integers
a = 7 
b = 5

# Print binary values
print(f"a: {a:04b}") # 0111
print(f"b: {b:04b}") # 0101

# Print bitwise operation results
print(f"Variable a >> 2: {(a >> 2):04b}") # 0001
print(f"Variable a << 2: {((a << 2) & 0b1111):04b}") # 1100
print(f"Variable ~a: {(~a & 0b1111):04b}") # 1000
print(f"Variable a & b: {(a & b):04b}") # 0101
print(f"Variable a | b: {(a | b):04b}") # 0111
print(f"Variable a ^ b: {(a ^ b):04b}") # 0010