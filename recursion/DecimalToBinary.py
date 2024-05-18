
def decToBin(n):
    assert int(n) == n, 'Value should be integer'
    if n == 0:
        return 0
    else:
        return n%2 + 10 * decToBin(int(n/2)) 


print(decToBin(12))