t1 = ("Jan","Feb",100, 200, 'Haha', 9.6)
t2 = (1,2,3,1.2,2.3,4.5,'a','b',True, False)

print(type(t1))

print(t1)

print(t1[3])

print(t2[2:6])

print(t1[1:])

print(t2 * 2)

print(t1 + t2)

#invalid - tuples are immutable
t1[2] = 6 