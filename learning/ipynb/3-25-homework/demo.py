"""
83, 41, 72, 58, 61, 36

氣泡排序法
將序列從小排到大，序列中的數字兩兩比較，把小的數字往前面移動
"""

def bubble(list):
    for round in range(1, len(list)): # range(起始值, 結束值), len() = 長度
        # print(round) # 1 2 3 4 5
        for i in range(0, len(list)-round): # ex: 6-1
            # print(i) # 0 1 2 3 4
            if list[i] > list[i+1]:  # 83 > 41 ?
                list[i], list[i+1] = list[i+1], list[i] # 如果是 True, 就交換
        print(str(round) + ' round :' + str(list))

    return

if __name__ == '__main__':
    list = [83, 41, 72, 58, 61, 36]
    print('origin : ' + str(list))
    bubble(list)