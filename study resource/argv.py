#*args的用法：当传入的参数个数未知，且不需要知道参数名称时。
def func_arg(farg, *args):
    print("formal arg:", farg)
    for arg in args:
        print("another arg:", arg)
func_arg(1,"youzan",'dba','四块五的妞')
print("-----------------------")
# 输出结果如下：
# formal arg: 1
# another arg: youzan
# another arg: dba
# another arg: 四块五的妞
# -----------------------