def quick_sort(arr,start, end):

  if start < end:
    pi = partition(arr, start, end)

    quick_sort(arr, start, pi-1)
    quick_sort(arr, pi+1, end)

def partition(arr, start, end):
  follower = leader = start
  print(arr[start:end])
  while leader < end:
    print(arr)
    if arr[leader] <= arr[end]:
      arr[follower], arr[leader] = arr[leader], arr[follower]
      follower += 1
    leader += 1
  arr[follower], arr[end] = arr[end], arr[follower]
  return follower

alist = [6,1,7,2,4,9]
quick_sort(alist, 0, len(alist) - 1)
print(alist)