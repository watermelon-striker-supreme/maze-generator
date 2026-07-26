import random

width = 21
length = 21

for _ in range(5):

    current_pos = [(width + 1) // 2, (length + 1) // 2]
    positions = []
    grid = [['⬛'] * width for _ in range(length)]
    grid[0][1] = '🟥'
    grid[length-1][width-2] = '🟦'

    while True:
        directions = []
        initial_x = current_pos[0]
        initial_y = current_pos[1]
        up_dist = 1
        down_dist = 1
        left_dist = 1
        right_dist = 1

        while True:
            if current_pos[1]-up_dist < 0 or grid[current_pos[1]-up_dist][current_pos[0]] == '⬜':
                break
            else:
                up_dist += 1

        while True:
            if current_pos[1]+down_dist > length - 1 or grid[current_pos[1]+down_dist][current_pos[0]] == '⬜':
                break
            else:
                down_dist += 1

        while True:
            if current_pos[0]-left_dist < 0 or grid[current_pos[1]][current_pos[0]-left_dist] == '⬜':
                break
            else:
                left_dist += 1

        while True:
            if current_pos[0]+right_dist > width - 1 or grid[current_pos[1]][current_pos[0]+right_dist] == '⬜':
                break
            else:
                right_dist += 1

        if up_dist >= 3:
            directions.append('up')

        if down_dist >= 3:
            directions.append('down')

        if left_dist >= 3:
            directions.append('left')

        if right_dist >= 3:
            directions.append('right')
            
        if not directions:
            positions.pop()
            if not positions:
                break
            else:
                current_pos = positions[-1]
                continue

        z = random.choice(directions)

        if z == 'up':
            dest_y = (initial_y - 2)
            for i in range(dest_y, initial_y):
                grid[i][current_pos[0]] = '⬜'
            current_pos = [initial_x, dest_y]

        elif z == 'down':
            dest_y = (initial_y + 2)
            for i in range(initial_y, dest_y + 1):
                grid[i][current_pos[0]] = '⬜'
            current_pos = [initial_x, dest_y]

        elif z == 'left':
            dest_x = (initial_x - 2)
            for i in range(dest_x, initial_x):
                grid[current_pos[1]][i] = '⬜'
            current_pos = [dest_x, initial_y]

        elif z == 'right':
            dest_x = (initial_x + 2)
            for i in range(initial_x, dest_x + 1):
                grid[current_pos[1]][i] = '⬜'
            current_pos = [dest_x, initial_y]
        
        positions.append(current_pos)

    for i in range(len(grid)):
        print(f"{grid[i]} \n")
    print("\n")