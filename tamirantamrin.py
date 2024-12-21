# n = int(input())
# for i in range(n):
#     print("man koshgalabam hastam")


#--------------------------------------


# n = int(input())
# for i in range(1,n + 1):
#     fact = fact * i
# print(fact)


#-------------------------------------

# def single_digit_sum(number):
#     while number >= 10:
#         digits = [int(digit) for digit in str(number)]
#         number = sum(digits)
#     return number
# input_number = int(input(""))
# result = single_digit_sum(input_number)
# print(f"{result}")


#--------------------------------------

# x = int(input(""))
# if x % 2 == 0:
#     print("Bala Barare")
# else:
#     print("payin Barare")

#--------------------------------------

# user_input = input("")
# for digit in user_input:
#     print(f"{digit}: " + digit * int (digit))

#---------------------------------------

# x = int(input(""))
# temp = 0
# for i in range(1,x):
#     if x % i == 0:
#         temp += i
# if temp == x:
#     print("YES")
# else:
#     print("NO")

#--------------------------------------

# n = int(input(" "))
# power_of_two = 1
# while power_of_two <= n:
#     power_of_two *= 2
# print(power_of_two)


#-------------------------------------

# numbers = []
# while True:
#     number = int(input(""))
#     if number == 0:
#         break
#     numbers.append(number)
# for number in reversed(numbers):
#     print(number)

#--------------------------------------

# n = int(input(""))
# print('*' * n)
# for i in range(n - 2):
#     print('*' + ' ' * (n - 2) +'*')
# if n > 1:
#     print("*" * n)

# ---------------------------------------

# x1,y1,x2,y2 = input(" ").split()
# if x1 == x2:
#     print("Vertical")
# elif y1 == y2:
#     print("Horizontal")
# else:
#     print("Try again")

#----------------------------------------

# def find_seat_direction_and_number(row,seat):
#     total_rows = 10
#     direction = "Right" if seat <= 10 else "Left"
#     row_from_top = total_rows - row + 1
#     seat_number = seat if direction == "Right" else 21 - seat
#     return direction,row_from_top,seat_number

# row_input,seat_input = map(int,input("").split())
# direction,row_from_top,seat_number = find_seat_direction_and_number(row_input,seat_input)
# print(f"{direction}{row_from_top}{seat_number}")

#----------------------------------------

# def calculate_final_garade(current_grade,travel_days):
#     if travel_days == 0:
#         return 20
#     elif travel_days == 7:
#         return current_grade
#     else:
#         final_grade = current_grade - travel_days
#         return max(final_grade,0)

# current_grade_input = int(input(""))
# travel_days_input = int(input(""))
# final_grade = calculate_final_garade(current_grade_input,travel_days_input)
# print(f"{final_grade}")

#----------------------------------------

# k = int(input().strip())
# total_time = k * (k + 1) // 2
# print(total_time)


#---------------------------------------

# num1 = input().strip()
# num2 = input().strip()
# rev_num1 = num1[::-1]
# rev_num2 = num2[::-1]
# if rev_num2 > rev_num1:
#     print(f"{num1} < {num2} ")
# elif rev_num1 > rev_num2:
#     print(f"{num1} > {num2}")
# else:
#     print(f"{num1} = {num2}")

#----------------------------------------

# date_string = input().strip()
# year = date_string[:2]
# month = date_string[2:]
# print(f"saal:{year}")
# print(f"maah:{month}")

#----------------------------------------

# m = int(input().strip())
# s_words = ["sib","senjed","samagh","serke","sonbal","sekkeh","samanoo"]
# for i in range(m):
#     print(s_words[i])

#---------------------------------------

# def find_free_days():
#     all_days = {"shanbe","1shanbe","2shanbe","3shanbe","4shanbe","5shanbe","jome"}
#     busy_days = set()
#     for _ in range(3):
#         num_days = int(input())
#         days = input().split()
#         busy_days.update(days)
#     free_days = all_days - busy_days
#     return len(free_days)
# print(find_free_days())

#----------------------------------------

# def count_mistakes(n,correct_word,written_word):
#     mistakes = 0
#     for i in range(n):
#         if correct_word[i] != written_word[i]:
#             mistakes += 1
#     return mistakes
# n = int(input())
# correct_word = input().strip()
# written_word = input().strip()
# print(count_mistakes(n,correct_word,written_word))

#----------------------------------------

# lower = int(input())
# upper = int(input())
# for num in range(lower,upper + 1):
#     if num > 1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)

#----------------------------------------

# n = int(input())
# words = input().split()
# reversed_words = words[::-1]
# print(" ".join(reversed_words))

#---------------------------------------

# def Table(bmi):
#     if bmi < 18.5:
#         print("Underwegiht")
#     elif 18.5 <= bmi <= 25:
#         print("Normal")
#     elif 25 <= bmi <= 30:
#         print("Overweight")
#     else:
#         print("Obses")

# def Bmi(weight,height):
#     b = weight // height ** 2
#     print(b)
#     t = Table(b)
#     print(t)

# a = Bmi(93,1.71)
# print(a)

#------------------------------------------

# n,k = map(int,input().split())
# for _ in range(k):
#     n //= 2
# print(n)

#-----------------------------------------

# lines = []
# for i in range(5):
#     lines.append(input().strip())
# indices = []
# for i in range(5):
#     if "MOLANA" in lines[i] or "HAFEZ" in lines[i]:
#         indices.append(i + 1)

# if indices:
#     print(" ".join(map(str,indices)))
# else:
#     print("NOT FOUND!")

#-----------------------------------------
#25
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2,int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#         return True
# def primes_in_ranage(a,b):
#     primes = []
#     for num in range(a + 1 , b):
#         if is_prime(num):
#             primes.append(num)
#     return primes
# a = int(input())
# b = int(input())
# primes_number = primes_in_ranage(a,b)
# print(','.join(map(str,primes_number)))

#-----------------------------------------
#26
# def find_last_watermelon(n,weights):
#     watermelons = list(range(1,n + 1))
#     while len(watermelons) > 1:
#         first,second = watermelons[0],watermelons[1]
#         if weights[first - 1] < weights[second - 1]:
#             watermelons.pop(0)
#         else:
#             watermelons.pop(1)
#     return watermelons[0]
# n = int(input(""))
# weights = list(map(int,input("").split()))
# last_watermelon = find_last_watermelon(n,weights)
# print(last_watermelon)

#----------------------------------------
#27
# def genrate_pascals_triangle(n):
#     triangle = []
#     for i in range(n):
#         row = [1] * (i + 1)
#         for j in range(1,i):
#             row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
#         triangle.append(row)
#     return triangle
# def print_pascals_triangle(triangle):
#     for row in triangle:
#         print(' '.join(map(str,row)))

# n = int(input(""))
# triangle = genrate_pascals_triangle(n)
# print_pascals_triangle(triangle)

#---------------------------------------
#28
# def count_unique_characters(s):
#     return len(set(s))
# n = int(input(""))
# names = [input("") for _ in range(n)]
# max_unique_count = 0
# for name in names:
#     unique_count = count_unique_characters(name)
#     if unique_count > max_unique_count:
#         max_unique_count = unique_count
# print(max_unique_count)

#----------------------------------------
#29
# def find_fourth_vertex(coords):
#     x_coords = [coords[0][0],coords[1][0],coords[2][0]]
#     y_coords = [coords[0][1],coords[1][1],coords[2][1]]
#     if x_coords.count(x_coords[0]) == 1:
#         x4 = x_coords[0]
#     elif x_coords.count(x_coords[1]) == 1:
#         x4 = x_coords[1]
#     else:
#         x4 = x_coords[2]
#     if y_coords.count(y_coords[0]) == 1:
#         y4 = y_coords[0]
#     elif y_coords.count(y_coords[1]) == 1:
#         y4 = y_coords[1]
#     else:
#         y4 = y_coords[2]

#     return x4,y4 

#------------------------------------------
#30
# def print_diamond(n):
#     for i in range(n + 1):
#         for j in range(n - i):
#             print(" ",end = "")
#         for j in range(2 * i + 1):
#             print("*",end = "")
#         print()
#     for i in range(n - 1, -1, -1):
#         for j in range(n - i):
#             print(" ",end = "")
#         for j in range(2 * i + 1):
#             print("*",end = "")
#         print()
# n = int(input(""))
# print_diamond(n)

#-------------------------------------------
#31
# a1 = int(input())
# b1 = int(input())
# a2 = int(input())
# b2 = int(input())
# a3 = int(input())
# b3 = int(input())
# teams_city1 = min(a1,b1)
# teams_city2 = min(a2,b2)
# teams_city3 = min(a3,b3)
# total_teams = teams_city1 + teams_city2 + teams_city3
# print(total_teams)

#------------------------------------------
#32
# n,k = map(int,input().split())
# capacities = [int(input()) for _ in range(n)]
# total_capacity = sum(capacities)
# if total_capacity >= k:
#     print("YES")
# else:
#     print("NO")

#-----------------------------------------
#33
# def solven(n, x, y):
#     def extended_gcd(a,b):
#         if b == 0:
#             return a,1,0
#         g,x1,y1  = extended_gcd(b,a % b)
#         x = y1
#         y = x1 - (a // b) * y1
#         return g,x,y
#     g , a , b = extended_gcd(x,y)
#     if n % g != 0:
#         return -1
#     a *= n // g
#     b *= n // g
#     k = -a // (y // g)
#     a += k *(y // g)
#     b -= k * (x //g)
#     if a < 0:
#         a += y // g
#         b -= x // g
#     if a < 0 or b < 0:
#         return -1
#     return a,b
# n , x , y = map(int,input().split())
# result = solven(n,x,y)
# if result == -1:
#     print(-1)
# else:
#     print(result[0],result[1])

#-----------------------------------------