import sys
import ModeloEntrenado
import EspecificacionesComputadora
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSlider, QComboBox, QPushButton, QHBoxLayout, QSizePolicy,QDialog, QTableWidget, QTableWidgetItem,QAbstractItemView
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPixmap


class InterfazBayes(QWidget):
    def __init__(self):
        super().__init__()
        self.indexCompu = 100
        self.Rec = "Nada que mostrar"
        self.setWindowTitle("Bayes IA")
        self.setGeometry(100, 100, 800, 600)  

        # Layout principal
        layout_principal = QVBoxLayout()

        # ===========================
        # SECCION: ENCABEZADO 
        # ===========================
        
        label_encabezado = QLabel()

        pixmap = QPixmap("Icons/LogoBayes")  # Imagen 
        label_encabezado.setPixmap(pixmap)

        label_encabezado.setText("<table><tr><td><img src='Icons/LogoBayes.png' height='60'></td><td><b style='font-size:39px; color:white;'>ComputeLeaRN</b></td></tr></table>")

        label_encabezado.setStyleSheet("background-color: #77afc1; padding: 5px;")
        label_encabezado.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_encabezado.setFixedHeight(85)

        layout_principal.addWidget(label_encabezado)

        # ===========================
        # SECCION: SUBENCABEZADO 
        # ===========================
        subencabezado_widget = QWidget()
        subencabezado_layout = QVBoxLayout()
        subencabezado_widget.setLayout(subencabezado_layout)

        texto_subencabezado = QLabel("Esta es una herramienta que usa IA basada en el teorema de Bayes, el objetivo de esta herramienta es brindar sugerencias a personas sobre qué computadora portátil es ideal según sus necesidades.\n\n"
                                     "Instrucciones: Seleccione una opción por campo. Cuando finalice la selección en todos los campos, presione el botón de procesar para obtener resultados.")
        texto_subencabezado.setWordWrap(True)
        texto_subencabezado.setAlignment(Qt.AlignmentFlag.AlignLeft)
        subencabezado_layout.addWidget(texto_subencabezado)
        texto_subencabezado.setFixedHeight(100)
        texto_subencabezado.setStyleSheet(" font-size: 15px;")
        layout_principal.addWidget(subencabezado_widget)

        # ===========================
        # SECCION: CUERPO 
        # ===========================
        cuerpo_widget = QWidget()
        cuerpo_layout = QVBoxLayout()
        cuerpo_widget.setLayout(cuerpo_layout)
        cuerpo_widget.setStyleSheet("background-color: #efedb5; color: black;padding: 10px;") 

        # Primera fila: barras deslizables + campo desplegable
        fila1_layout = QHBoxLayout()

        # Barra 1 con nivel debajo
        barra1_layout = QVBoxLayout()
        barra1_label = QLabel("Presupuesto Maximo")
        barra1 = QSlider(Qt.Orientation.Horizontal)
        barra1.setMinimum(8)
        barra1.setMaximum(36)
        nivel1_label = QLabel("Valor en MXN: 8000")
        barra1.valueChanged.connect(lambda value: nivel1_label.setText(f"Valor en MXN: {value*1000}"))
        barra1_layout.addWidget(barra1_label)
        barra1_layout.addWidget(barra1)
        barra1_layout.addWidget(nivel1_label)

        # Barra 2 con nivel debajo
        barra2_layout = QVBoxLayout()
        barra2_label = QLabel("Calidad de Video")
        barra2 = QSlider(Qt.Orientation.Horizontal)
        barra2.setMinimum(1)
        barra2.setMaximum(4)
        nivel2_label = QLabel("Nivel de Calidad: 1")
        barra2.valueChanged.connect(lambda value: nivel2_label.setText(f"Nivel de Calidad: {value}"))
        barra2_layout.addWidget(barra2_label)
        barra2_layout.addWidget(barra2)
        barra2_layout.addWidget(nivel2_label)

        # Campo desplegable (Sistema Operativo)
        campo_label = QLabel("Sistema Operativo")
        campo_desplegable = QComboBox()
        campo_desplegable.addItem(QIcon("Icons/w.png"),"Windows")
        campo_desplegable.addItem(QIcon("Icons/A.png"),"Mac OS")

        fila1_layout.addLayout(barra1_layout)
        fila1_layout.addLayout(barra2_layout)
        fila1_layout.addWidget(campo_label)
        fila1_layout.addWidget(campo_desplegable)

        cuerpo_layout.addLayout(fila1_layout)

        # Segunda fila: barras deslizables + campo desplegable (Uso)
        fila2_layout = QHBoxLayout()

        # Barra 3 con nivel debajo
        barra3_layout = QVBoxLayout()
        barra3_label = QLabel("Nivel de Rendimiento")
        barra3 = QSlider(Qt.Orientation.Horizontal)
        barra3.setMinimum(1)
        barra3.setMaximum(5)
        nivel3_label = QLabel("Nivel de Rendimiento: 1")
        barra3.valueChanged.connect(lambda value: nivel3_label.setText(f"Nivel de Rendimiento: {value}"))
        barra3_layout.addWidget(barra3_label)
        barra3_layout.addWidget(barra3)
        barra3_layout.addWidget(nivel3_label)

        # Barra 4 con nivel debajo
        barra4_layout = QVBoxLayout()
        barra4_label = QLabel("Rendimiento de la Bateria")
        barra4 = QSlider(Qt.Orientation.Horizontal)
        barra4.setMinimum(1)
        barra4.setMaximum(3)
        nivel4_label = QLabel("Nivel de Bateria: 1")
        barra4.valueChanged.connect(lambda value: nivel4_label.setText(f"Nivel de Bateria: {value}"))
        barra4_layout.addWidget(barra4_label)
        barra4_layout.addWidget(barra4)
        barra4_layout.addWidget(nivel4_label)

        # Campo desplegable (Uso requerido)
        campo2_label = QLabel("Uso Requerido")
        campo2_desplegable = QComboBox()
        campo2_desplegable.addItem(QIcon("Icons/Esco.png"), "Escolar")#1
        campo2_desplegable.addItem(QIcon("Icons/Game.png"), "Gamer")#3
        campo2_desplegable.addItem(QIcon("Icons/Ofice.png"), "Oficina")#1
        campo2_desplegable.addItem(QIcon("Icons/Hogar.png"), "Diario")#2
        campo2_desplegable.addItem(QIcon("Icons/Inge.png"), "Ingenieria")#2
        campo2_desplegable.addItem(QIcon("Icons/Edic.png"), "Diseño y Edicion")#3
        campo2_desplegable.addItem(QIcon("Icons/Model.png"), "Modelado 3D")#4

        fila2_layout.addLayout(barra3_layout)
        fila2_layout.addLayout(barra4_layout)
        fila2_layout.addWidget(campo2_label)
        fila2_layout.addWidget(campo2_desplegable)

        cuerpo_layout.addLayout(fila2_layout)
        layout_principal.addWidget(cuerpo_widget)

        

        # ===========================
        # SECCION: RESULTADOS
        # ===========================
        layout_botones = QHBoxLayout()
        boton1 = QPushButton("   Procesar Datos")
        boton2 = QPushButton("   Ver Resultado")
        self.configurar_icono_boton(boton1, "Icons/IA.png")
        self.configurar_icono_boton(boton2, "Icons/Lap.png")

        layout_botones.addWidget(boton1)
        layout_botones.addWidget(boton2)
        layout_principal.addLayout(layout_botones)

        self.setLayout(layout_principal)

        boton1.clicked.connect(lambda: self.obtener_valores(barra1,barra2,campo_desplegable,barra3,barra4,campo2_desplegable))
        boton2.clicked.connect(self.mostrar_Tabla_Resultado)

    def obtener_valores(self, dinero, video, SO, Rendimiento, bateria, Uso):
        dineroarr = dinero.value()
        videoarr = video.value()
        SOarr = (SO.currentIndex())+1
        Rendimientoarr = Rendimiento.value()
        bateriaarr = bateria.value()
        usoarr = (Uso.currentIndex())+1

        arrCarac = [dineroarr,videoarr,SOarr,Rendimientoarr,bateriaarr,usoarr]

        self.indexCompu, self.Rec = ModeloEntrenado.realizar_prediccion(arrCarac)
        self.mostrar_Tabla_Resultado()

    def mostrar_Tabla_Resultado(self):

        # Crear ventana para mostrar los procesos reintentados
        ventana_reintentos = QDialog(self)
        ventana_reintentos.setWindowTitle("Tabla De Recursos")
        ventana_reintentos.setGeometry(150, 150, 400, 300)
        link_url =  EspecificacionesComputadora.Especificaciones[self.indexCompu][5]
        
        link = QLabel(f"<a href='{link_url}'>Visitar sitio</a>", self)
        link.setTextFormat(Qt.TextFormat.RichText)  # Permite interpretar HTML
        link.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)  # Permite hacer clic
        link.setOpenExternalLinks(True)

        layout = QVBoxLayout()
        label0 = QLabel("Resultados Obtenidos del Modelo")
        label0.setStyleSheet("background-color: #77afc1; color: white; font-size:15; font-weight: bold; padding: 5px;")
        label = QLabel(self.Rec)
        label1 = QLabel("Recuerda que esto es solo una sugerencia, en caso de desacuerdo, intenta con otros parametros")
 
        #tablita
        tabla = QTableWidget()
        tabla.setRowCount(5)
        tabla.setColumnCount(2)
        tabla.setHorizontalHeaderLabels(["Componente", "Especificacion"])

        tabla.setColumnWidth(0, 195)  # Ancho de la columna 0 (en píxeles)
        tabla.setColumnWidth(1, 195)  # Ancho de la columna 1

        nuevo_item = QTableWidgetItem('Procesador')
        tabla.setItem(0, 0, nuevo_item)
        nuevo_item1 = QTableWidgetItem('RAM')
        tabla.setItem(1, 0, nuevo_item1)
        nuevo_item2 = QTableWidgetItem('Almacenamiento')
        tabla.setItem(2, 0, nuevo_item2)
        nuevo_item3 = QTableWidgetItem('Tarjeta Grafica')
        tabla.setItem(3, 0, nuevo_item3)
        nuevo_item4 = QTableWidgetItem('Precio aproximado')
        tabla.setItem(4, 0, nuevo_item4)

        nuevo_item = QTableWidgetItem(EspecificacionesComputadora.Especificaciones[self.indexCompu][0])
        tabla.setItem(0, 1, nuevo_item)
        nuevo_item1 = QTableWidgetItem(EspecificacionesComputadora.Especificaciones[self.indexCompu][1])
        tabla.setItem(1, 1, nuevo_item1)
        nuevo_item2 = QTableWidgetItem(EspecificacionesComputadora.Especificaciones[self.indexCompu][2])
        tabla.setItem(2, 1, nuevo_item2)
        nuevo_item3 = QTableWidgetItem(EspecificacionesComputadora.Especificaciones[self.indexCompu][3])
        tabla.setItem(3, 1, nuevo_item3)
        nuevo_item4 = QTableWidgetItem(EspecificacionesComputadora.Especificaciones[self.indexCompu][4])
        tabla.setItem(4, 1, nuevo_item4)

        

        # Botón de cerrar
        boton_cerrar = QPushButton("Cerrar")
        boton_cerrar.clicked.connect(ventana_reintentos.close)
        layout.addWidget(label0)
        layout.addWidget(label)
        layout.addWidget(label1)
        layout.addWidget(link)
        layout.addWidget(tabla)
        layout.addWidget(boton_cerrar)
        ventana_reintentos.setLayout(layout)
        ventana_reintentos.exec()

    def configurar_icono_boton(self,boton, ruta_imagen):
        if boton is None:
            print("El botón proporcionado es nulo.")
            return

        icono = QIcon(ruta_imagen)
        if icono.isNull():
            print("No se pudo cargar el ícono desde la ruta proporcionada.")
            return

        boton.setIcon(icono)
    #boton.setStyleSheet("QPushButton { border: none; background: none; }")
        boton.setIconSize(QSize(50, 50))  



# Ejecuta aplicación
app = QApplication(sys.argv)

# Aplicar estilos globales directamente
app.setStyleSheet("""
    QWidget {
        background-color: #f0f0f0;
    }
    
    QLabel {
        
        font-size: 14px;
        color: #333;
    }
    
    QPushButton {
        background-color: #77afc1;
        color: white;
        border-radius: 5px;
        padding: 10px;
    }
    
                  
     QSlider::groove:horizontal {
        border: 1px solid #bbb;
        background: #ddd;
        height: 20px;
        border-radius: 2px;
    }

    QSlider::handle:horizontal {
        background: #126ebc;
        border: 2px solid #126ebc;
        width: 13px;
        height: 18px;
        border-radius: 2px;
    }

    QSlider::sub-page:horizontal {
        background: #77afc1;
        border-radius: 2px;
    }

    QSlider::add-page:horizontal {
        background: white;
        border-radius: 2px;
    }
    
    QComboBox QAbstractItemView {
        background-color: #ffffff;
        border: 1px solid #77afc1;
        selection-background-color: #A5D6A7;
    }
    QComboBox {
        background-color: white;
        border: 2px solid #77afc1;
        border-radius: 6px;
        padding: 5px;
        font-size: 14px;
    }
            

    QComboBox::drop-down {
        border: none;
        width: 20px;
        background: #77afc1;
        border-radius: 3px;
    }

    QComboBox::down-arrow {
        image: url(Icons/arrow.png);
        width: 16px;
        height: 16px;
    }


                  
    QPushButton {
        background-color: #4074be;
        color: white;
        font-size: 14px;
        padding: 7px;
        border-radius: 8px;
        border: none;
    }

    QPushButton:hover {
        background-color:#333;
    }

    QPushButton:pressed {
        background-color: #4c4c4c;
    }
                  
    QTableWidget {
        background-color: #f0f0f0;  /* Color de fondo de las tablas */
        gridline-color: #0078d7;   /* Color de las líneas */
    }
    
    QHeaderView::section {
        background-color: #77afc1; /* Fondo de los encabezados */
        color: white;              /* Color del texto en encabezados */
        font-weight: bold;         /* Texto en negrita */
        border: none;
    }

    QTableWidget::item:selected {
        background-color: #005a9e; /* Fondo de celdas seleccionadas */
        color: white;              /* Texto de celdas seleccionadas */
    }
""")

ventana = InterfazBayes()
ventana.show()
sys.exit(app.exec())

