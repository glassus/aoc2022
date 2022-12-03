print(*(map(sum,zip(*[(ip+1+3*((ip-io+1)%3),ip*3+1+(io+ip-1)%3)
                      for c in map(str.split,open('input.txt')) if ((io := ord(c[0])-ord('A')),
              (ip := ord(c[1])-ord('X')))]))))

print(sum([ip+1+3*((ip-io+1)%3)
                      for c in map(str.split,open('input.txt')) if ((io := ord(c[0])-ord('A')),
              (ip := ord(c[1])-ord('X')))]))

print(sum([ip*3+1+(io+ip-1)%3
                      for c in map(str.split,open('input.txt')) if ((io := ord(c[0])-ord('A')),
              (ip := ord(c[1])-ord('X')))]))