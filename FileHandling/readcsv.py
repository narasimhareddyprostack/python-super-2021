import csv
f = open('test.csv', 'r')
data = csv.reader(f)

print(data)
for list1 in data:
    for word in list1:
        print(word, end='\t')

    print()


