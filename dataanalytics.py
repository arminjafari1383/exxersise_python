# خواندن ورودی
string_to_find = input().strip()
sentence = input().strip()

# بررسی وجود رشته در جمله
if string_to_find in sentence:
    print(1)
else:
    print(0)

