from containertrianglepentagon import *

def main():
    # КОЭФФИЦИЕНТЫ VOLUME COEF И MATERIAL МОЖНО ДРУГИЕ ВЫБРАТЬ
    r1 = Container_Triangle_Pentagon(volume=115, coef=0.20, material=Material.steel)
    r2 = Container_Triangle_Pentagon(volume=135, coef=0.40, material=Material.titanium_alloy)
    r3 = Container_Triangle_Pentagon(volume=120, coef=0.35, material=Material.polymer_composite)


    l_r : list[Container_Triangle_Pentagon] = []
 
    print(r1)
    r1.optimize()
    print(r1)
    l_r.append(r1)
    print(r2)
    r2.optimize()
    print(r2)
    l_r.append(r2)
    print(r3)
    r3.optimize()
    print(r3)
    l_r.append(r3)
    #print(l_r)

    sorted_list = sorted(l_r, key=lambda Container_Triangle_Pentagon:Container_Triangle_Pentagon.volume)
    for el in sorted_list:
        print(Container_Triangle_Pentagon.__str__(el))


if __name__ == '__main__':
    main()


