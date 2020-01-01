N = int(input())
dic = {}

for _ in range(N):
    datas = input().split()
    dic[datas[0]] = datas[1]

while True:
    try:
        name = input()        
        if name in dic:
            print("{}={}".format(name, dic[name]))
        else:
            print("Not found")
    except:
        break