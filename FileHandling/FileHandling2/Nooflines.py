f = open('one.txt', 'r')
lc = 0
wc = 0
cc =0
for line in f:
    lc = lc+1
    word = line.split()
    wc = wc + len(word)
    cc = cc+len(line)



print(lc)
print(wc)
print(cc)