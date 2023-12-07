bim = lambda w,h: w/h; # lambda 傳入參數: 運算條件
bim(2,3);

res = lambda x: 'nice' if x > 10 else 'soso' if x > 5 else 'bad';
            # 'nice' if x > 10
            # 'soso' if x > 5
res(bim(2,3))

list1 = [8,9,7,5,4,2];
fun = filter(lambda x: x>5, list1);

fun2 = map(lambda x: x+1, list1);