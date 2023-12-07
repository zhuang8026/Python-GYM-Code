# Python 單元測試官網文件
# https://docs.python.org/zh-tw/3/library/unittest.html


def calculate(w, h):
    return round(w/h**2,2)

def cmToM(cm):
    return cm/100

print(__name__) # result: __main__
                # 主要入口會打印出 __main__

if __name__ == '__main__':  # 作用：判斷此文件是 單獨 運作，還是被其他文件引用
                            # 只有自己運作才會是 "__main__"
    import unittest 
    # TestCase 測試案例
    # TestSuite 測試套件
    # TestRunner 測試執行器
    class BmiTestCase(unittest.TestCase):

        def test_calculate(self):
            result = calculate(65, 1.75) #result: 21.22, 呼叫外層函式
            self.assertEqual(21.22, result); # 檢查參數是否一樣, 
                                             # assertEqual(期望的結果, 程式計算的結果)
        def test_cmToM(self):
            result = cmToM(175)
            self.assertEqual(1.75, result) # 檢查參數是否一樣

    tests = [
        BmiTestCase('test_calculate'), # 放入函式 test_calculate
        BmiTestCase('test_cmToM')  #放入函式 test_cmToM
    ]
    suite = unittest.TestSuite() # 測試套件
    suite.addTests(tests)

    runner = unittest.TextTestRunner() # 測試執行器
    runner.run(suite)
