from collections import deque

def shortest_path(a, b, k):
  """
  پیدا کردن کوتاه‌ترین مسیر بین دو نقطه در گراف قطار

  Args:
    a: نقطه شروع
    b: نقطه مقصد
    k: ضریب فاصله در نوع دوم قطارها

  Returns:
    int: طول کوتاه‌ترین مسیر یا -1 اگر مسیری وجود نداشته باشد
  """

  # ایجاد گراف با استفاده از مجموعه برای جلوگیری از تکرار همسایه‌ها
  graph = {x: set([x+1, x-1, k*x, k*(x+1)]) for x in range(a, b+1)}

  # BFS
  queue = deque([(a, 0)])  # (نقطه، فاصله)
  visited = set()
  while queue:
    node, distance = queue.popleft()
    if node == b:
      return distance
    if node not in visited:
      visited.add(node)
      for neighbor in graph[node]:
        if a <= neighbor <= b:  # بررسی محدوده مجاز برای همسایه‌ها
          queue.append((neighbor, distance+1))

  return -1  # اگر مسیری وجود نداشته باشد

# گرفتن ورودی
a, b, k = map(int, input().split())

# محاسبه و چاپ جواب
result = shortest_path(a, b, k)
print(result)