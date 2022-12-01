data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

cal = []
somme = 0

for val in data:
    if val != '':
        somme += int(val)
    else:
        cal.append(somme)
        somme = 0

if val != '':
    cal.append(somme)

#part 1
print(max(cal))

#part 2
cal.sort()
print(cal[-1] + cal[-2] + cal[-3])