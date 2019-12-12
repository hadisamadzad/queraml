print(' '.join(filter(lambda x : int(x) % 3 == 0 and x.index(x) % 3 == 2, enumerate(input().split()))))
#