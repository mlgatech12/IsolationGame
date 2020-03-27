#import operators
a = {3:3000, 4:4000, 1: 10000}
b = [1,2,3,4,5]

#sorted(a.items(), key=itemgetter(1)

print(max(a, key=lambda k: a[k]))
