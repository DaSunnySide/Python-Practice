west_coast = ['Oregon', 'Washington', 'California', 'Alaska']
print(west_coast)
for state in west_coast:
    print(state)
print(west_coast[1])
west_coast.append('Oregon')
print(west_coast.count('Oregon'))
print(west_coast)

opposite_corner = [ 'Florida', 'Georgia', 'South Carolina']
for state in west_coast:
    opposite_corner.append(state)
opposite_corner.append('North Carolina')
opposite_corner[1], opposite_corner[5] = opposite_corner[5], opposite_corner[1]
print(opposite_corner)

p = False
q = False

if(p and q):
    print('P and q are true')

else: print('Not p and q')

tv = [True, False ]

for p in tv:
    for q in tv:
        r = p and not q
        print(p,q,r)



