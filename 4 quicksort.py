def quick_sort(array):
  if len(array) < 2:
    return array
  else:
    pivot = array[0]

    less = [i for i in array[1:] if i <= pivot]

    greater = [i for i in array[1:] if i > pivot]
    
    return quick_sort(less) + [pivot] + quick_sort(greater)
  

my_arr = [1,3,6,734,7,98,2]

print(quick_sort(my_arr))
