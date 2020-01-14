import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

def perform_bubble_sort(blist):
    cmpcount, swapcount = 0, 0
    for j in range(len(blist)):
        for i in range(1, len(blist)-j):
            cmpcount += 1
            if blist[i-1] > blist[i]:
                swapcount += 1
                blist[i-1], blist[i] = blist[i], blist[i-1]
    return swapcount

print("Array is sorted in {} swaps.".format(perform_bubble_sort(a)))
print("First Element: {}".format(sorted(a)[0]))
print("Last Element: {}".format(sorted(a)[n-1]))