year = int(input("연도를 입력하세요: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year,"년은  윤년입니다.", sep="")
else:
    print(year,"년은 윤년이 아닙니다.", sep="")
