def min_maximum_cost(n, k, cakes):
    left, right = 1, max(cakes)
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        required_groups = 1
        current_max = cakes[0]
        
        for i in range(1, n):
            if cakes[i] > mid:
                required_groups += 1
                current_max = cakes[i]
            else:
                current_max = max(current_max, cakes[i])
        
        if required_groups <= k:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer


# ورودی
n, k = map(int, input().split())
cakes = list(map(int, input().split()))


# خروجی
print(min_maximum_cost(n, k, cakes))





