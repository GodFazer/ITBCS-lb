# Implementation-of-transformations-between-coordinate-systems



[Numpy`s little guide](https://www.geeksforgeeks.org/how-to-import-numpy-as-np/)


Ця програма на Python надає інструменти для перетворення між різними системами координат та обчислення відстаней у цих системах. Вона підтримує перетворення як у 2D, так і у 3D, а також включає функції для оцінки продуктивності.

### Перетворення координат:

Перетворення між полярними та декартовими координатами у 2D.
Перетворення між сферичними та декартовими координатами у 3D.

Обчислення відстаней:

Обчислення відстаней у декартових координатах (2D та 3D).
Обчислення відстаней у полярних координатах (2D).
Обчислення відстаней у сферичних координатах за допомогою об'єму та через перетворення в декартові координати.

### Бенчмаркінг:

Вимірювання часу, необхідного для обчислення відстаней у різних системах координат для заданої кількості точок.
Побудова графіків:

Візуалізація продуктивності обчислення відстаней у різних системах координат за допомогою стовпчастих діаграм.

## Використання

### Запуск програми

### Перетворення координат та обчислення відстаней:

Запустіть програму та виберіть опцію 1 для виконання перетворень координат та обчислення відстаней.
Виберіть систему координат (2D Полярна або 3D Сферична) та введіть необхідні параметри.
За бажанням, обчисліть відстань між двома точками у вибраній системі координат.

### Бенчмаркінг:

Виберіть опцію 2 для запуску бенчмарків.

Введіть кількість точок для бенчмарку (рекомендовано між 10,000 та 100,000).

Програма відобразить час, витрачений на обчислення відстаней у різних системах, та побудує графік результатів.

## Огляд функцій

### Функції перетворення координат:

polar_to_cartesian(r, theta): Перетворює полярні координати у декартові (2D).

cartesian_to_polar(x, y): Перетворює декартові координати у полярні (2D).

spherical_to_cartesian(r, theta, phi): Перетворює сферичні координати у декартові (3D).

cartesian_to_spherical(x, y, z): Перетворює декартові координати у сферичні (3D).

### Функції обчислення відстаней:

distance_cartesian_2d(x1, y1, x2, y2): Обчислює відстань між двома точками у декартових координатах (2D).

distance_cartesian_3d(x1, y1, z1, x2, y2, z2): Обчислює відстань між двома точками у декартових координатах (3D).

distance_polar(r1, theta1, r2, theta2): Обчислює відстань між двома точками у полярних координатах (2D).

distance_spherical_3d_volume(r1, theta1, phi1, r2, theta2, phi2): Обчислює відстань у сферичних координатах за допомогою об'єму.

### Функції бенчмаркінгу:

benchmark_cartesian_2d(n): Оцінює продуктивність обчислень відстаней у декартових координатах (2D).

benchmark_cartesian_3d(n): Оцінює продуктивність обчислень відстаней у декартових координатах (3D).

benchmark_polar(n): Оцінює продуктивність обчислень відстаней у полярних координатах.

benchmark_polar_2d_cartesian(n): Оцінює продуктивність обчислень відстаней у полярних координатах через перетворення в декартові.

benchmark_spherical_3d_volume(n): Оцінює продуктивність обчислень відстаней у сферичних координатах за допомогою об'єму.

benchmark_spherical_3d_cartesian(n): Оцінює продуктивність обчислень відстаней у сферичних координатах через перетворення в декартові.

### Побудова графіків:

plot_benchmarks(results): Побудує графік результатів бенчмарків.

### Залежності

numpy: Для чисельних обчислень.

matplotlib: Для побудови графіків результатів бенчмарків.

pandas: Для обробки даних у табличній формі.
