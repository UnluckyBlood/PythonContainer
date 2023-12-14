
class Container(object):
    def __init__(self, height : float,
                 outer_size : float,
                 inner_size : float,
                 surface_area : float) -> None:
        self.__height = height
        self.__outer_size = outer_size
        self.__inner_size = inner_size
        self.__surface_area = surface_area
 
    def get_size(self, height : float,
                 outer_size : float,
                 inner_size : float,
                 surface_area : float):
        self.__height = height
        self.__outer_size = outer_size
        self.__inner_size = inner_size
        self.__surface_area = surface_area

