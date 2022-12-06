data = open('input.txt').read().splitlines()[0]
#data = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
# data = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
#data = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'

i = 0
while len(set(data[i:i+14])) != 14:
    i += 1
print(i+14)

#print([i+14 for i in range(len(data)) if len(set(data[i:i+14])) == 14][0])