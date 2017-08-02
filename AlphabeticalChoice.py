
names = [["Jenny", 0], ["Jerold", 0], ["Jean-Luc", 0], ["CJ", 0], ["Sarah", 0], ["Lee", 0], ["Chris", 0]]


def get_person_index(names, person):
    for i in xrange(len(names)):
        if names[i][0] == person:
            return i
    return len(names) + 1


def name_sort_key(item):
    return item[0]


def alphabetical_choice(names):
    # Check that names is not empty
    # Check that names is a 2D array with only two elements in each element
    ordered_names = sorted(names)
    first_person = ordered_names[0][0]
    min_food_num = ordered_names[0][1]
    for (person, food_num) in ordered_names:
        if food_num < min_food_num:
            names[get_person_index(names, person)][1] += 1
            return (names, person)
    names[get_person_index(names, first_person)][1] += 1
    return (names, first_person)


def test_alphabetical_choice(names, num):
    counter = 0
    print "Cycling %d times" % num
    print names
    while counter < num:
        (names, person) = alphabetical_choice(names)
        print names
        print person
        counter += 1

def display_person(names, person):
    print "Congratulations to %s you it is your turn to bring in food" % person
    print
    print "This will be your %dth time bringing in food" % names[get_person_index(names, person)][1]
    print

# test_alphabetical_choice(names, 34)
(names, person) = alphabetical_choice(names)
display_person(names, person)