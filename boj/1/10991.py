#예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
n = int(input())
for i in range(n): print((" " * (n-i-1) + "* " * (i+1)).rstrip())
