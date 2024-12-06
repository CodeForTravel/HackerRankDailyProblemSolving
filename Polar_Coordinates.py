import cmath

# Read the input complex number
z = complex(input().strip())  # Example input: 1+2j

# Compute the polar coordinates
r = abs(z)  # Modulus (magnitude)
theta = cmath.phase(z)  # Phase (angle in radians)

# Print the results
print(r)
print(theta)
