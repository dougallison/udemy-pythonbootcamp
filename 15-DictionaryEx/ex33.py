# List to Dictionary Exercise

# Given a person variable:
# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# Create a dictionary called `answer`, that makes each first item
# in each list a key and the second item a corresponding value.
# Output should look like this:
# {'name': 'Jared', 'job': 'Musician', 'city': 'Bern'}

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# my solution
answer = {person[i][0]: person[i][1] for i in range(0, len(person))}
print(answer)

# alternate solution
answer = {p[0]: p[1] for p in person}
print(answer)

# alternate solution
answer = {k: v for k, v in person}
print(answer)

# if you have a list of pairs, it can be turned into a dictionary
# using dict()
answer = dict(person)
print(answer)
