def words_check(text):
    words = text.split()
    result = {}

    for word in words:
        good_chars = ''
        for ch in word:
            if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
                good_chars += ch
        if len(good_chars) * 2 >= len(word):
            formatted = good_chars.capitalize()
            if formatted in result:
                result[formatted] += 1
            else:
                result[formatted] = 1

    return result

