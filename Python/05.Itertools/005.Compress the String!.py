from itertools import groupby

string = input()
lis = [(len(list(g)), int(k)) for k, g in groupby(string)]
print(*lis)