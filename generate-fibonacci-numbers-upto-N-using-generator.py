def fib(n):
    p, q = 0, 1
    while(p < n):
        yield p
        p, q = q, p + q

print([num for num in fib(20)])
# OR
## iterating using __next__(), for Python2, use next()
# x.__next__()    # output => 0
# x.__next__()    # output => 1
# x.__next__()    # output => 1
# x.__next__()    # output => 2
# x.__next__()    # output => 3
# x.__next__()    # output => 5
# x.__next__()    # output => 8
# x.__next__()    # error

# It can be implemented by a simple list a well, by pushing items in a list instead of yielding
