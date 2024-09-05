import numpy as np
import time

# Перетворення між полярною та декартовою системами координат (2D)
def polar_to_cartesian(r, theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

def cartesian_to_polar(x, y):
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    return r, theta

# Перетворення між сферичною та декартовою системами координат (3D)
def spherical_to_cartesian(r, theta, phi):
    x = r * np.sin(phi) * np.cos(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * np.cos(phi)
    return x, y, z

def cartesian_to_spherical(x, y, z):
    r = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arctan2(y, x)
    phi = np.arccos(z / r)
    return r, theta, phi

# Обчислення відстаней у декартовій системі координат (3D)
def distance_cartesian_3d(x1, y1, z1, x2, y2, z2):
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

# Обчислення відстаней у полярній системі координат (2D)
def distance_polar(r1, theta1, r2, theta2):
    return np.sqrt(r1**2 + r2**2 - 2 * r1 * r2 * np.cos(theta2 - theta1))

# Обчислення відстаней у сферичній системі координат через об'єм сфери
def distance_spherical_3d_volume(r1, theta1, phi1, r2, theta2, phi2):
    return np.sqrt(r1**2 + r2**2 - 2 * r1 * r2 * (np.sin(phi1) * np.sin(phi2) * np.cos(theta1 - theta2) + np.cos(phi1) * np.cos(phi2)))

# Обчислення великої колової відстані по поверхні сфери
def distance_spherical_3d_surface(r, theta1, phi1, theta2, phi2):
    return r * np.arccos(np.sin(phi1) * np.sin(phi2) + np.cos(phi1) * np.cos(phi2) * np.cos(theta1 - theta2))

# Функція для зчитування даних з клавіатури (2D полярні координати)
def input_2d_point():
    r = float(input("Введіть радіус (r): "))
    theta = float(input("Введіть кут (theta, в радіанах): "))
    return r, theta

# Функція для зчитування даних з клавіатури (3D сферичні координати)
def input_3d_point():
    r = float(input("Введіть радіус (r): "))
    theta = float(input("Введіть азимутальний кут (theta, в радіанах): "))
    phi = float(input("Введіть полярний кут (phi, в радіанах): "))
    return r, theta, phi

# Основна функція для виконання перетворень та обчислення відстаней
def main():
    print("Виберіть систему координат:")
    print("1: Полярна (2D)")
    print("2: Сферична (3D)")
    choice = input("Ваш вибір: ")

    print("Ви хочете виконати обчислення відстані між двома точками?")
    print("1: Так")
    print("2: Ні, тільки перетворення")
    calc_distance = input("Ваш вибір: ")

    if choice == '1':
        print("Перетворення між полярною та декартовою системами координат (2D)")
        r1, theta1 = input_2d_point()
        x1, y1 = polar_to_cartesian(r1, theta1)
        print(f"Декартові координати: x = {x1}, y = {y1}")
        r_back, theta_back = cartesian_to_polar(x1, y1)
        print(f"Повернені полярні координати: r = {r_back}, theta = {theta_back}")

        if calc_distance == '1':
            print("Введіть координати другої точки:")
            r2, theta2 = input_2d_point()
            x2, y2 = polar_to_cartesian(r2, theta2)
            dist_polar = distance_polar(r1, theta1, r2, theta2)
            print(f"Відстань між точками у полярній системі: {dist_polar:.4f}")
            dist_cartesian = distance_cartesian_3d(x1, y1, 0, x2, y2, 0)
            print(f"Відстань між точками у декартовій системі (2D): {dist_cartesian:.4f}")

    elif choice == '2':
        print("Перетворення між сферичною та декартовою системами координат (3D)")
        r1, theta1, phi1 = input_3d_point()
        x1, y1, z1 = spherical_to_cartesian(r1, theta1, phi1)
        print(f"Декартові координати: x = {x1}, y = {y1}, z = {z1}")
        r_back, theta_back, phi_back = cartesian_to_spherical(x1, y1, z1)
        print(f"Повернені сферичні координати: r = {r_back}, theta = {theta_back}, phi = {phi_back}")

        if calc_distance == '1':
            print("Введіть координати другої точки:")
            r2, theta2, phi2 = input_3d_point()
            x2, y2, z2 = spherical_to_cartesian(r2, theta2, phi2)

            # Обчислення відстані у декартовій системі координат
            dist_cartesian_3d = distance_cartesian_3d(x1, y1, z1, x2, y2, z2)
            print(f"Відстань між точками у декартовій системі (3D): {dist_cartesian_3d:.4f}")

            # Обчислення відстані у сферичній системі через об'єм сфери
            dist_spherical_volume = distance_spherical_3d_volume(r1, theta1, phi1, r2, theta2, phi2)
            print(f"Відстань між точками у сферичній системі через об'єм сфери: {dist_spherical_volume:.4f}")

            # Обчислення великої колової відстані (по поверхні сфери)
            if r1 == r2:
                dist_spherical_surface = distance_spherical_3d_surface(r1, theta1, phi1, theta2, phi2)
                print(f"Велика колова відстань по поверхні сфери: {dist_spherical_surface:.4f}")
            else:
                print("Точки знаходяться на різних сферах, не можна обчислити велику колову відстань.")

if __name__ == "__main__":
    main()
