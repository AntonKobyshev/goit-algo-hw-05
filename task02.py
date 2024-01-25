def binary_search(array, target):
    iterations = 0
    left = 0
    right = len(array) - 1
    upper_bound = None  

    while left <= right:
        mid = (left + right) // 2
        iterations += 1

        if array[mid] == target:
            upper_bound = array[mid]
            break
        elif array[mid] < target:
            left = mid + 1
        else:
            upper_bound = array[mid]
            right = mid - 1

    if upper_bound is None:
        upper_bound = array[left] if left < len(array) else None

    return iterations, upper_bound

# Приклад використання функції
if __name__ == "__main__":
 
    sorted_array = [2.5, 3.8, 5.2, 7.1, 9.6, 11.0, 13.3]

    target = 8.0 # Значення, яке потрібно знайт

    iterations, upper_bound = binary_search(sorted_array, target)

    print(f"Кількість ітерацій: {iterations}")
    print(f"Верхня межа: {upper_bound}")
