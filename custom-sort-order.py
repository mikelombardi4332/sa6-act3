#Given a list of strings, use a lambda function to sort the list in ascending order based on the length of the strings. In case of a tie, sort the strings alphabetically

ls1 = [("Random words"),("More other words"),("Some other words too"),("aab"),("baa"),("bba")]

sorter = lambda x: sorted(x)

print(sorter(ls1))