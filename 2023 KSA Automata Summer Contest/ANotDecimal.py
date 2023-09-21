x = float(input())

# Initialize variables for the smallest solution
smallest_y = None
smallest_z = None

z = 1
while True:
    # Calculate the corresponding y value
    y = x * z
    
    # Check if y is an integer and both y and z are non-negative
    if y.is_integer() and y >= 0 and z >= 0:
        smallest_y = int(y)
        smallest_z = z
        break  # Found the smallest valid solution
    
    # Increment z for the next iteration
    z += 1

# Print the smallest solution
if smallest_y is not None and smallest_z is not None:
    print(f"YES")
    print(f"{smallest_y} {smallest_z}")
else:
    print(f"NO")
    