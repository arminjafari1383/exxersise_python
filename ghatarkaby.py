from collections import deque

def shortest_time(k, a, b):
    # اگر لیته از قبل در محل قرار باشد
    if a == b:
        return 0

    # صف BFS
    queue = deque([(a, 0)])  # (نقطه فعلی, زمان طی شده)
    visited = set()  # نقاط بازدید شده
    
    while queue:
        current, time = queue.popleft()
        
        # بازدید از نقطه فعلی
        if current in visited:
            continue
        visited.add(current)
        
        # بررسی مسیر نوع اول (x-1 و x+1)
        for neighbor in [current - 1, current + 1]:
            if neighbor == b:
                return time + 1
            if neighbor not in visited:
                queue.append((neighbor, time + 1))
        
        # بررسی مسیر نوع دوم (نزدیک‌ترین مضرب k)
        for neighbor in [current // k * k, (current // k + 1) * k]:
            if neighbor == b:
                return time + 1
            if neighbor not in visited:
                queue.append((neighbor, time + 1))

    return -1  # در صورتی که غیرممکن باشد (که طبق مسئله چنین حالتی وجود ندارد)

# ورودی
k, a, b = map(int, input("مقدار k، a و b را وارد کنید: ").split())

# محاسبه و چاپ جواب
print(shortest_time(k, a, b))
