import container as cont


import numpy as np
from enum import Enum
from scipy import optimize

import matplotlib.pyplot as plt

class Material(Enum):
    steel = 'Сталь ХВГ'
    brass = 'Латунь 113'
    titanium_alloy = 'Титановый Сплав Т12'
    aluminum_alloy = 'Алюминиевый Сплав А231'
    polymer_composite = 'Полимерный Композит ПК 421'

    def __str__(self):
        return f'{self.value}'

class Container_Triangle_Pentagon(cont.Container):
    def __init__(self, material: Material,
                 coef: float, volume: float) -> None:
        self.__height = 0
        self.__outer_size = 0
        self.__inner_size = 0
        self.__surface_area = 0

        self.__material = material
        self.__volume = volume
        self.__coef = coef

    @property
    def volume(self):
        return self.__volume
    def get_size(self, height : float,
                 outer_size : float,
                 inner_size : float,
                 surface_area : float):
        self.__height = height
        self.__outer_size = outer_size
        self.__inner_size = inner_size
        self.__surface_area = surface_area
 

    def __str__(self) -> str:
        return (f'ReservoirCircleSquare {{\n'
            f'    volume: {self.__volume},\n'
            f'    coef: {self.__coef},\n'
            f'    material: {self.__material},\n'
            f'    height: {self.__height:.3f},\n'
            f'    outer_size: {self.__outer_size:.3f},\n'
            f'    inner_size: {self.__inner_size:.3f},\n'
            f'    surface_area: {self.__surface_area:.3f},\n' 
            f'}}')


    # ДАННЫЙ МЕТОД ОТВЕЧАЕТ ЗА НАХОЖДЕНИЕ ОБЪЕМА
    def __fvolume(self, H: float, R: float) -> float:
        return H * R ** 2 * (np.pi - self.__coef ** 2) 

    def __fradius(self, H: float) -> float:
        return np.sqrt(self.__volume / (H * (np.pi - self.__coef ** 2))) 
    def __fsurface(self, H: float) -> float:
        return (2 * self.__fradius(H) ** 2 * (np.pi - self.__coef ** 2) +
                4 * self.__fradius(H) * H * np.pi + 5 * self.__coef) 
                
    def optimize(self) -> None:
        h0 = np.cbrt(self.__volume)
        h_min = optimize.fmin(self.__fsurface, h0)[0]
        R_min = self.__fradius(h_min)
        r_min = self.__coef * R_min
        ff_min = self.__fsurface(h_min)
        self.get_size(height=h_min, outer_size=R_min, inner_size=r_min, surface_area=ff_min)
        plt.xlabel('Ряд шагов')
        plt.ylabel('Ряд поверхностей')

        list_starts = np.linspace(h0/3, 2 * h0, 50)
        list_surface = [self.__fsurface(h) for h in list_starts]

        plt.plot(list_starts, list_surface, marker='o')
        plt.annotate('local min', xy=(h_min, ff_min), xytext=(h_min+1, ff_min+20),
                     arrowprops=dict(facecolor='black', shrink=0.05),
                     )
        plt.show()

    def result(self):
        return self.__material, self.__volume, self.__outer_size, self.__inner_size, self.__surface_area
