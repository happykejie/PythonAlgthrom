# coding: utf-8

if __name__ == "__main__":

    n, k = list(map(lambda x: int(x), input().split()))

    arr = list(map(lambda x: int(x),input().split()))

    min_sum = sum(arr[:k])
    cur_sum = min_sum
    min_start = 0

    for i in range(1, n-k):
        cur_sum = cur_sum - arr[i-1] + arr[i+k-1]
        if cur_sum < min_sum:
            min_sum = cur_sum
            min_start = i

    print (min_start+1)
