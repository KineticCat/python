def max_length_subarray(trees, k):
    n = len(trees)
    max_len = 0
    for i in range(n):
        curr_len = 1
        total_fruits = trees[i]
        j = i + 1

        while j < n:
            if total_fruits > k:
                break

            if trees[j] % trees[j - 1] == 0:
                curr_len += 1
                total_fruits += trees[j]
                j += 1
            else:
                break

        max_len = max(max_len, curr_len)

    return max_len

# Input the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    n, k = map(int, input().split())
    fruits = list(map(int, input().split()))
    heights = list(map(int, input().split()))
    result = max_length_subarray(heights, k)
    print(result)
