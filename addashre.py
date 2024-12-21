def calculate_stats(numbers):
  """
  محاسبه ماکزیمم، مینیمم و میانگین اعداد دریافتی

  Args:
    numbers: لیستی از اعداد

  Returns:
    tuple: شامل ماکزیمم، مینیمم و میانگین
  """

  return max(numbers), min(numbers), sum(numbers) / len(numbers)

if __name__ == "__main__":
  N = int(input())
  numbers = []
  for _ in range(N):
    numbers.append(float(input()))

  max_num, min_num, avg = calculate_stats(numbers)

  print(f"Max: {max_num:.3f}")
  print(f"Min: {min_num:.3f}")
  print(f"Avg: {avg:.3f}")

