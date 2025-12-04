from input_data import data

data = [[int(y) for y in x.split('-')] for x in data.split(',')]

ans1 = 0
for x in data:
    for num in range(x[0], x[1]+1):
        m, n = len(str(num))//2, len(str(num))//2
        # print( list(str(num))[:n], str(num)[n:], sep=':')
        if len(str(num))%2==0 and str(num)[:n] == str(num)[n:]:

            ans1 += num

print(ans1)

# task 2
checked = []
ans2 = 0
for x in data:
    for num in range(x[0], x[1]+1):
        for i in range(1, len(str(num))//2+1):
             if str(num).count(str(num)[:i])*i == len(str(num)) and num not in checked:
                 checked.append(num)
                 ans2 += num

print(ans2)




