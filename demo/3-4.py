#TODO: try-except
try:
    num = input('請輸入一個數字')
    num = int(num) # input 本身輸入 字串，需轉型態
    total = num + 1
    print(total)
except ValueError:  # 抓住 ValueError 錯誤
                    # ValueError 是Python報出的錯誤, 說明輸入的參數有問題
    print('請輸入數字')
except:
    print('發生錯誤')


try:
    num = input('請輸入一個數字')
    num = int(num)
    total = num + 1
    print(total)
except ValueError: # 抓住 ValueError
    print('請輸入數字')
except: # 抓住 所有錯誤
    print('發生錯誤')
else:
    # 當 try 沒有發生任何錯誤時，就會繼續執行 else
    print('成功執行')
finally:
    # 不管 try 是否執行成果，都會繼續執行 else
    print('程式結束')