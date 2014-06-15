pfx = ['c', 'a', 'e', 'h']
fo = [2, 2, 2, 0]
l = ["l1", "l2", "l3", ""]

def f1(x, y, z):
    return x, y, z

t = map(f1, pfx, fo, l)

print(t[0])
