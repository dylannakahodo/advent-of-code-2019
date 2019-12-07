with open('input.txt') as f:
    wire_1_path = f.readline().strip().split(',')
    wire_2_path = f.readline().strip().split(',')

def manhattan_distance(point):
    return abs(point[0]) + abs(point[1])

def parse_wire_positions(wire_path):
    x,y = 0,0
    wire_positions = set()
    directions = {"R": (1,0), "L": (-1,0), "U": (0,1), "D": (0,-1)}

    for vector in wire_path:
        for _ in range(int(vector[1:])):
            direction = vector[0]
            x += directions[direction][0]
            y += directions[direction][1] 
                       
            wire_positions.add((x,y))
            
    return wire_positions

wire_1_points = parse_wire_positions(wire_1_path)
wire_2_points = parse_wire_positions(wire_2_path)

intersections = wire_1_points.intersection(wire_2_points)

closest = min(map(manhattan_distance,intersections))

print(closest)