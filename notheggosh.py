def find_missing_corner(points):
    x_missing = 0
    y_missing = 0
    z_missing = 0

    # XOR all the coordinates
    for x, y, z in points:
        x_missing ^= x
        y_missing ^= y
        z_missing ^= z

    return x_missing, y_missing, z_missing

# Input processing
points = []
for _ in range(7):
    x, y, z = map(int, input().split())
    points.append((x, y, z))

# Find and print the missing corner
missing_corner = find_missing_corner(points)
print(*missing_corner)
