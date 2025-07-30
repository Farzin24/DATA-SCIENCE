
# Rotation matrix
import math
angle_deg = float(input("Enter rotation angle in degrees: "))
angle_rad = math.radians(angle_deg)

rotation_matrix = [[math.cos(angle_rad), -math.sin(angle_rad), 0],
                   [math.sin(angle_rad),  math.cos(angle_rad), 0],
                   [0, 0, 1]]

print("Rotation Matrix:")
for row in rotation_matrix:
    print(row)

# Scaling matrix
sx = float(input("Enter scaling factor along x-axis: "))
sy = float(input("Enter scaling factor along y-axis: "))

scaling_matrix = [[sx, 0, 0],
                  [0, sy, 0],
                  [0, 0, 1]]

print("Scaling Matrix:")
for row in scaling_matrix:
    print(row)
