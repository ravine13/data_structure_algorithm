
def remove_duplicates(sequence):

    list = set()
    return [ x for x in sequence if not (x in list or list.add(x))]


input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result) 
