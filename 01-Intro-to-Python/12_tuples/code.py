# short_tuple = "Ian", "James"
# a_bit_clearer = ("Ian", "James")
# not_a_tuple = "Ian"
# tuple_in_list = [("Ian", "James")]

friends = ("Ian", "James", "Sam")
# friends.append("Liam") #wrong

friends = friends + ("Liam") #wrong
friends = friends + ("Liam",)
print(friends)