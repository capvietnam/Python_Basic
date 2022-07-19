from math import pi


class MyMath:

    @staticmethod
    def circle_len(radius: (int, float)) -> (int, float):
        return 2 * radius * pi

    @staticmethod
    def circle_sq(radius: (int, float)) -> (int, float):
        return radius * pow(pi, 2)

    @staticmethod
    def cube_volume(side: (int, float)) -> (int, float):
        return pow(side, 3)

    @staticmethod
    def surface_area_sphere(radius: (int, float)) -> (int, float):
        return 4 * pi * pow(radius, 3)


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.cube_volume(side=5)
res_4 = MyMath.surface_area_sphere(radius=1)

print(res_1)
print(res_2)
print(res_3)
print(res_4)
