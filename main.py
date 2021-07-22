'''
https://www.geeksforgeeks.org/merge-sort/
'''

# arr = [1, 3, 56234, 123, 6, 63, 1, 3423, 6234, 4, 1, 4, 6, 234234, 12, 63, 22141, 345, 238, 34582, 34958, 1248, 3458, 1282]

# for indx, elem in enumerate(arr):
#   # setup intial holding variables
#   element = arr[indx]
#   count = indx

#   # loop through our array
#   while (count > 0 and arr[count - 1] > element):
#     print(f"{count} is the current count")
#     print(f"{element} is the current element")
#     print(f"{arr[count-1]} is the current comparison element")

#     # if true, run switch
#     arr[count] = arr[count - 1]

#     # checl for val at new elem place with updated count
#     count = count - 1
  
#   arr[count] = element

# print(arr)

arr2 = [234, 51, 123, 5, 12, 5, 8, 12312, 6, 1231]

def merge_sort(arr):
    # check to make sure list has elements to sort
    if len(arr) > 1:

        # get middle of list
        middle = len(arr) // 2
        #divide up our list into segments
        left_side = arr[:middle]
        right_side = arr[middle:]

        # RECURSE
        merge_sort(left_side)
        merge_sort(right_side)

        # count for both sides
        left_count = 0
        right_count = 0

        # count for our end list
        main_count = 0

        # while loop to check for segment size and run if segment not sorted
        while left_count < len(left_side) and right_count < len(right_side):
            if left_side[left_count] <= right_side[right_count]:
                arr[main_count] = left_side[left_count]
                left_count += 1
            else:
                arr[main_count] = right_side[right_count]
                right_count += 1
            
            # once check has run, increment main count
            main_count += 1

        # check for final vals on left side
        while left_count < len(left_side):
            arr[main_count] = left_side[left_count]
            left_count += 1
            main_count += 1

        # check for final vals on right side
        while right_count < len(right_side):
            arr[main_count] = right_side[right_count]
            right_count += 1
            main_count += 1

def print_list(arr):
    merge_sort(arr)
    return arr

print(print_list(arr2))