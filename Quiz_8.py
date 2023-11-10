import random

def lotto():
    number_list = []
    while len(number_list) < 6:
        number = random.randint(1, 45)
        if number not in number_list:
            number_list.append(number)
    print("생성된 로또 번호는 " + str(number_list) + "입니다.")
    return number_list
a = lotto()

print(a)
