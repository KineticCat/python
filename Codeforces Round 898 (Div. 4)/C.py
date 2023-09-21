def calculate_points(target):
    point_values = [1, 2, 3, 4, 5]
    
    total_points = 0
    
    for i in range(10):
        for j in range(10):
            if target[i][j] == "X":  
                distance = min(i, j, 9 - i, 9 - j)
                ring_value = point_values[distance]
                total_points += ring_value
    
    return total_points

t = int(input())

for _ in range(t):
    target = [input() for _ in range(10)]  
    result = calculate_points(target)
    print(result)
