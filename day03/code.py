data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

def compartments(rucksack):
    n = len(rucksack)
    return rucksack[:n//2], rucksack[n//2:]

def common_item(compartments):
    c1 = set(compartments[0])
    c2 = set(compartments[1])
    return list(c1.intersection(c2))[0]

def priority(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27
    
#part1 = print(sum([priority(common_item(compartments(r))) for r in data]))
    
def common_item3(r1, r2, r3):
    s1 = set(r1)
    s2 = set(r2)
    s3 = set(r3)
    return list(s1.intersection(s2).intersection(s3))[0]

commons = [common_item3(data[k], data[k+1], data[k+2]) for k in range(0, len(data), 3)]
part2 = print(sum([priority(c) for c in commons]))
data = open('input.txt').readlines()