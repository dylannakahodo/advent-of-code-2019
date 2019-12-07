from one import manhattan_distance, parse_wire_positions

def count_steps(wire_path, intersections):
    x,y = 0,0
    steps = 0
    total_steps = dict()
    directions = {"R": (1,0), "L": (-1,0), "U": (0,1), "D": (0,-1)}

    for vector in wire_path:
        for _ in range(int(vector[1:])):
            direction = vector[0]
            x += directions[direction][0]
            y += directions[direction][1] 
            steps += 1
            
            if (x,y) in intersections:
                total_steps[(x,y)] = steps
    return total_steps

if __name__ == "__main__":
    with open('input.txt') as f:
        wire_1_path = f.readline().strip().split(',')
        wire_2_path = f.readline().strip().split(',')
        
    wire_1_points = parse_wire_positions(wire_1_path)
    wire_2_points = parse_wire_positions(wire_2_path)

    intersections = wire_1_points.intersection(wire_2_points)
    wire_1_steps = count_steps(wire_1_path, intersections)
    wire_2_steps = count_steps(wire_2_path, intersections)

    print(min(wire_1_steps[intersection] + wire_2_steps[intersection] for intersection in intersections))