#to take the list element as many i want then i won't  use use 
#the list to take input 
#instead i can take only map(int, input().split())
#if i want to take the some fixed element such as n then i have to use the following
#because [:n] this subscription doesn't work for map.

#map(the intended function, the iterator)

n = int(input())
arr =list(map(int, input().split()))[:n]
arr_new=set(arr)
arr_new.remove(max(arr_new))
print(max(arr_new))