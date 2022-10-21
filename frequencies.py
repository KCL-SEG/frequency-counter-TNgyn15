"Frequencies function."
def frequencies(items):
    frequencies = {}
    for item in items:
        item = str(item)
        if item in frequencies:
            frequencies.update({item: frequencies.get(item) + 1})
        else:
            frequencies.update({item: 1})
    return frequencies
