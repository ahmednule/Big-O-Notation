# finding the maximum number in an array

def find_max(arr):
    max_value=arr[0]

    for num in arr:
        if num > max_value:
            max_value=num
    return max_value

number=[12, 23, 32, 42, 55, 66, 77, 88, 99, 112, 223, 332, 442, 555, 666, 777, 888, 999]
print("Max number is:", find_max(number))