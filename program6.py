# code courtesy of Adam Dempsey
# modified for PHY1055 by Oisín Creaner
import matplotlib.pyplot as plt
import numpy as np

def density_change(x, y, dx, dy):
    plt.streamplot(x, y, dx, dy, density=[0.5, 0.5])


def coupled_de(x, y):
    dx = y
    dy = - x + (1 - (x ** 2)) * y
    return dx, dy


def main():
    plt.close('all')
    coords = np.linspace(-5, 5, 30)
    x, y = np.meshgrid(coords, coords)
    dx, dy = coupled_de(x, y)

    plt.figure(figsize=(6,6))
    plt.gca().set_aspect('equal', adjustable='box')  # Make plot box square
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('y vs x quiver/streamline plot')
    plt.quiver(x, y, dx, dy)  # plot field as quiver
    #density_change(x, y, dx, dy)
    plt.streamplot(x, y, dx, dy)  # plot streamlines of field.
    plt.show()


# if this is the module called directly, then execute the main function, otherwise only define it
if __name__ == '__main__':
    main()