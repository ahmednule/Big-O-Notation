# Quadratic time, double

def has_duplicate(arr):
    for i in range(len(arr)):
        for j in range((i+1),len(arr)):
            if arr[i] == arr[j]:
                # return True
                return arr[i]
    # return False
    # return arr[j]
    return None

number=[12, 12, 13, 13]
# number=[12, 23, 32, 42, 55, 66, 77, 88, 99, 112, 223, 332, 442, 555, 666, 777, 888, 999,12, 23, 32, 42, 55, 66, 77, 88, 99, 112, 223, 332, 442, 555, 666, 777, 888, 999,12, 23, 32, 42, 55, 66, 77, 88, 99, 112, 223, 332, 442, 555, 666, 777, 888, 999,12, 23, 32, 42, 55, 66, 77, 88, 99, 112, 223, 332, 442, 555, 666, 777, 888, 999,]
result = has_duplicate(number)

print("Duplicate found:" if result else "No duplicates", result or "")