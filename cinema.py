films = {
    "Avengers Infinity Wars": [13,5],
    "Deadpool 2": [18,8],
    "Black Panther": [12,10],
    "Ready Player One": [8,20],
    "Thor Ragnarok": [12,7],
    "A Quiet Place": [18,15]
}

while True:
    choice = input("Please choose the film you want to watch: ").strip().title()
    if choice in films:
        age =int(input("How old are you?: ").strip())
        # Check the age
        if age >= films[choice][0]:
            # Check the number of tickets
            num_seats = films[choice][1]
            if films[choice][1] > 0:                
                print("Enjoy the film!")
                films[choice][1] = num_seats - 1
            else:
                print("There are no tickets left!")
        else:
            print("You're too young to watch the film!")
    else:
        print("We don't have that film...")