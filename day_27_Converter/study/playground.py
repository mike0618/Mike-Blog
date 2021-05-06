def add(*args):
    # return sum(args)
    summ = 0
    for n in args:
        summ += n
    return summ


print(add(5, 3, 8))
