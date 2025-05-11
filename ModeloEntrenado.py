import numpy as np
import joblib

modelo_yaentrenado = joblib.load('modBayes_fit.pkl')
nueva_pc = np.array([[15, 2, 1, 2, 2, 1]])  # uso

nueva_prediccion = modelo_yaentrenado.predict(nueva_pc) 


categorias = {
0: "Lenovo IdeaPad 3",
1: "Laptop Lenovo 81Y4001HUS", 
2: "Acer Predator Helios 300", 
3: "Acer Predator Helios 300 PH315-54-760S", 
4: "Laptop Lenovo IdeaPad Gaming 3i",
5: "Laptop MSI GF63 Thin 10SCSR",
6: "Laptop MSI Gamer Cyborg 15",
7: "Laptop HP Envy",
8: "Laptop HP 240 G10",
9: "Laptop HP 240 G8",
10: "ThinkPad L13 Yoga Gen 2",
11: "Laptop ASUS Vivobook 14 ",
12: "DELL Latitude 7420", 
13: "ACER Laptop Aspire 5", 
14: "Acer Nitro 5 AN515-55-53E5 Laptop Gaming",
15: "Laptop Gaming Msi Gf75 Thin 10scrx ",
16: "ASUS Laptop Vivobook 14/14",
17: "MSI GF63 Thin 11SC-693",
18: "Laptop Dell Inspiron I5 11va", 
19: "Laptop Gamer Lenovo Legion 5 ",
20: "Laptop Lenovo V15",
21: "HUAWEI Laptop Thin & Light MateBook D 16",
22: "HP Portátil HD",
23: "MICROSOFT Surface Laptop 3",
24: "HP 7NZ97UA Intel Core i7-1065G7",
25: "Lenovo - Laptop Ideapad 3 i3",
26: "HP Cuaderno Portátil ",

#Parte de Josue -------------

27: 'Acer Swift 3 14',
28:'Ideapad Gaming 3i 6ta Gen',
29:'Dell Inspiron 5510',
30:'HP Victus 16',
31:'HP Portátil FHD de 15.6 pulgadas, Intel i3-1215U',
32:'Acer Laptop Aspire Lite 14"',
33:'Laptop Lenovo V14 G3 14"',
34:'Notebook Asus Vivobook Intel Core I3 14"',
35:'ASUS - Laptop FHD de 17,3 pulgadas',
36:'acer Swift 3 Intel EVO Thin & Light Laptop | 14" FHD 100 sRGB ',
37:'Acer Laptop Aspire Lite 14 Core i5 1235U 512 GB SSD',
38:'Laptop Lenovo V14 G3 IAP 14" 1920x1080 Full HD',
39:'Laptop Lenovo Thinkpad L14',
40:'Lenovo ThinkPad X1 Carbon Gen 10 Intel Core i7-1280P',
41:'Laptop Dell Latitude 5330 Core I7 1265u',
42:'ASUS Laptop Vivobook 14/X1404ZA-NK100W/Intel Core i7-1255U',
43:'DELL Laptop Inspiron 3520 15.6 FHD Core i7-1255U',
44:'Acer Laptop Gaming Nitro 5 Modelo 2024 Core i5 12th',
45:'Laptop Lenovo IdeaPad Slim 3 15IAH8 15.6"',
46:'HP Victus 15.6 i5 - Laptop para juegos, pantalla de 15.6',
47:'#Bundle Laptop Gamer Asus Tuf F15 Intel Core i5 15.6',
48:'Laptop Gamer Gigabyte Notebook Aorus 15 9mf Core I5 ',
49:'Acer Nitro 5 AN515-58-527S Gaming Laptop',
50:'Laptop Asus TUF Gaming FX507ZC4-HN002W',
51:'Laptop Lenovo LOQ NB LOQ 15IAX9 CI5 Gen 12th',

#AMD
52:'ASUS Laptop Vivobook Go 14/E1404FA-NK480W/AMD',
53:'Laptop Gamer Legion 5 15.6 pulgadas Full HD GeForce RTX 2060 AMD Ryzen 5',
54:'HP 255 G10 15.6" FHD Business Laptop, AMD Ryzen 7 7730U',
55:'Laptop Dell Inspiron 3525 Ryzen 5 8gb 512ssd Win11 Plata' ,

#Parte de Rafa -------------
56: 'MacBook Air 13" M3',
57: 'MacBook Air 13" M1',
58: 'MacBook Pro M4 MAX',
59: 'MacBook Air 13" M2 16 gb ram',
60: 'MacBook Air 13" M2 8 gb ram',
61: 'ASUS TUF A15',
62: 'Dell Inspiron',
63: 'HP Victus',
64: 'Lenovo Notebook',
65: 'ASUS Vivobook',
66: 'Lenovo IdeaPad 3',
67: 'Lenovo IdeaPad 1',
68: 'Lenovo Legion Slim 5',
69: 'Lenovo Legion 5 Pro',
70: 'Lenovo LOQ',
71: 'Dell G15',
72: 'HP OMEN',
73: 'Acer Aspire',
74: 'Lenovo IdeaPad 5',
75: 'Lenovo V14',
}

print(f"La computadora probablemente es: {categorias[nueva_prediccion[0]]}")

def realizar_prediccion(nuevoarr):
    nueva_pc = np.array([nuevoarr])
    nueva_prediccion = modelo_yaentrenado.predict(nueva_pc) 
    print(f"La computadora probablemente es: {categorias[nueva_prediccion[0]]}")
    return nueva_prediccion[0], categorias[nueva_prediccion[0]]