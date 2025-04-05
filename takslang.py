def translate_taxlang(lines):
    # تعریف دیکشنری بلوک‌ها
    blocks = {
        "*****oo*oooo*oo": "T",
        "oo*ooo***ooo*oo": "A",
        "*ooo*oo*oo*ooo*": "X",
        "**o***o*o**ooo*": "M",
        "*ooo**o*o*ooo*": "N"
    }
    
    # طول هر بلوک
    block_width = 5
    num_blocks = len(lines[0]) // block_width  # تعداد بلوک‌ها در هر خط
    
    # استخراج بلوک‌ها و ترجمه
    result = []
    for i in range(num_blocks):
        # استخراج هر بلوک از خطوط
        block = (
            lines[0][i*block_width:(i+1)*block_width] +
            lines[1][i*block_width:(i+1)*block_width] +
            lines[2][i*block_width:(i+1)*block_width]
        )
        # اضافه کردن ترجمه بلوک به نتیجه
        result.append(blocks[block])
    
    return "".join(result)

# دریافت ورودی
lines = [input().strip() for _ in range(3)]
# ترجمه و چاپ نتیجه
print(translate_taxlang(lines))






















