def takeSecond(elem):
    return elem[1]

if __name__ == '__main__':
    
    name_list = []
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        name_list.append([name, score])
        score_list.append(score)

    name_list = sorted(name_list)
    score = sorted(set(score_list))
    
    for key, value in name_list:
        if score[1] == value:
            print(key)
