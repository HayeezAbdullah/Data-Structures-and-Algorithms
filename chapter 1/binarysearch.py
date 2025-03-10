# Binary Search

def binary_search(lst, item):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]  

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    
    return None  

# Testing
my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3)) 
