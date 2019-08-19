# coding: utf-8

n = input()

arr = list(map(lambda x: int(x), raw_input().split()))

min_index = 0
min_value = float('INF')

salary = [0]*n  # 保存薪水

for index, val in enumerate(arr):  # 找到最小下标
    if val < min_value:
        min_index = index
        min_value = val

salary[min_index] = 100  # 最小资质100快

left = min_index-1  # 向左边扩展
right = min_index+1  # 向右边扩展

while left >= 0:
    if arr[left] < arr[left+1]:
        salary[left] = 100  # 如何处理
    elif arr[left] == arr[left+1]:
        salary[left] = salary[left+1]
    elif arr[left] > arr[left+1]:
        salary[left] = salary[left+1]+100
    left -= 1

while right < n:
    if arr[right] < arr[right-1]:
        salary[right] = 100
    elif arr[right] == arr[right-1]:
        salary[right] = salary[right-1]
    elif arr[right] > arr[right-1]:
        salary[right] = salary[right-1]+100
    right += 1


print sum(salary)