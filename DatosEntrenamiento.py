import numpy as np
#precio/calidadVideo/SO/Rendimiento/Duracionbateria/Uso(escolar,gamer,oficina,hogar,ingenieria,edicion y modelado 3D)
datos_entrenamiento = np.array([
    [11, 1, 1, 1, 3, 1],  # Lenovo IdeaPad 3
    [11, 1, 1, 1, 3, 1],  # Lenovo IdeaPad 3
    [11, 1, 1, 1, 3, 1],  # Lenovo IdeaPad 3
    [11, 1, 1, 1, 2, 3],  # Lenovo IdeaPad 3
    [11, 1, 1, 1, 2, 4],  # Lenovo IdeaPad 3

    [14, 2, 1, 2, 2, 2],  # Laptop Lenovo 81Y4001HUS
    [14, 2, 1, 2, 2, 2],  # Laptop Lenovo 81Y4001HUS
    [14, 2, 1, 2, 2, 4],  # Laptop Lenovo 81Y4001HUS
    [14, 2, 1, 2, 1, 5],  # Laptop Lenovo 81Y4001HUS
    [14, 1, 1, 2, 1, 5],  # Laptop Lenovo 81Y4001HUS

    [25, 2, 1, 2, 2, 2],   # Acer Predator Helios 300 
    [25, 2, 1, 2, 2, 2],   # Acer Predator Helios 300 
    [25, 2, 1, 2, 1, 2],   # Acer Predator Helios 300 
    [25, 2, 1, 2, 1, 2],   # Acer Predator Helios 300 
    [25, 1, 1, 3, 1, 5],   # Acer Predator Helios 300

    [30, 2, 1, 3, 1, 2],  # Acer Predator Helios 300 PH315-54-760S
    [30, 2, 1, 3, 1, 2],  # Acer Predator Helios 300 PH315-54-760S
    [30, 2, 1, 3, 1, 2],  # Acer Predator Helios 300 PH315-54-760S
    [30, 2, 1, 2, 2, 6],  # Acer Predator Helios 300 PH315-54-760S
    [30, 2, 1, 2, 2, 5],  # Acer Predator Helios 300 PH315-54-760S

    [26, 2, 1, 2, 2, 2],   # Laptop Lenovo IdeaPad Gaming 3i
    [26, 2, 1, 2, 2, 2],   # Laptop Lenovo IdeaPad Gaming 3i
    [26, 2, 1, 3, 1, 5],   # Laptop Lenovo IdeaPad Gaming 3i
    [26, 2, 1, 3, 1, 5],   # Laptop Lenovo IdeaPad Gaming 3i
    [26, 1, 1, 3, 1, 5],   # Laptop Lenovo IdeaPad Gaming 3i

    [24, 1, 1, 2, 1, 2],   # Laptop MSI GF63 Thin 10SCSR
    [24, 1, 1, 2, 1, 2],   # Laptop MSI GF63 Thin 10SCSR
    [24, 1, 1, 2, 1, 2],   # Laptop MSI GF63 Thin 10SCSR
    [24, 2, 1, 2, 1, 5],   # Laptop MSI GF63 Thin 10SCSR
    [24, 1, 1, 1, 1, 5],   # Laptop MSI GF63 Thin 10SCSR

    [20, 2, 1, 3, 1, 2],  # Laptop MSI Gamer Cyborg 15  
    [20, 2, 1, 3, 1, 2],  # Laptop MSI Gamer Cyborg 15
    [20, 2, 1, 3, 1, 6],  # Laptop MSI Gamer Cyborg 15
    [20, 2, 1, 3, 1, 5],  # Laptop MSI Gamer Cyborg 15
    [20, 1, 1, 2, 2, 2],  # Laptop MSI Gamer Cyborg 15

    [19, 2, 1, 2, 3, 1],  # Laptop HP Envy
    [19, 2, 1, 2, 3, 3],  # Laptop HP Envy
    [19, 2, 1, 2, 2, 3],  # Laptop HP Envy
    [19, 1, 1, 1, 3, 4],  # Laptop HP Envy
    [19, 2, 1, 1, 3, 4],  # Laptop HP Envy

    [12, 1, 1, 2, 2, 1],  # Laptop HP 240 G10
    [12, 2, 1, 1, 3, 1],  # Laptop HP 240 G10
    [12, 2, 1, 1, 3, 1],  # Laptop HP 240 G10
    [12, 2, 1, 1, 1, 3],  # Laptop HP 240 G10
    [12, 2, 1, 1, 3, 4],  # Laptop HP 240 G10

    [6, 1, 1, 1, 2, 1],  # Laptop HP 240 G8  
    [6, 1, 1, 1, 2, 1],  # Laptop HP 240 G8
    [6, 1, 1, 1, 2, 1],  # Laptop HP 240 G8
    [6, 1, 1, 1, 2, 1],  # Laptop HP 240 G8
    [6, 1, 1, 1, 3, 4],  # Laptop HP 240 G8

    [8, 2, 1, 2, 3, 4],  # ThinkPad L13 Yoga Gen 2
    [8, 1, 1, 1, 2, 4],  # ThinkPad L13 Yoga Gen 2
    [8, 1, 1, 1, 2, 4],  # ThinkPad L13 Yoga Gen 2
    [8, 1, 1, 2, 1, 3],  # ThinkPad L13 Yoga Gen 2
    [8, 1, 1, 2, 2, 3],  # ThinkPad L13 Yoga Gen 2

    [14, 2, 1, 2, 2, 1],  # Laptop ASUS Vivobook 14 
    [14, 2, 1, 2, 2, 1],  # Laptop ASUS Vivobook 14 
    [14, 2, 1, 2, 1, 3],  # Laptop ASUS Vivobook 14 
    [14, 1, 1, 1, 2, 4],  # Laptop ASUS Vivobook 14 
    [14, 2, 1, 1, 1, 4],  # Laptop ASUS Vivobook 14 

    [9, 1, 1, 2, 3, 3],  # DELL Latitude 7420  
    [9, 1, 1, 1, 1, 4],  # DELL Latitude 7420
    [9, 1, 1, 2, 2, 1],  # DELL Latitude 7420
    [9, 1, 1, 2, 1, 3],  # DELL Latitude 7420
    [9, 1, 1, 1, 2, 4],  # DELL Latitude 7420

    [8, 1, 1, 1, 2, 1],  # ACER Laptop Aspire 5
    [8, 1, 1, 2, 3, 1],  # ACER Laptop Aspire 5
    [8, 1, 1, 1, 3, 4],  # ACER Laptop Aspire 5
    [8, 1, 1, 1, 2, 1],  # ACER Laptop Aspire 5
    [8, 1, 1, 2, 2, 1],  # ACER Laptop Aspire 5

    [20, 2, 1, 2, 1, 2],  # Acer Nitro 5 AN515-55-53E5 Laptop Gaming 
    [20, 1, 1, 2, 1, 2],  # Acer Nitro 5 AN515-55-53E5 Laptop Gaming
    [20, 2, 1, 2, 1, 5],  # Acer Nitro 5 AN515-55-53E5 Laptop Gaming
    [20, 2, 1, 3, 2, 5],  # Acer Nitro 5 AN515-55-53E5 Laptop Gaming
    [20, 2, 1, 2, 2, 5],  # Acer Nitro 5 AN515-55-53E5 Laptop Gaming

    [24, 1, 1, 1, 1, 2],  # Laptop Gaming Msi Gf75 Thin 10scrx 
    [24, 2, 1, 2, 1, 5],  # Laptop Gaming Msi Gf75 Thin 10scrx
    [24, 2, 1, 2, 1, 5],  # Laptop Gaming Msi Gf75 Thin 10scrx
    [24, 2, 1, 2, 2, 5],  # Laptop Gaming Msi Gf75 Thin 10scrx
    [24, 2, 1, 2, 2, 2],  # Laptop Gaming Msi Gf75 Thin 10scrx 

    [9, 1, 1, 1, 3, 3],  # ASUS Laptop Vivobook 14/14
    [9, 2, 1, 2, 2, 3],  # ASUS Laptop Vivobook 14/14
    [9, 2, 1, 1, 1, 1],  # ASUS Laptop Vivobook 14/14
    [9, 1, 1, 1, 2, 3],  # ASUS Laptop Vivobook 14/14
    [9, 1, 1, 1, 2, 3],  # ASUS Laptop Vivobook 14/14

    [12, 1, 1, 2, 1, 5],  # MSI GF63 Thin 11SC-693
    [12, 1, 1, 2, 2, 5],  # MSI GF63 Thin 11SC-693
    [12, 2, 1, 2, 2, 5],  # MSI GF63 Thin 11SC-693
    [12, 2, 1, 1, 1, 2],  # MSI GF63 Thin 11SC-693
    [12, 2, 1, 1, 1, 2],  # MSI GF63 Thin 11SC-693

    [12, 1, 1, 1, 2, 5],  # Laptop Dell Inspiron I5 11va
    [12, 1, 1, 1, 1, 4],  # Laptop Dell Inspiron I5 11va
    [12, 2, 1, 2, 2, 3],  # Laptop Dell Inspiron I5 11va
    [12, 2, 1, 2, 3, 1],  # Laptop Dell Inspiron I5 11va
    [12, 2, 1, 2, 3, 1],  # Laptop Dell Inspiron I5 11va

    [35, 2, 1, 3, 2, 5],  # Laptop Gamer Lenovo Legion 5 
    [35, 2, 1, 2, 2, 6],  # Laptop Gamer Lenovo Legion 5
    [35, 2, 1, 3, 2, 6],  # Laptop Gamer Lenovo Legion 5
    [35, 2, 1, 3, 2, 2],  # Laptop Gamer Lenovo Legion 5
    [35, 2, 1, 2, 2, 2],  # Laptop Gamer Lenovo Legion 5

    [16, 1, 1, 1, 2, 5],  # Laptop Lenovo V15
    [16, 2, 1, 2, 2, 1],  # Laptop Lenovo V15
    [16, 2, 1, 2, 1, 3],  # Laptop Lenovo V15
    [16, 1, 1, 1, 1, 3],  # Laptop Lenovo V15
    [16, 2, 1, 2, 2, 1],  # Laptop Lenovo V15

    [15, 2, 1, 2, 3, 1],  # HUAWEI Laptop Thin & Light MateBook D 16
    [15, 2, 1, 2, 3, 1],  # HUAWEI Laptop Thin & Light MateBook D 16
    [15, 2, 1, 2, 2, 3],  # HUAWEI Laptop Thin & Light MateBook D 16
    [15, 1, 1, 2, 2, 3],  # HUAWEI Laptop Thin & Light MateBook D 16
    [15, 2, 1, 1, 3, 3],  # HUAWEI Laptop Thin & Light MateBook D 16

    [16, 1, 1, 2, 2, 1],  # HP Portátil HD 
    [16, 2, 1, 1, 2, 1],  # HP Portátil HD 
    [16, 1, 1, 1, 3, 3],  # HP Portátil HD 
    [16, 1, 1, 2, 2, 3],  # HP Portátil HD 
    [16, 2, 1, 2, 2, 1],  # HP Portátil HD 

    [20, 1, 1, 2, 2, 4],  # MICROSOFT Surface Laptop 3 
    [20, 2, 1, 2, 2, 4],  # MICROSOFT Surface Laptop 3
    [20, 2, 1, 1, 1, 4],  # MICROSOFT Surface Laptop 3
    [20, 1, 1, 1, 1, 3],  # MICROSOFT Surface Laptop 3
    [20, 2, 1, 2, 2, 3],  # MICROSOFT Surface Laptop 3

    [24, 2, 1, 2, 2, 3],  # HP 7NZ97UA Intel Core i7-1065G7 
    [24, 2, 1, 2, 2, 3],  # HP 7NZ97UA Intel Core i7-1065G7
    [24, 2, 1, 2, 1, 3],  # HP 7NZ97UA Intel Core i7-1065G7
    [24, 1, 1, 1, 3, 4],  # HP 7NZ97UA Intel Core i7-1065G7
    [24, 2, 1, 2, 2, 4],  # HP 7NZ97UA Intel Core i7-1065G7

    [8, 1, 1, 1, 3, 1],  # Lenovo - Laptop Ideapad 3 i3
    [8, 1, 1, 1, 2, 1],  # Lenovo - Laptop Ideapad 3 i3
    [8, 1, 1, 1, 2, 1],  # Lenovo - Laptop Ideapad 3 i3
    [8, 1, 1, 1, 2, 3],  # Lenovo - Laptop Ideapad 3 i3
    [8, 1, 1, 1, 2, 3],  # Lenovo - Laptop Ideapad 3 i3

    [9, 1, 1, 2, 2, 1],  # HP Cuaderno Portátil 
    [9, 1, 1, 1, 2, 1],  # HP Cuaderno Portátil 
    [9, 1, 1, 1, 2, 1],  # HP Cuaderno Portátil 
    [9, 1, 1, 1, 2, 3],  # HP Cuaderno Portátil 
    [9, 1, 1, 2, 3, 3],  # HP Cuaderno Portátil 
    
    
    #Parte de Josue
    
    [15,1,1,2,2,1], #Acer Swift 3 14' 
    [15,2,1,2,1,3], #Acer Swift 3 14'
    [15,1,1,2,2,4], #Acer Swift 3 14'
    [15,2,1,2,1,3], #Acer Swift 3 14'
    [15,1,1,2,2,1], #Acer Swift 3 14'
    
    [15,2,1,3,1,2], #Ideapad Gaming 3i 6ta Gen
    [15,2,1,2,1,5], #Ideapad Gaming 3i 6ta Gen
    [15,2,1,2,1,2], #Ideapad Gaming 3i 6ta Gen
    [15,3,1,2,2,5], #Ideapad Gaming 3i 6ta Gen
    [15,2,1,2,1,6], #Ideapad Gaming 3i 6ta Gen
    
    [17,1,1,2,2,1], #Dell Inspiron 5510
    [17,2,1,1,2,3], #Dell Inspiron 5510
    [17,1,1,1,1,4], #Dell Inspiron 5510
    [17,2,1,1,1,1], #Dell Inspiron 5510
    [17,1,1,2,2,5], #Dell Inspiron 5510
    
    [13,2,1,2,1,2], #HP Victus 16
    [13,2,1,2,2,2], #HP Victus 16
    [13,2,1,2,1,5], #HP Victus 16
    [13,1,1,1,2,5], #HP Victus 16
    [13,2,1,2,1,6], #HP Victus 16
    
    [17,1,1,2,2,1], #HP Portátil FHD de 15.6 pulgadas, Intel i3-1215U
    [17,1,1,2,2,3], #HP Portátil FHD de 15.6 pulgadas, Intel i3-1215U
    [17,1,1,1,2,4], #HP Portátil FHD de 15.6 pulgadas, Intel i3-1215U
    [17,1,1,1,3,1], #HP Portátil FHD de 15.6 pulgadas, Intel i3-1215U
    [17,1,1,1,2,3], #HP Portátil FHD de 15.6 pulgadas, Intel i3-1215U
    
    [7,1,1,1,1,1], #Acer Laptop Aspire Lite 14"
    [7,1,1,1,1,3], #Acer Laptop Aspire Lite 14"
    [7,1,1,1,1,4], #Acer Laptop Aspire Lite 14"
    [7,1,1,1,2,1], #Acer Laptop Aspire Lite 14"
    [7,1,1,1,2,3], #Acer Laptop Aspire Lite 14"
    
    [7,1,1,1,1,1], #Laptop Lenovo V14 G3 14"
    [7,1,1,1,1,3], #Laptop Lenovo V14 G3 14"
    [7,1,1,1,1,4], #Laptop Lenovo V14 G3 14"
    [7,1,1,1,2,1], #Laptop Lenovo V14 G3 14"
    [7,1,1,1,2,3], #Laptop Lenovo V14 G3 14"
    
    [8,1,1,1,2,1], #Notebook Asus Vivobook Intel Core I3 14"
    [8,1,1,1,1,3], #Notebook Asus Vivobook Intel Core I3 14"
    [8,1,1,1,1,4], #Notebook Asus Vivobook Intel Core I3 14"
    [8,1,1,1,2,1], #Notebook Asus Vivobook Intel Core I3 14"
    [8,1,1,1,1,3], #Notebook Asus Vivobook Intel Core I3 14"
   
    [19,1,1,2,2,1], #ASUS - Laptop FHD de 17,3 pulgadas
    [19,1,1,2,1,3], #ASUS - Laptop FHD de 17,3 pulgadas
    [19,1,1,2,1,4], #ASUS - Laptop FHD de 17,3 pulgadas
    [19,1,1,2,2,1], #ASUS - Laptop FHD de 17,3 pulgadas
    [19,1,1,2,2,3], #ASUS - Laptop FHD de 17,3 pulgadas
    
    
    [12,3,1,2,2,1], #acer Swift 3 Intel EVO Thin & Light Laptop | 14" FHD 100% sRGB 
    [12,3,1,2,2,3], #acer Swift 3 Intel EVO Thin & L ight Laptop | 14" FHD 100% sRGB 
    [12,3,1,3,1,4], #acer Swift 3 Intel EVO Thin & Light Laptop | 14" FHD 100% sRGB 
    [12,2,1,1,2,1], #acer Swift 3 Intel EVO Thin & Light Laptop | 14" FHD 100% sRGB 
    [12,2,1,2,2,4], #acer Swift 3 Intel EVO Thin & Light Laptop | 14" FHD 100% sRGB 
    
    [8,1,1,1,2,1], #Acer Laptop Aspire Lite 14 Core i5 1235U 512 GB SSD
    [8,1,1,2,3,3], #Acer Laptop Aspire Lite 14 Core i5 1235U 512 GB SSD
    [8,1,1,1,2,4], #Acer Laptop Aspire Lite 14 Core i5 1235U 512 GB SSD
    [8,1,1,2,2,1], #Acer Laptop Aspire Lite 14 Core i5 1235U 512 GB SSD
    [8,1,1,1,2,3], #Acer Laptop Aspire Lite 14 Core i5 1235U 512 GB SSD
    
    [15,1,1,2,1,3], #Laptop Lenovo V14 G3 IAP 14" 1920x1080 Full HD
    [15,1,1,1,1,4], #Laptop Lenovo V14 G3 IAP 14" 1920x1080 Full HD
    [15,2,1,2,2,1], #Laptop Lenovo V14 G3 IAP 14" 1920x1080 Full HD
    [15,1,1,1,1,3], #Laptop Lenovo V14 G3 IAP 14" 1920x1080 Full HD
    [15,1,1,2,1,4], #Laptop Lenovo V14 G3 IAP 14" 1920x1080 Full HD
    
    [19,2,1,2,2,3], #Laptop Lenovo Thinkpad L14
    [19,2,1,2,1,5], #Laptop Lenovo Thinkpad L14
    [19,2,1,2,2,3], #Laptop Lenovo Thinkpad L14
    [19,2,1,2,2,5], #Laptop Lenovo Thinkpad L14
    [19,2,1,1,3,5], #Laptop Lenovo Thinkpad L14
    
    [36,2,1,3,2,3], #Lenovo ThinkPad X1 Carbon Gen 10 Intel Core i7-1280P
    [36,2,1,2,2,5], #Lenovo ThinkPad X1 Carbon Gen 10 Intel Core i7-1280P
    [36,2,1,3,3,3], #Lenovo ThinkPad X1 Carbon Gen 10 Intel Core i7-1280P
    [36,2,1,2,1,5], #Lenovo ThinkPad X1 Carbon Gen 10 Intel Core i7-1280P
    [36,2,1,2,2,5], #Lenovo ThinkPad X1 Carbon Gen 10 Intel Core i7-1280P
    
    [15,1,1,2,1,3], #Laptop Dell Latitude 5330 Core I7 1265u
    [15,1,1,2,1,4], #Laptop Dell Latitude 5330 Core I7 1265u
    [15,1,1,2,2,3], #Laptop Dell Latitude 5330 Core I7 1265u
    [15,2,1,1,1,4], #Laptop Dell Latitude 5330 Core I7 1265u
    [15,1,1,2,1,3], #Laptop Dell Latitude 5330 Core I7 1265u
    
    [14,1,1,2,1,3], #ASUS Laptop Vivobook 14/X1404ZA-NK100W/Intel Core i7-1255U
    [14,1,1,2,2,4], #ASUS Laptop Vivobook 14/X1404ZA-NK100W/Intel Core i7-1255U
    [14,2,1,2,1,3], #ASUS Laptop Vivobook 14/X1404ZA-NK100W/Intel Core i7-1255U
    [14,1,1,1,2,4], #ASUS Laptop Vivobook 14/X1404ZA-NK100W/Intel Core i7-1255U
    [14,1,1,2,1,3], #ASUS Laptop Vivobook 14/X1404ZA-NK100W/Intel Core i7-1255U
    
    [17,1,1,2,1,3], #DELL Laptop Inspiron 3520 15.6 FHD Core i7-1255U
    [17,1,1,2,1,3], #DELL Laptop Inspiron 3520 15.6 FHD Core i7-1255U
    [17,1,1,2,2,3], #DELL Laptop Inspiron 3520 15.6 FHD Core i7-1255U
    [17,1,1,1,2,3], #DELL Laptop Inspiron 3520 15.6 FHD Core i7-1255U
    [17,1,1,2,1,3], #DELL Laptop Inspiron 3520 15.6 FHD Core i7-1255U
    
    [18,2,1,2,1,2], #Acer Laptop Gaming Nitro 5 Modelo 2024 Core i5 12th
    [18,2,1,2,1,2], #Acer Laptop Gaming Nitro 5 Modelo 2024 Core i5 12th
    [18,1,1,2,2,2], #Acer Laptop Gaming Nitro 5 Modelo 2024 Core i5 12th
    [18,2,1,2,1,5], #Acer Laptop Gaming Nitro 5 Modelo 2024 Core i5 12th
    [18,2,1,2,1,5], #Acer Laptop Gaming Nitro 5 Modelo 2024 Core i5 12th
    
    [11,1,1,2,1,1], #Laptop Lenovo IdeaPad Slim 3 15IAH8 15.6"
    [11,1,1,1,1,3], #Laptop Lenovo IdeaPad Slim 3 15IAH8 15.6"
    [11,1,1,2,2,3], #Laptop Lenovo IdeaPad Slim 3 15IAH8 15.6"
    [11,1,1,2,1,4], #Laptop Lenovo IdeaPad Slim 3 15IAH8 15.6"
    [11,1,1,2,1,4], #Laptop Lenovo IdeaPad Slim 3 15IAH8 15.6"
    
    [17,2,1,2,1,2], #HP Victus 15.6 i5 - Laptop para juegos, pantalla de 15.6
    [17,2,1,3,1,2], #HP Victus 15.6 i5 - Laptop para juegos, pantalla de 15.6
    [17,2,1,2,2,5], #HP Victus 15.6 i5 - Laptop para juegos, pantalla de 15.6
    [17,2,1,3,1,5], #HP Victus 15.6 i5 - Laptop para juegos, pantalla de 15.6
    [17,2,1,3,1,6], #HP Victus 15.6 i5 - Laptop para juegos, pantalla de 15.6
    
    [20,2,1,2,1,2], #Bundle Laptop Gamer Asus Tuf F15 Intel Core i5 15.6
    [20,2,1,3,1,2], #Bundle Laptop Gamer Asus Tuf F15 Intel Core i5 15.6
    [20,2,1,2,2,5], #Bundle Laptop Gamer Asus Tuf F15 Intel Core i5 15.6
    [20,2,1,3,1,5], #Bundle Laptop Gamer Asus Tuf F15 Intel Core i5 15.6
    [20,2,1,2,1,6], #Bundle Laptop Gamer Asus Tuf F15 Intel Core i5 15.6
    
    [23,2,1,3,1,2], #Laptop Gamer Gigabyte Notebook Aorus 15 9mf Core I5 
    [23,2,1,3,1,2], #Laptop Gamer Gigabyte Notebook Aorus 15 9mf Core I5 
    [23,2,1,3,2,5], #Laptop Gamer Gigabyte Notebook Aorus 15 9mf Core I5 
    [23,2,1,3,1,5], #Laptop Gamer Gigabyte Notebook Aorus 15 9mf Core I5 
    [23,2,1,3,1,6], #Laptop Gamer Gigabyte Notebook Aorus 15 9mf Core I5 
    
    [20,2,1,3,1,2], #Acer Nitro 5 AN515-58-527S Gaming Laptop 
    [20,2,1,3,1,2], #Acer Nitro 5 AN515-58-527S Gaming Laptop 
    [20,2,1,3,1,5], #Acer Nitro 5 AN515-58-527S Gaming Laptop 
    [20,2,1,3,1,6], #Acer Nitro 5 AN515-58-527S Gaming Laptop 
    [20,2,1,3,1,6], #Acer Nitro 5 AN515-58-527S Gaming Laptop 
    
    [28,2,1,2,1,2], #Laptop Asus TUF Gaming FX507ZC4-HN002W
    [28,2,1,3,1,2], #Laptop Asus TUF Gaming FX507ZC4-HN002W
    [28,2,1,2,1,5], #Laptop Asus TUF Gaming FX507ZC4-HN002W
    [28,3,1,3,2,5], #Laptop Asus TUF Gaming FX507ZC4-HN002W
    [28,2,1,2,1,6], #Laptop Asus TUF Gaming FX507ZC4-HN002W
    
    [20,3,1,2,1,2], #Laptop Lenovo LOQ NB LOQ 15IAX9 CI5 Gen 12th
    [20,3,1,3,1,2], #Laptop Lenovo LOQ NB LOQ 15IAX9 CI5 Gen 12th
    [20,3,1,2,1,5], #Laptop Lenovo LOQ NB LOQ 15IAX9 CI5 Gen 12th
    [20,3,1,3,1,5], #Laptop Lenovo LOQ NB LOQ 15IAX9 CI5 Gen 12th
    [20,3,1,3,1,6], #Laptop Lenovo LOQ NB LOQ 15IAX9 CI5 Gen 12th
    
    
    #AMD SECTION
    
    [11,1,1,1,1,1], #ASUS Laptop Vivobook Go 14/E1404FA-NK480W/AMD
    [11,1,1,2,1,1], #ASUS Laptop Vivobook Go 14/E1404FA-NK480W/AMD
    [11,1,1,1,1,3], #ASUS Laptop Vivobook Go 14/E1404FA-NK480W/AMD
    [11,1,1,1,2,4], #ASUS Laptop Vivobook Go 14/E1404FA-NK480W/AMD
    [11,1,1,2,2,4], #ASUS Laptop Vivobook Go 14/E1404FA-NK480W/AMD
    
    
    [30,2,1,2,1,2], #Laptop Gamer Legion 5 15.6 pulgadas Full HD GeForce RTX 2060 AMD Ryzen 5
    [30,2,1,3,1,2], #Laptop Gamer Legion 5 15.6 pulgadas Full HD GeForce RTX 2060 AMD Ryzen 5
    [30,2,1,2,1,5], #Laptop Gamer Legion 5 15.6 pulgadas Full HD GeForce RTX 2060 AMD Ryzen 5
    [30,2,1,3,1,2], #Laptop Gamer Legion 5 15.6 pulgadas Full HD GeForce RTX 2060 AMD Ryzen 5
    [30,2,1,2,1,6], #Laptop Gamer Legion 5 15.6 pulgadas Full HD GeForce RTX 2060 AMD Ryzen 5
    
    [17,1,1,2,2,4], #HP 255 G10 15.6" FHD Business Laptop, AMD Ryzen 7 7730U
    [17,1,1,2,2,3], #HP 255 G10 15.6" FHD Business Laptop, AMD Ryzen 7 7730U
    [17,1,1,2,2,3], #HP 255 G10 15.6" FHD Business Laptop, AMD Ryzen 7 7730U
    [17,1,1,1,2,3], #HP 255 G10 15.6" FHD Business Laptop, AMD Ryzen 7 7730U
    [17,1,1,2,3,4], #HP 255 G10 15.6" FHD Business Laptop, AMD Ryzen 7 7730U
    
    [9,2,1,2,1,1], #Laptop Dell Inspiron 3525 Ryzen 5 8gb 512ssd Win11 Plata
    [9,2,1,2,2,1], #Laptop Dell Inspiron 3525 Ryzen 5 8gb 512ssd Win11 Plata
    [9,2,1,2,1,1], #Laptop Dell Inspiron 3525 Ryzen 5 8gb 512ssd Win11 Plata
    [9,1,1,2,1,4], #Laptop Dell Inspiron 3525 Ryzen 5 8gb 512ssd Win11 Plata
    [9,1,1,1,2,4], #Laptop Dell Inspiron 3525 Ryzen 5 8gb 512ssd Win11 Plata

#Parte de Rafa

    [23, 3, 2, 4, 3, 3], #MacBook Air 13" M3
    [23, 3, 2, 4, 3, 3], #MacBook Air 13" M3
    [23, 3, 2, 4, 3, 4], #MacBook Air 13" M3
    [23, 3, 2, 4, 3, 4], #MacBook Air 13" M3
    [23, 2, 2, 4, 3, 4], #MacBook Air 13" M3

    [16, 3, 2, 3, 3, 3], #MacBook Air 13" M1
    [16, 3, 2, 3, 3, 3], #MacBook Air 13" M1
    [16, 2, 2, 3, 2, 5], #MacBook Air 13" M1
    [16, 2, 2, 3, 3, 5], #MacBook Air 13" M1
    [16, 3, 2, 3, 3, 5], #MacBook Air 13" M1

    [100, 4, 2, 4, 3, 6], #MacBook Pro M4 MAX
    [100, 4, 2, 4, 3, 6], #MacBook Pro M4 MAX
    [100, 4, 2, 4, 3, 7], #MacBook Pro M4 MAX
    [100, 4, 2, 4, 3, 7], #MacBook Pro M4 MAX
    [100, 4, 2, 4, 3, 6], #MacBook Pro M4 MAX

    [21, 3, 2, 2, 2, 5], #MacBook Air 13" M2 16 gb ram
    [21, 3, 2, 2, 3, 5], #MacBook Air 13" M2 16 gb ram
    [21, 3, 2, 3, 2, 3], #MacBook Air 13" M2 16 gb ram
    [21, 3, 2, 3, 2, 6], #MacBook Air 13" M2 16 gb ram
    [21, 3, 2, 3, 2, 3], #MacBook Air 13" M2 16 gb ram

    [25, 3, 2, 3, 2, 7], #MacBook Air 13" M2 8 gb ram
    [25, 3, 2, 3, 2, 5], #MacBook Air 13" M2 8 gb ram
    [25, 3, 2, 3, 2, 6], #MacBook Air 13" M2 8 gb ram
    [25, 3, 2, 2, 2, 5], #MacBook Air 13" M2 8 gb ram
    [25, 3, 2, 2, 3, 6], #MacBook Air 13" M2 8 gb ram

    [26, 3, 1, 3, 2, 5], #ASUS TUF A15
    [26, 3, 1, 3, 2, 1], #ASUS TUF A15
    [26, 3, 1, 3, 2, 5], #ASUS TUF A15
    [26, 3, 1, 3, 2, 6], #ASUS TUF A15
    [26, 3, 1, 3, 3, 6], #ASUS TUF A15

    [9, 2, 1, 2, 2, 1], #Dell Inspiron
    [9, 2, 1, 2, 3, 3], #Dell Inspiron
    [9, 2, 1, 2, 2, 1], #Dell Inspiron
    [9, 2, 1, 2, 2, 3], #Dell Inspiron
    [9, 2, 1, 2, 2, 4], #Dell Inspiron

    [13, 2, 1, 2, 2, 1], #HP Victus
    [13, 2, 1, 2, 2, 3], #HP Victus
    [13, 2, 1, 2, 2, 4], #HP Victus
    [13, 2, 1, 2, 2, 1], #HP Victus
    [13, 3, 1, 2, 2, 3], #HP Victus

    [15, 2, 1, 2, 3, 1], #Lenovo Notebook
    [15, 2, 1, 2, 2, 3], #Lenovo Notebook
    [15, 3, 1, 2, 2, 2], #Lenovo Notebook
    [15, 2, 1, 2, 2, 3], #Lenovo Notebook
    [15, 3, 1, 2, 2, 2], #Lenovo Notebook

    [16, 3, 1, 2, 3, 2], #ASUS Vivobook
    [16, 3, 1, 2, 2, 3], #ASUS Vivobook
    [16, 3, 1, 1, 2, 4], #ASUS Vivobook
    [16, 1, 1, 2, 3, 3], #ASUS Vivobook
    [16, 2, 1, 2, 2, 4], #ASUS Vivobook

    [11, 2, 1, 2, 2, 1], #Lenovo IdeaPad 3
    [11, 1, 1, 2, 3, 3], #Lenovo IdeaPad 3
    [11, 1, 1, 1, 2, 4], #Lenovo IdeaPad 3
    [11, 2, 1, 1, 3, 3], #Lenovo IdeaPad 3
    [11, 2, 1, 2, 2, 4], #Lenovo IdeaPad 3

    [9, 1, 1, 2, 2, 1], #Lenovo IdeaPad 1
    [9, 1, 1, 2, 2, 3], #Lenovo IdeaPad 1
    [9, 1, 1, 1, 3, 2], #Lenovo IdeaPad 1
    [9, 1, 1, 1, 2, 3], #Lenovo IdeaPad 1
    [9, 2, 1, 2, 3, 2], #Lenovo IdeaPad 1

    [40, 3, 1, 4, 2, 2], #Lenovo Legion Slim 5
    [40, 3, 1, 3, 3, 6], #Lenovo Legion Slim 5
    [40, 3, 1, 3, 2, 7], #Lenovo Legion Slim 5
    [40, 3, 1, 3, 3, 6], #Lenovo Legion Slim 5
    [40, 3, 1, 3, 3, 7], #Lenovo Legion Slim 5

    [40, 3, 1, 4, 3, 2], #Lenovo Legion 5 Pro
    [40, 3, 1, 5, 3, 5], #Lenovo Legion 5 Pro
    [40, 3, 1, 4, 3, 6], #Lenovo Legion 5 Pro
    [40, 3, 1, 4, 3, 5], #Lenovo Legion 5 Pro
    [40, 3, 1, 4, 3, 6], #Lenovo Legion 5 Pro

    [23, 3, 1, 3, 3, 7], #Lenovo LOQ
    [23, 3, 1, 3, 3, 7], #Lenovo LOQ
    [23, 3, 1, 2, 2, 6], #Lenovo LOQ
    [23, 3, 1, 3, 2, 6], #Lenovo LOQ
    [23, 2, 1, 3, 3, 5], #Lenovo LOQ

    [20, 2, 1, 3, 3, 7], #Dell G15
    [20, 2, 1, 3, 2, 5], #Dell G15
    [20, 1, 1, 2, 2, 5], #Dell G15
    [20, 1, 1, 2, 2, 2], #Dell G15
    [20, 2, 1, 3, 2, 5], #Dell G15

    [20, 3, 1, 3, 3, 5], #HP OMEN
    [20, 3, 1, 3, 2, 5], #HP OMEN
    [20, 3, 1, 3, 2, 7], #HP OMEN
    [20, 3, 1, 3, 2, 6], #HP OMEN
    [20, 3, 1, 3, 2, 7], #HP OMEN

])

etiquetas = np.array([
    0,0,0,0,0,
    1,1,1,1,1,
    2,2,2,2,2,
    3,3,3,3,3,
    4,4,4,4,4,
    5,5,5,5,5,
    6,6,6,6,6,
    7,7,7,7,7,
    8,8,8,8,8,
    9,9,9,9,9,
    10,10,10,10,10,
    11,11,11,11,11,
    12,12,12,12,12,
    13,13,13,13,13,
    14,14,14,14,14,
    15,15,15,15,15,
    16,16,16,16,16,
    17,17,17,17,17,
    18,18,18,18,18,
    19,19,19,19,19,
    20,20,20,20,20,
    21,21,21,21,21,
    22,22,22,22,22,
    23,23,23,23,23,
    24,24,24,24,24,
    25,25,25,25,25,
    26,26,26,26,26,
    27,27,27,27,27,
    28,28,28,28,28,
    29,29,29,29,29,
    30,30,30,30,30,
    31,31,31,31,31,
    32,32,32,32,32,
    33,33,33,33,33,
    34,34,34,34,34,
    35,35,35,35,35,
    36,36,36,36,36,
    37,37,37,37,37,
    38,38,38,38,38,
    39,39,39,39,39,
    40,40,40,40,40,
    41,41,41,41,41,
    42,42,42,42,42,
    43,43,43,43,43,
    44,44,44,44,44,
    45,45,45,45,45,
    46,46,46,46,46,
    47,47,47,47,47,
    48,48,48,48,48,
    49,49,49,49,49,
    50,50,50,50,50,
    51,51,51,51,51,
    52,52,52,52,52,
    53,53,53,53,53,
    54,54,54,54,54,
    55,55,55,55,55,
    56,56,56,56,56,
    57,57,57,57,57,
    58,58,58,58,58,
    59,59,59,59,59,
    60,60,60,60,60,
    61,61,61,61,61,
    62,62,62,62,62,
    63,63,63,63,63,
    64,64,64,64,64,
    65,65,65,65,65,
    66,66,66,66,66,
    67,67,67,67,67,
    68,68,68,68,68,
    69,69,69,69,69,
    70,70,70,70,70,
    71,71,71,71,71,
    72,72,72,73,72,

    ])