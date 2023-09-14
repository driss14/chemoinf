import numpy as np

def distance(a, b):
    return np.linalg.norm(b - a)
    
def angle(a, b, c):
    u1 = b - a
    u2 = c - b
    ang_rad = np.arccos(np.dot(u1, u2)/( np.linalg.norm(u1) * np.linalg.norm(u2)))
    return np.degrees(ang_rad)

def dihedral(a, b, c, d):
    u1 = b - a
    u2 = c - b
    u3 = d - c
    v1 = np.cross(u1, u2)
    v1 = v1 / np.linalg.norm(v1)
    v2 = np.cross(u2, u3)
    v2 = v2 / np.linalg.norm(v2)
    ang_rad = np.arccos(np.dot(v1, v2)/(np.linalg.norm(v1) * np.linalg.norm(v2)))
    sign =  np.sign(v1 * u3).sum()
    if sign != 0:
        ang_rad = ang_rad * sign
    return np.degrees(ang_rad)

if __name__ == '__main__':       
    C = np.array([0., 0., 0.])
    O = np.array([0., 0., 2.2])
    Cl = np.array([2.2, 0.0, 0.0])
    H = np.array([3, 0.5, 0.0]) 
    print('Distance between H and C: ',distance(H, C))
    print('Angle (H, C, O) : ',angle(H, C, O))
    print('Dihedral angle (H, C, O, Cl): ',dihedral(H, C, O, Cl)) 
    
