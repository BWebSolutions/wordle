

def get_ranked_words:
    with open('txt/isogram_values.txt','r') as f:
        lines = f.read().splitlines()

        for line in lines:
            x = line.split(":")
            words.append(x[0])

    with open('txt/non_isogram_values.txt','r') as f:
        lines = f.read().splitlines()

        for line in lines:
            x = line.split(":")
            words.append(x[0])

    return words