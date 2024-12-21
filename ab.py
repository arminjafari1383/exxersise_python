# def max_water_trapped(heights):
#     n = len(heights)
#     if n == 0:
#         return 0


#     left_max = [0] * n
#     right_max = [0] * n


#     # محاسبه بلندترین ارتفاع از سمت چپ برای هر ساختمان
#     left_max[0] = heights[0]
#     for i in range(1, n):
#         left_max[i] = max(left_max[i - 1], heights[i])


#     # محاسبه بلندترین ارتفاع از سمت راست برای هر ساختمان
#     right_max[n - 1] = heights[n - 1]
#     for i in range(n - 2, -1, -1):
#         right_max[i] = max(right_max[i + 1], heights[i])


#     # محاسبه آب جمع شده
#     total_water = 0
#     for i in range(n):
#         water_on_building = min(left_max[i], right_max[i]) - heights[i]
#         total_water += water_on_building


#     return total_water

def max_water_trapped(hegihts):
    n = len(hegihts)
    if n == 0:
        return 0
    left_max = [0] * n
    right_max = [0] * n
    left_max[0] = hegihts[0]
    for i in range(1,n):
        left_max[i] = max(left_max[i - 1],hegihts[i])
    right_max[n - 1] = hegihts[n - 1]
    for i in range(n - 2,-1,-1):
        right_max[i] = max(right_max[i + 1],hegihts[i])
    total_water = 0
    for i in range(n):
        water_on_building = min(left_max[i],right_max[i]) - hegihts[i]
        total_water += water_on_building
    return total_water