"""
This script demonstrates the use of the 'in' and 'not in' operators 
to check for inclusion and exclusion of substrings within a string
"""

announcement = "The winners of the prize are Chris, James, and Sam"

print("Chris" in announcement)
print("Steve" in announcement)
print("chris" in announcement)
print(" " in announcement)
print("," in announcement)

print()

print("Chris" not in announcement)
print("Steve" not in announcement)
print("chris" not in announcement)
print(" " not in announcement)
print("," not in announcement)