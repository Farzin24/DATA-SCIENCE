import numpy as np

def translation_matrix(tx, ty, tz):
    return np.array([[1,0,0,tx],[0,1,0,ty],[0,0,1,tz],[0,0,0,1]])

def scaling_matrix(sx, sy, sz):
    return np.array([[sx,0,0,0],[0,sy,0,0],[0,0,sz,0],[0,0,0,1]])

def rotation_matrix_x(angle_deg):
    theta = np.radians(angle_deg)
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[1,0,0,0],[0,c,-s,0],[0,s,c,0],[0,0,0,1]])

tx, ty, tz = map(float, input("Enter translation tx ty tz: ").split())
sx, sy, sz = map(float, input("Enter scaling sx sy sz: ").split())
angle = float(input("Enter rotation angle in degrees (X-axis): "))

print("Translation Matrix:\n", translation_matrix(tx, ty, tz))
print("Scaling Matrix:\n", scaling_matrix(sx, sy, sz))
print("Rotation Matrix (X-axis):\n", rotation_matrix_x(angle))
