
# input함수를 사용해서 문구가 출력되도록 작성하는 식(int함수를 사용해서 문자를 숫자로 인지하게 바꿈)
a = int(input("몇 단까지 출력할까요?: "))
def group(A):
    for x in range(1, A+1):
        print("-------[" + str(x) + "단] -------")
        for y in range(1, A+1):
            print(x, "X", y, "=", x*y)
group(a)
