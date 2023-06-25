''' Break the door d with n hammers. Each time a hammer strikes door power (d) recudes by hammer power and that
hammer's power reduces by half. Attack so that door breaks in minimum no. of attacks. '''

# n = no. of hammer, d = door power, k = max no. of attacks
n, d, k = map(int, input().split())

# list with n hammer powers
m = [int(x) for x in input().split()[:n]]

attack = 0

while d >= 0:
    # reduce door power 
    d = d - max(m)
    
    # reduce hammer value to half and update list
    m[m.index(max(m))] = float(max(m) / 2)

    # count attacks
    attack += 1

# print attack
if attack <= k:
    print(attack)

# if attack exceeds 4
else:
    print("-1")