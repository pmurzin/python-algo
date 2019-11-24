from collections import deque

def bfs_mango(name):
  search_queue = deque()
  search_queue += graph[name]
  searched = []
  while search_queue:
    person = search_queue.popleft()
    if not person in searched:
      if person_is_seller(person):
        print(person, "is mango seller!")
        return True
      else:
        search_queue += graph[person]
        searched.append(person)
  return False

# name ends with ! means mango seller
def person_is_seller(name):
   return name[-1] == "!"


#my friends graph
graph = {}
graph["me"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom!", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom!"] = []
graph["jonny"] = []

#test
bfs_mango("me")