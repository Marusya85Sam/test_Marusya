def my_calc(*args, operation="1"):
    if operation == "1":
        result = 0
        for number in args:
            result += number
        return result

    elif operation == "2":
        result = 1
        for number in args:
            result *= number
        return result

user_numbers = input("Введите числа через пробел: ")
numbers_list = [float(x) for x in user_numbers.split()]

print("Выберите операцию:")
print("1 — сложение")
print("2 — умножение")
user_op = input("Введите 1 или 2: ").strip()

final_result = my_calc(*numbers_list, operation=user_op)

print(f"Результат: {final_result}")

def get_integer():
    while True:
        user_input = input("Введите целое число: ")
        try:
            number = int(user_input)
            return number
        except ValueError:
            print("Ошибка! Вы ввели не целое число. Попробуйте снова.")

result = get_integer()
print(f"Верно: {result}")

def f_path(drive, *args, ext, sep="/"):
    file_name = args[-1]

    folders = args[:-1]

    if folders:
        path_without_ext = (
            drive + sep + sep.join(folders) + sep + file_name
        )
    else:
        path_without_ext = drive + sep + file_name

    return f"{path_without_ext}.{ext}"

result = f_path("c:", "work", "python", "function", "main", ext="py")
print(result)

result2 = f_path("d:", "photo", ext="png")
print(result2)

result3 = f_path(
    "d:", "movies", "comedy", "film", ext="mp4", sep="\\"
)
print(result3)



def group_by_type(input_list):
    result_dict = {}

    for item in input_list:
        type_name = type(item).__name__

        if type_name not in result_dict:
            result_dict[type_name] = []

        result_dict[type_name].append(item)

    return result_dict


my_list = [1, "привет", 777.77, True, "преподавателям", 42, [1, 2], (5, 6), 10]

result = group_by_type(my_list)
print("Результат:")
print(result)