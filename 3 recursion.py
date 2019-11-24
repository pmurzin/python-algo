my_list = [1,3,6,734,7,98,2]

def sum(list):
  if list == []:
    return 0
  return list[0] + sum(list[1:])

print("sum of my_list is ", sum(my_list))

def count(list):
  if list == []:
    return 0
  return 1 + count(list[1:])

print("size of my_list is ", count(my_list))


def find_max(list):
  if len(list) == 2:
    return list[0] if list[0] > list[1] else list[1]
  submax = find_max(list[1:])
  return list[0] if list[0] > submax else submax

print("max of my_list is ", find_max(my_list))