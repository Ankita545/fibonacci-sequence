fibonacci sequence
terms=int(input('Enter the no. of terms: '))
n1,n2=0,1
count=0
print('fibonacci sequence upto ', terms,'terms:')
if terms<1:        #checks if no. terms is valid
    print('enter positive no. of terms')
else:
    while count<terms:
        print(n1)   #prints the first term
        n=n1+n2     
        n1=n2       #swapping 
        n2=n
        count+=1
output:
Enter the no. of terms: 20
fibonacci sequence upto  20 terms:
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
