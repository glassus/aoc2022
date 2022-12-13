data = open('input.txt').read().splitlines()
data = open('input_test.txt').read().splitlines()

class Monkey:
    def __init__(self, number, items, op, test, to_true, to_false):
        self.number = number
        self.items = items
        self.op = op
        self.test = test
        self.to_true = to_true
        self.to_false = to_false
        self.activity = 0
        #self.val = None
        
    
    def action(self, item):
        self.activity += 1
        self.items.remove(item)
        item.append(self.number)
        #new_val = self.calcul(item)
        #print(item[0],new_val)
        #self.val = new_val
        if self.calcul(item) % self.test == 0:
            monkey[self.to_true].items.append(item)
        else:
            monkey[self.to_false].items.append(item)
            
    def calcul(self, item):
        level = item[0]
        for i in range(1, len(item)):
            level = monkey[item[i]].op(level)
            #level = level // 3
        return level
    
    def own_round(self):
        lst = list(self.items)
        for item in lst:
            #print(f"action sur {item}")
            self.action(item)



            
monkey = [None]*8
#input de test
monkey[0] = Monkey(0,
                   [[79], [98]],
                   lambda x : x * 19,
                   23,
                   2,3)

monkey[1] = Monkey(1,
                   [[54], [65], [75], [74]],
                   lambda x : x + 6,
                   19,
                   2,0)

monkey[2] = Monkey(2,
                   [[79], [60], [97]],
                   lambda x : x * x,
                   13,
                   1,3)

monkey[3] = Monkey(3,
                   [[74]],
                   lambda x : x + 3,
                   17,
                   0,1)

vrai_input = False
if vrai_input:
    monkey[0] = Monkey(0,
                       [[65], [78]],
                       lambda x : x*3,
                       5,
                       2,3)

    monkey[1] = Monkey(1,
                       [[54],[78],[86],[79],[73],[64],[85],[88]],
                       lambda x : x+8,
                       11,
                       4,7)

    monkey[2] = Monkey(2,
                       [[69],[97],[77],[88],[87] ],
                       lambda x : x+2,
                       2,
                       5,3)

    monkey[3] = Monkey(3,
                       [[99]],
                       lambda x :  x+4,
                       13,
                       1,5)

    monkey[4] = Monkey(4,
                       [[60],[57],[52]],
                       lambda x : x*19,
                       7,
                       7,6)

    monkey[5] = Monkey(5,
                       [[91],[82],[85],[73],[84],[53]],
                       lambda x : x+5 ,
                       3,
                       4,1)

    monkey[6] = Monkey(6,
                       [[88],[74],[68],[56]],
                       lambda x : x*x,
                       17,
                       0,2)

    monkey[7] = Monkey(7,
                       [[54],[82],[72],[71],[53],[99],[67] ],
                       lambda x : x+1,
                       19,
                       6,0)


def round():
    for monk in monkey:
        if monk is not None:
            monk.own_round()

def go(n):
    for _ in range(n):
        #print(_)
        round()

def print_test():
    for i in range(len(monkey)):
        if monkey[i] is not None:
            print(i, monkey[i].activity)
            #print(i, [monkey[i].calcul(item) for item in monkey[i].items])
            print(i, monkey[i].items)

def max_activity():
    act = [monk.activity for monk in monkey if monk is not None]
    act.sort()
    print(act)
    print(act[-1] * act[-2])
    


n = 20
go(n)
print_test()
max_activity()
