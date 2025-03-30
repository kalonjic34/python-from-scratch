"""
This script demonstrates string slicing in Python using various examples
It showcases how to extract substrings by specifying start and end indices,
as well as using negative indices and omitting indices for flexibility
"""

address = "Adventures street, Beverly Hills, CA 90210"

print(address[0:3])
print(address[0:4])
print(address[0:17])
print(address[19:32])
print(address[10:100])

print("\n")

print(address[34:-6])
print(address[-8:-6])
print(address[-8:36])

print("\n")

print(address[5:])
print(address[13:])
print(address[-10:])

print(address[:10])
print(address[0:10])
print(address[0:23])
print(address[0:-3])

print(address[:])