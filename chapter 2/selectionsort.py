# getting the smallest number to insert to the array
def find_smallest(arr):
    smallest_value = arr[0]
    smallest_value_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest_value:
            smallest_value = arr[i]
            smallest_value_index = i
    return smallest_value_index

# inserting the smallest AKA Selection sort Algorithm
def selection_sort(arr):
    new_array = [] #the array which is going to include the sorted final output
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_array.append(arr.pop(smallest))
    return new_array

print(selection_sort([5,6,7,1,2,3,4]))