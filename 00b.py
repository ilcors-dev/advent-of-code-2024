# time complexity: O(n)  (ignoring initial data parsing from file)
# space complexity: O(n) (ignoring inputs)

def read_input():
    left, right = [], []
    with open('00-input-data') as f:
        for line in f:
            split_line = ' '.join(line.split()).split(' ')
            
            left.append(int(split_line[0]))
            right.append(int(split_line[1]))

    return left, right

def process():
    similarity_score = 0
    frequency = {}

    for n in left_list: # O(n)
        frequency[n] = 0

    for n in right_list: # O(n)
        if n in frequency:
            frequency[n] += 1

    for key, frequency in frequency.items(): # O(n)
        similarity_score += key * frequency

    return similarity_score

left_list, right_list = read_input()

print(process())
