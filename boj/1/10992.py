#예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
n = int(input())
if n == 1:
    print("*")
elif n == 2:
    print(" *")
    print("***")
else:
    print(" "*(n-1) + "*" )
    for i in range(2,n):
        print(" "*(n-i) +"*"+ " "*(2*i -3) +"*")
    print("*"*(2*n-1))