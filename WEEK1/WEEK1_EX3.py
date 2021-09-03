'''
Enter the number of lines and print them out in the following form
- Using an input() function and for loops
'''

n=int(input('Please enter the number : '))

for i in range(1, n+1):
    for j in range(i, n+1):
        print("*", end="") # end="" -> 파이썬은 기본적으로 출력할때 \n됨 (end=""하면 한줄에 여러개의 값 출력)
    print(" ")

'''
출력
Please enter the number : 5
***** 
**** 
*** 
** 
* 
'''