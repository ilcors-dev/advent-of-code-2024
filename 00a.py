# time complexity: O(nlogn) (ignoring initial data parsing from file)
# space complexity: O(1) (ignoring inputs)

def read_input():
    left, right = [], []
    with open('00-input-data') as f:
        for line in f:
            split_line = ' '.join(line.split()).split(' ')
            
            left.append(int(split_line[0]))
            right.append(int(split_line[1]))

    return left, right

def process():
    sum = 0

    for i in range(len(left_list)):
        sum += abs(left_list[i] - right_list[i])

    return sum

left_list, right_list = read_input()

left_list = sorted(left_list) # O(nlogn)
right_list = sorted(right_list) # O(nlogn)

print(process())
