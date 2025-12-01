from input_data import data

data = [(x[0], int(x[1:])) for x in data.split('\n')]
# print(data)

ans = 0
key = 50
for direction, num in data:
    #   part 1
    # if key == 0:
    #         ans += 1
    #   end of change for part 1 (uncomment)
    tmp = 1 if direction == 'R' else -1
    for _ in range(num):
        #   part 2
        if key == 0:
            ans += 1
        #   end of change for part 2
        key += tmp
        if key < 0:
            key = 99
        elif key > 99:
            key = 0



print(ans)