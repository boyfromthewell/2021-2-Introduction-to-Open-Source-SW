'''
EX2) After taking two numbers, x and y, as inputs,
creating a function to calculate the multiplication of two inputs
- Using an input() function and function
'''

def mul(a,b):
    ans= a*b
    print(f'{a} X {b} = {ans}')

if __name__ == '__main__':
    x=int(input('x: '))
    y=int(input('y: '))
    mul(x,y)

'''
출력
x: 31
y: 38
31 X 38 = 1178
'''