art_friends = {"Ian", "James","Liam"}
science_friends = {"Liam", "Sam"}

art_but_not_friends = art_friends.difference(science_friends)
science_but_not_friends = science_friends.difference(art_friends)

print(art_but_not_friends)
print(science_but_not_friends)

not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)

art_and_science = art_friends.intersection(science_friends)
print(art_and_science)

all_friends = art_friends.union(science_friends)
print(all_friends)