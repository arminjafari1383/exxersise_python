# n, m = map(int, input().split())
# direct_streets = list(map(int, input().split()))
# circle_streets = list(map(int, input().split()))

# # بررسی وجود هر دو جهت در خیابان‌های مستقیم
# has_outward = 1 in direct_streets
# has_inward = 0 in direct_streets

# # بررسی وجود هر دو جهت در خیابان‌های دایره‌ای
# has_clockwise = 1 in circle_streets
# has_counterclockwise = 0 in circle_streets

# # اگر همه شرایط برقرار باشد، جواب YES است
# if has_outward and has_inward and (has_clockwise or has_counterclockwise):
#     print("YES")
# else:
#     print("NO")

n,m = map(int,input().split())
direct_streets = list(map(int,input().split()))
circle_streets = list(map(int,input().split()))
has_outward = 1 in direct_streets
has_inward = 0 in direct_streets
has_clockwise = 1 in circle_streets
has_counterclockwise = 0 in circle_streets
if has_outward and has_inward and(has_clockwise or has_counterclockwise):
    print("YES")
else:
    print("NO")
