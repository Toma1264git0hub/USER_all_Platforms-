import random
import requests
import os
import time
import datetime
import sys


end_date = datetime.datetime(2025, 5, 20)


today = datetime.datetime.now()

if today >= end_date:
    print("انتهت صلاحية الأداة. تواصل مع المطور للاشتراك : https://t.me/K_DKP.")
    sys.exit()

# كود الأداة هنا
print("تاريخ الانتهاء 20/5/2025")
GREEN = '\033[92m'
RED = '\033[91m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
MAGENTA = '\033[95m'
RESET = '\033[0m'

platforms = {
    "TIKTOK": "https://www.tiktok.com/@{}",
    "FACEBOOK": "https://www.facebook.com/{}",
    "INSTAGRAM": "https://www.instagram.com/{}",
    "TELEGRAM": "https://t.me/{}",
    "GITHUB": "https://github.com/{}",
    "DISCORD": "https://discord.com/users/{}",
    "SNAPCHAT": "https://www.snapchat.com/add/{}",
    "TWITTER": "https://twitter.com/{}",
    "REDDIT": "https://www.reddit.com/user/{}",
    "YOUTUBE": "https://www.youtube.com/{}",
    "PINTEREST": "https://www.pinterest.com/{}",
    "LINKEDIN": "https://www.linkedin.com/in/{}"
}

status = {platform: {'hit': 0, 'bad': 0} for platform in platforms}

def generate_username(type_id):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    all_chars = letters + digits

    if type_id == 1:
        # اليوزر الأول: 4 أحرف وأرقام بولد (uppercase)
        return ''.join(random.choices(all_chars, k=4)).upper()

    elif type_id == 2:
        # اليوزر الثاني: مكرر أول حرفين
        base = ''.join(random.choices(all_chars, k=2))
        return base + base

    elif type_id == 3:
        # اليوزر الثالث: 3 أحرف وأرقام عشوائية
        return ''.join(random.choices(all_chars, k=3))

    elif type_id == 4:
        # اليوزر الرابع: 4 أحرف وأرقام عشوائية
        return ''.join(random.choices(all_chars, k=4))

    elif type_id == 5:
        # اليوزر الخامس: 5 أحرف مكون من أول حرفين مكرر + حرف + رقم
        first_two = ''.join(random.choices(all_chars, k=2))
        third = random.choice(all_chars)
        fourth = random.choice(digits)
        return first_two + first_two + third + fourth  # لكن هذا يعطي 6 أحرف
        # تعديل: لتكون 5 أحرف، نعتمد أول حرفين مكرر + حرف + رقم
        # نعيد كتابتها هكذا:
        # return first_two + first_two[0] + third + fourth

    elif type_id == 6:
        # اليوزر السادس: 6 أحرف، أول 3 أحرف مكررة + 3 عشوائية
        first_three = ''.join(random.choices(all_chars, k=3))
        last_three = ''.join(random.choices(all_chars, k=3))
        return first_three + first_three + last_three  # هذا يعطينا 9 أحرف!
        # تعديل: مطلوب 6 أحرف = أول 3 مكررة (يعني 3 أحرف) + 3 عشوائية
        # أي أول 3 أحرف مكررة مرة واحدة فقط
        return first_three + last_three

    elif type_id == 7:
        # اليوزر السابع: 7 أحرف، أول 4 أحرف مكررة + 3 عشوائية
        first_four = ''.join(random.choices(all_chars, k=4))
        last_three = ''.join(random.choices(all_chars, k=3))
        return first_four + first_four + last_three  # 11 أحرف
        # تعديل: مطلوب 7 أحرف فقط: أول 4 أحرف مكررة مرة واحدة + 3 عشوائية
        return first_four + last_three

    elif type_id == 8:
        # اليوزر الثامن: 5 أحرف مميزة (بدون تكرار)
        return ''.join(random.sample(all_chars, 5))

    elif type_id == 9:
        # اليوزر التاسع: 6 أحرف مميزة (بدون تكرار)
        return ''.join(random.sample(all_chars, 6))

    elif type_id == 10:
        # اليوزر العاشر: 3 أحرف وأرقام
        return ''.join(random.choices(all_chars, k=3))

    elif type_id == 11:
        # اليوزر الحادي عشر: 5 أحرف عشوائية
        return ''.join(random.choices(all_chars, k=5))

    elif type_id == 12:
        # اليوزر الثاني عشر: 6 أحرف عشوائية
        return ''.join(random.choices(all_chars, k=6))


def animated_title():
    title = "TOMAS USERNAME SCANNER\nBy:@K_DKP✓"
    for i in range(3):
        os.system('clear' if os.name != 'nt' else 'cls')
        print(YELLOW + "=" * 40 + RESET)
        print(' ' * i + CYAN + title + RESET)
        print(YELLOW + "=" * 40 + RESET)
        time.sleep(0.3)


def main_interface_colored(token, ID):
    os.system('clear' if os.name != 'nt' else 'cls')
    print(YELLOW + "=" * 40 + RESET)
    print(CYAN + "         TOMAS TOOL\n By:@K_DKP             " + RESET)
    print(YELLOW + "=" * 40 + RESET)
    print(f"TOKEN  : [ {MAGENTA}{token}{RESET} ]")
    print(f"ID : [ {MAGENTA}{ID}{RESET} ]\n")

    for platform in platforms:
        hit = f"{GREEN}{status[platform]['hit']}{RESET}"
        bad = f"{RED}{status[platform]['bad']}{RESET}"
        print(f"[ {platform:<10}] HIT: {hit:<3} | BAD: {bad:<3}")

    print(YELLOW + "-" * 37 + RESET)


def check_username(platform, username):
    url = platforms[platform].format(username)
    try:
        resp = requests.get(url, timeout=6)
        if resp.status_code == 200:
            return False
        elif resp.status_code == 404:
            return True
        else:
            return False
    except:
        return False

def send_to_telegram(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    try:
        requests.post(url, data=data, timeout=5)
    except:
        pass


def main():
    token = input(" TOKEN: ")
    ID = input(" ID: ")

    
    print("1 - رباعي ")
    print("2 - رباعي مكرر ")
    print("3 - ثلاثي")
    print("4 - رباعي مميز")
    print("5 - خماسي مكرر")
    print("6 - سداسي مكرر")
    print("7 - سباعي مكرر")
    print("8 - خماسي مميز")
    print("9 - سداسي مميز")
    print("10 - ثلاثي مميز")
    print("11 - خماسي")
    print("12 - سداسي")

    while True:
        try:
            type_id = int(input("Enter : "))
            if 1 <= type_id <= 12:
                break
            else:
                print("اختار من الاختيارات")
        except:
            print("❌.")

    animated_title()

    while True:
        username = generate_username(type_id)
        for platform in platforms:
            exists = check_username(platform, username)
            if exists:
                status[platform]['hit'] += 1
                message = f"يوزر متاح بمنصة {platform} \n اليوزر:{username}\nBy:@K_DKP"
                send_to_telegram(token, ID, message)
                print(f"{GREEN}[HIT]{RESET} {platform} Username : {username}")
            else:
                status[platform]['bad'] += 1
                print(f"{RED}[BAD]{RESET} {platform} Username : {username}")
        main_interface_colored(token, ID)
        time.sleep(1)


if __name__ == "__main__":
    main()