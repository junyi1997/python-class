while True:
    try:
        num=int(input("請輸入整數："))
        break
    except ValueError:
        print("輸入錯誤！請輸入整數")
        continue
print("您輸入的數字為：{:}".format(num))    

print(f"123|{num:10d}|")