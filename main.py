from collections import Counter
def my_lower(text):
    my_text=text.lower().replace(" "," ")
    return dict(Counter(my_text))
usr_txt="Привет. Я Маша"
result=my_lower(usr_txt)
print(result)


def my_text(text):
    inrevers = text[::-1]
    my_str = inrevers.split()
    return " ".join(my_str)

my_txt = input("Введите текст: ")

result = my_text(my_txt)
print(result)

def duplicates(lst):
    return list(dict.fromkeys(lst))

my_list =[1, 2, 2, "Masha", "Olya", 4, "Masha"]
result=duplicates(my_list)

print("Исходник: ", my_list)
print("Нет дубликатов: ", result)

def unique(*lists):
    my_unique=set()

    for lst in lists:
        my_unique.update(lst)

    return list(my_unique)

list1=[1,2,3,4,"Masha"]
list2=[1,2,3,4,5,6,7,"Masha", "Olya", 1,2,99]

result=unique(list1,list2)
print(result)



def my_str(text):
    stat = {"гласные": 0, "согласные": 0, "цифры": 0, "пунктуация": 0}

    for char in text:
        char_lower = char.lower()

        if char_lower in "аеёиоуыэюя":
            stat["гласные"] += 1
        elif char_lower.isalpha():
            stat["согласные"] += 1
        elif char.isdigit():
            stat["цифры"] += 1
        elif not char.isalnum() and not char.isspace():
            stat["пунктуация"] += 1

    return stat


user_input = input("Введите текст: ")
result = my_str(user_input)

print("Результат: ")
for key, value in result.items():
    print(f"{key.capitalize()}: {value}")

