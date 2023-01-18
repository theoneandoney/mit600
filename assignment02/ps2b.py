 # Problem Set 2 (Part I)
 # Name: Ryan Oney
 # Collaborators: N/A
 # Time: .5 hours

def diophantine(num):
    # Returns the number of solutions to the diophantine equation
    # 6a + 9b + 20c = num
    # where a, b, and c are non-negative integers
    sol_cnt = 0
    for a in range(num//6 + 1):
        for b in range(num//9 + 1):
            for c in range(num//20 + 1):
                if 6*a + 9*b + 20*c == num:
                    sol_cnt += 1
    return sol_cnt


def part_one():
    print("there are", diophantine(50), "possible ways to buy 50 chicken nuggets")
    print("there are", diophantine(51), "possible ways to buy 51 chicken nuggets")
    print("there are", diophantine(52), "possible ways to buy 52 chicken nuggets")
    print("there are", diophantine(53), "possible ways to buy 53 chicken nuggets")
    print("there are", diophantine(54), "possible ways to buy 54 chicken nuggets")
    print("there are", diophantine(55), "possible ways to buy 55 chicken nuggets")

part_one()

def part_three():
  n = 1
  cnt = 0
  save = []
  while cnt < 6:
    if diophantine(n) > 0:
      cnt += 1
      n += 1
    else:
      save.append(n)
      n += 1
      cnt = 0
  print("Largest number of McNuggets that cannot be bought in exact quantity:", save[-1])

part_three()

def diophantine2(num, packages):
    # Returns the number of solutions to the diophantine equation
    # x*a + y*b + z*c = num
    # where a, b, and c are non-negative integers
    x = packages[0]
    y = packages[1]
    z = packages[2]
    sol_cnt = 0
    for a in range(num//x + 1):
        for b in range(num//y + 1):
            for c in range(num//z + 1):
                if x*a + y*b + z*c == num:
                    sol_cnt += 1
    return sol_cnt


def part_4(x, y, z):
  bestSoFar = 0     # variable that keeps track of largest number
                    # of McNuggets that cannot be bought in exact quantity
  packages = (x, y, z)   # variable that contains package sizes

  for n in range(1, 200):   # only search for solutions up to size 150
      ## complete code here to find largest size that cannot be bought
      ## when done, your answer should be bound to bestSoFar
      if diophantine2(n, packages) == 0:
        bestSoFar = n
  print("Largest number of McNuggets that cannot be bought in exact quantity:", bestSoFar)


part_4(6, 9, 20)