f = open('one.txt', 'a')
lst = ['one \n', 'two \n', 'three \n']
f.write("Hello,Good Morning \n")
f.writelines(lst)
f.close()