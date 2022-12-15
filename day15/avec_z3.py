import z3
import re

input_data= open('input.txt').read().splitlines()


def all_numbers(s):
    return [int(d) for d in re.findall("(-?\d+)", s)]


lines = [all_numbers(line) for line in input_data]

M = 4_000_000
x = z3.Int("x")
y = z3.Int("y")
solver = z3.Solver()
solver.add([x >= 0, x <= M, y >= 0, y <= M])

for line in lines:
    vals = line
    sensor = (vals[0], vals[1])
    beacon = (vals[2], vals[3])
    dist = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])
    hors_zone = z3.Or(x+y > sensor[0]+sensor[1]+dist,
                   x+y < sensor[0]+sensor[1]-dist,
                   y-x > sensor[1]-sensor[0]+dist,
                   y-x < sensor[1]-sensor[0]-dist)
    solver.add(hors_zone)

print(solver.check())
print(solver.model())