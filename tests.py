import datetime

class brithandzodiac():
    # 輸入出生日期
    birthday_str = input("請輸入您的出生日期（格式為YYYY-MM-DD）：")
    birthday = datetime.datetime.strptime(birthday_str, '%Y-%m-%d')

    # 檢查年份是否超過今年
    if birthday.year > datetime.datetime.now().year:
        print("輸入的年份不合法")
    else:
        month, day = birthday.month, birthday.day

        # 計算星座符號
        if month == 12 and day >= 22 or month == 1 and day <= 19:
            zodiac_sign = "摩羯座(Capricorn)"
        elif month == 1 and day >= 20 or month == 2 and day <= 18:
            zodiac_sign = "水瓶座(Aquarius)"
        elif month == 2 and day >= 19 or month == 3 and day <= 20:
            zodiac_sign = "雙鱼座(Pisces)"
        elif month == 3 and day >= 21 or month == 4 and day <= 19:
            zodiac_sign = "牡羊座(Aries)"
        elif month == 4 and day >= 20 or month == 5 and day <= 20:
            zodiac_sign = "金牛座(Taurus)"
        elif month == 5 and day >= 21 or month == 6 and day <= 21:
            zodiac_sign = "雙子座(Gemini)"
        elif month == 6 and day >= 22 or month == 7 and day <= 22:
            zodiac_sign = "巨蟹座(Cancer)"
        elif month == 7 and day >= 23 or month == 8 and day <= 22:
            zodiac_sign = "獅子座(Leo)"
        elif month == 8 and day >= 23 or month == 9 and day <= 22:
            zodiac_sign = "處女座(Virgo)"
        elif month == 9 and day >= 23 or month == 10 and day <= 22:
            zodiac_sign = "天秤座(Libra)"
        elif month == 10 and day >= 23 or month == 11 and day <= 21:
            zodiac_sign = "天蠍座(Scorpio)"
        elif month == 11 and day >= 22 or month == 12 and day <= 21:
            zodiac_sign = "射手座(Sagittarius)"
        
        # 計算年齡
        age = datetime.datetime.now().year - birthday.year

        # 顯示結果
        print("您的星座是：{}".format(zodiac_sign))
        print("您的年齡是：{} 歲".format(age))