import math
import time

# Перетворення між полярною та декартовою системами координат (2D)
def polar_to_cartesian(r, theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return x, y

def cartesian_to_polar(x, y):
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    return r, theta

# Перетворення між сферичною та декартовою системами координат (3D)
def spherical_to_cartesian(r, theta, phi):
    x = r * math.sin(phi) * math.cos(theta)
    y = r * math.sin(phi) * math.sin(theta)
    z = r * math.cos(phi)
    return x, y, z

def cartesian_to_spherical(x, y, z):
    r = math.sqrt(x**2 + y**2 + z**2)
    theta = math.arctan2(y, x)
    phi = math.arccos(z / r)
    return r, theta, phi

# Обчислення відстаней
def distance_cartesian_2d(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def distance_cartesian_3d(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def distance_polar(r1, theta1, r2, theta2):
    return math.sqrt(r1**2 + r2**2 - 2 * r1 * r2 * math.cos(theta2 - theta1))

def distance_spherical(r1, theta1, phi1, r2, theta2, phi2):
    return math.sqrt(r1**2 + r2**2 - 2 * r1 * r2 * (math.sin(phi1) * math.sin(phi2) * math.cos(theta1 - theta2) + math.cos(phi1) * math1.cos(phi2)))

# Функція для зчитування даних з клавіатури
def input_2d_point():
    r = float(input("Введіть радіус (r): "))
    theta = float(input("Введіть кут (theta, в радіанах): "))
    return r, theta

def input_3d_point():
    r = float(input("Введіть радіус (r): "))
    theta = float(input("Введіть азимутальний кут (theta, в радіанах): "))
    phi = float(input("Введіть полярний кут (phi, в радіанах): "))
    return r, theta, phi

# Основна функція для виконання перетворень
def main():
    print("Виберіть систему координат:")
    print("1: Полярна (2D)")
    print("2: Сферична (3D)")
    choice = input("Ваш вибір: ")

    if choice == '1':
        print("Перетворення між полярною та декартовою системами координат (2D)")
        r, theta = input_2d_point()
        x, y = polar_to_cartesian(r, theta)
        print(f"Декартові координати: x = {x}, y = {y}")
        r_back, theta_back = cartesian_to_polar(x, y)
        print(f"Повернені полярні координати: r = {r_back}, theta = {theta_back}")

    elif choice == '2':
        print("Перетворення між сферичною та декартовою системами координат (3D)")
        r, theta, phi = input_3d_point()
        x, y, z = spherical_to_cartesian(r, theta, phi)
        print(f"Декартові координати: x = {x}, y = {y}, z = {z}")
        r_back, theta_back, phi_back = cartesian_to_spherical(x, y, z)
        print(f"Повернені сферичні координати: r = {r_back}, theta = {theta_back}, phi = {phi_back}")

if __name__ == "__main__":
    main()
