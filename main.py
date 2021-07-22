arr = [1, 3, 56234, 123, 6, 63, 1, 3423, 6234, 4, 1, 4, 6, 234234, 12, 63, 22141, 345, 238, 34582, 34958, 1248, 3458, 1282]

for indx, elem in enumerate(arr):
  # setup intial holding variables
  element = arr[indx]
  count = indx

  # loop through our array
  while (count > 0 and arr[count - 1] > element):
    print(f"{count} is the current count")
    print(f"{element} is the current element")
    print(f"{arr[count-1]} is the current comparison element")

    # if true, run switch
    arr[count] = arr[count - 1]

    # checl for val at new elem place with updated count
    count = count - 1
  
  arr[count] = element

print(arr)