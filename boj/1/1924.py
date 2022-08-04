#오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.
import datetime
days = ["MON","TUE","WED","THU","FRI","SAT","SUN"]# 파이썬은 monday가 첫번쨰 요일
month,day = map(int,input().split())
print(days[datetime.datetime(2007,month,day).weekday()])
