from wand.image import Image 
from wand.drawing import Drawing 
from wand.color import Color 
import wand.display


# Generujemy obiekt dla wand.drawing
with Drawing() as draw: 
  
    # Ustawiamy kolor na czarny
    draw.stroke_color = Color('black') 
  
    # Szerokosc obrysu
    draw.stroke_width = 3
  
    # points list to determine curve 
    points = [(68, 420), # Start point 
              (67, 420), # First control 
              (92, 420), # Second control 
              (106, 420)] # End point  

    points2 = [(106, 420), # Start point 
              (107, 420), # First control 
              (136, 360), # Second control 
              (132, 362)] # End point  

    points3 = [(132, 362), # Start point 
              (130, 363), # First control 
              (205, 361), # Second control 
              (205, 361)] # End point

    points4 = [(205, 361), # Start point 
              (205, 346), # First control 
              (229, 426), # Second control 
              (228, 425)] # End point

    points5 = [(228, 425), # Start point 
              (226, 423), # First control 
              (265, 423), # Second control 
              (265, 424)] # End point

    points6 = [(265, 424), # Start point 
              (264, 426), # First control 
              (175, 144), # Second control 
              (169, 144)] # End point

    points7 = [(169, 144), # Start point 
              (156, 143), # First control 
              (82, 420), # Second control 
              (67, 420)] # End point

    points8 = [(67, 420), # Start point 
              (66, 420), # First control 
              (82, 420), # Second control 
              (104, 420)] # End point

    points9 = [(104, 420), # Start point 
              (108, 420), # First control 
              (134, 355), # Second control 
              (134, 361)] # End point

    points10 = [(134, 361), # Start point 
              (134, 363), # First control 
              (163, 206), # Second control 
              (168, 206)] # End point

    points11 = [(168, 206), # Start point 
              (170, 206), # First control 
              (204, 361), # Second control 
              (204, 359)] # End point

    points12 = [(204, 359), # Start point 
              (204, 341), # First control 
              (200, 338), # Second control 
              (201, 338)] # End point

    points13 = [(201, 338), # Start point 
              (202, 338), # First control 
              (139, 340), # Second control 
              (137, 339)] # End point


    pointsb = [(271, 73), # Start point 
              (287, 65), # First control 
              (377, 57), # Second control 
              (390, 58)] # End point 

    pointsb2 = [(390, 58), # Start point 
              (417, 64), # First control 
              (519, 37), # Second control 
              (515, 146)] # End point

    pointsb3 = [(515, 146), # Start point 
              (512, 225), # First control 
              (427, 224), # Second control 
              (415, 224)] # End point

    pointsb4 = [(415, 224), # Start point 
              (376, 224), # First control 
              (516, 217), # Second control 
              (516, 301)] # End point

    pointsb5 = [(516, 301), # Start point 
              (516, 394), # First control 
              (450, 408), # Second control 
              (435, 406)] # End point

    pointsb6 = [(435, 406), # Start point 
              (420, 404), # First control 
              (272, 407), # Second control 
              (257, 406)] # End point

    pointsb7 = [(257, 406), # Start point 
              (208, 404), # First control 
              (202, 389), # Second control 
              (227, 388)] # End point

    pointsb8 = [(227, 388), # Start point 
              (249, 387), # First control 
              (274, 385), # Second control 
              (274, 381)] # End point

    pointsb9 = [(274, 381), # Start point 
              (274, 366), # First control 
              (279, 136), # Second control 
              (275, 115)] # End point

    pointsb10 = [(275, 115), # Start point 
              (272, 100), # First control 
              (237, 105), # Second control 
              (222, 102)] # End point

    pointsb11 = [(222, 101), # Start point 
              (194, 96), # First control 
              (216, 74), # Second control 
              (231, 77)] # End point

    pointsb12 = [(231, 77), # Start point 
              (246, 80), # First control 
              (293, 81), # Second control 
              (263, 74)] # End point

    pointsb13 = [(263, 74), # Start point 
              (248, 71), # First control 
              (329, 75), # Second control 
              (319, 87)] # End point

    pointsb14 = [(319, 87), # Start point 
              (314, 93), # First control 
              (317, 186), # Second control 
              (320, 198)] # End point

    pointsb15 = [(320, 198), # Start point 
              (324, 213), # First control 
              (456, 217), # Second control 
              (454, 147)] # End point

    pointsb16 = [(454, 147), # Start point 
              (452, 80), # First control 
              (322, 98), # Second control 
              (320, 83)] # End point

    pointsb17 = [(320, 83), # Start point 
              (318, 68), # First control 
              (314, 287), # Second control 
              (317, 271)] # End point

    pointsb18 = [(317, 271), # Start point 
              (320, 256), # First control 
              (425, 254), # Second control 
              (438, 261)] # End point

    pointsb19 = [(438, 261), # Start point 
              (472, 279), # First control 
              (477, 313), # Second control 
              (466, 348)] # End point

    pointsb20 = [(466, 348), # Start point 
              (460, 367), # First control 
              (396, 383), # Second control 
              (371, 381)] # End point

    pointsb21 = [(371, 381), # Start point 
              (356, 380), # First control 
              (333, 380), # Second control 
              (318, 358)] # End point

    pointsb22 = [(318, 358), # Start point 
              (310, 346), # First control 
              (305, 290), # Second control 
              (319, 275)] # End point

  
    # Wypelnienie bialym kolorem
    draw.fill_color = Color('white') 
  
    # Rysowanie punktow uzywajac funkcji bezier
    draw.bezier(points)  
    draw.bezier(points2)  
    draw.bezier(points3)  
    draw.bezier(points4)  
    draw.bezier(points5)  
    draw.bezier(points6)  
    draw.bezier(points7)  
    draw.bezier(points8)  
    draw.bezier(points9)
    draw.bezier(points10)
    draw.bezier(points11)
    draw.bezier(points12)
    draw.bezier(points13)

    draw.bezier(pointsb)
    draw.bezier(pointsb2)
    draw.bezier(pointsb3)
    draw.bezier(pointsb4)
    draw.bezier(pointsb5)
    draw.bezier(pointsb6)
    draw.bezier(pointsb7)
    draw.bezier(pointsb8)
    draw.bezier(pointsb9)
    draw.bezier(pointsb10)
    draw.bezier(pointsb11)
    draw.bezier(pointsb12)
    draw.bezier(pointsb13)
    draw.bezier(pointsb14)
    draw.bezier(pointsb15)
    draw.bezier(pointsb16)
    draw.bezier(pointsb17)
    draw.bezier(pointsb18)
    draw.bezier(pointsb19)
    draw.bezier(pointsb20)
    draw.bezier(pointsb21)
    draw.bezier(pointsb22)


    with Image(width = 800, 
               height = 800, 
               background = Color('white')) as img: 
  
        # Rysowanie uzywajac obrazka img
        draw.draw(img) 
        wand.display.display(img)   # Wyswietlenie obrazka
