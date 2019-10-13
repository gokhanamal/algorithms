
#google interview question

given_array = [9, 9, 9, 9, 9, 9]


def add_one(arr):
    result = []
    weight = 1
    for index in range(len(arr)):
        reverse_index = (len(arr) - 1) - index

        number = arr[reverse_index] + weight

        if number >= 10:
            weight = 1
            if reverse_index == 0:
                result.insert(0, 0)
                result.insert(0, weight)
            else:
                result.insert(0, 0)
        else:
            weight = 0
            result.insert(0, number)
    return result


print(add_one(given_array))
# print [1,0,0,0,0,0,0]
