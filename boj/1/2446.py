#예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
n = int(input())
for i in range(0,n):print(" " * i + "*" *(2 * (n-i)-1))
for j in range(2,n+1):print(" "*(n-j) + "*" * (2*(j)-1))