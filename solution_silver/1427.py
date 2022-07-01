n = int(input())
 
a = []
for i in str(n):
    a.append(int(i))
    
a.sort(reverse = True)
 
for i in a:
    print(i , end ='')