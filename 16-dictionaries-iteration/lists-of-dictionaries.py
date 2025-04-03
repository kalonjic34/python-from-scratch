concert_attendees= [
    {"Name": "Sam", "section": 400, "price paid": 99.99},
    {"Name": "Ian", "section": 223, "price paid": 149.99},
    {"Name": "James", "section": 100, "price paid": 0.0},
]

for attended in concert_attendees:
    for key, value in attended.items():
        print(f"The {key} is {value}")