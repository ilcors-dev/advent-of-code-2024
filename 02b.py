# time complexity: O(n)  (ignoring initial data parsing from file)
# space complexity: O(1) (ignoring inputs)

import re

with open('02-input-data') as f:
    data = f.read()
    enabled = True

    res = 0
    
    i = 0
    while i < len(data): 
        if data[i:i + 7] == "don't()":
            print("disabling at i", i)
            enabled = False
            i += 7
            continue
        elif data[i:i + 4] == "do()":
            print("enabling at i", i)
            enabled = True
            i += 4
            continue

        if not enabled:
            i += 1
            continue

        if data[i] != "m":
            i += 1
            continue
        
        accumulated = ""

        while data[i] != ")":
            if data[i] == "m":
                accumulated = ""

            accumulated += data[i]
            i += 1

        accumulated += ")"

        if "don't()" in accumulated:
            enabled = False
            continue
        
        if re.search(r"mul\(\d+,\d+\)", accumulated):
            n1 = int(accumulated.split(",")[0].split("(")[1])
            n2 = int(accumulated.split(",")[1].split(")")[0])
            res += n1 * n2

        i += 1

    print(res)
