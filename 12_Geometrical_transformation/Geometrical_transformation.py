import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.animation as animation


anchors = np.array([
    [-1, -1, -1],
    [-1,  2, -1],
    [ 2, -1, -1],
    [ 2,  2, -1],
    [-1, -1,  2],
    [-1,  2,  2],
    [ 2, -1,  2],
    [ 2,  2,  2]
])


edges = [
    (0,1), (1,3), (3,2), (2,0),  
    (4,5), (5,7), (7,6), (6,4),  
    (0,4), (1,5), (2,6), (3,7)   
]

#Rotation
def rotate(X, angle):
    rot = np.array([
        [math.cos(angle), -math.sin(angle), 0],
        [math.sin(angle),  math.cos(angle), 0],
        [0,0,1]
    ])
    return X @ rot

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


def animate(i):
    ax.clear()
    angle = 2 * math.pi * i / 36
    rotated = rotate(anchors, angle)
    ax.scatter(rotated[:, 0], rotated[:, 1], rotated[:, 2], color='green', s=50)
    
    #Add edges
    for edge in edges:
        p1 = rotated[edge[0]]
        p2 = rotated[edge[1]]
        xs, ys, zs = zip(p1, p2)
        ax.plot(xs, ys, zs, color='black')
    
    
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_zlim(-3, 3)
    ax.set_xlabel('Os x')
    ax.set_ylabel('Os y')
    ax.set_zlabel('Os z')
    ax.set_title('3D Rotation')


#Animation
ani = animation.FuncAnimation(fig, animate, frames=36, interval=100, repeat=True)
ani.save('Own_gifs\Own_rotation_3D_contours.gif', writer='imagemagick', fps=100)




