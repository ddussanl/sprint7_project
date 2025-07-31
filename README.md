# sprint7_project
Proyecto del Sprint 7 del bootcamp de Tripleten - DA

# Dashboard de vehículos usados en EE. UU.

Este proyecto forma parte del Sprint 7 del bootcamp de Data Analytics. La aplicación fue construida usando **Streamlit**, **pandas** y **plotly-express**, y permite explorar datos de vehículos usados en Estados Unidos de forma interactiva.

## 🎯 Funcionalidades principales

- ✅ Visualización de un **histograma** del kilometraje (`odometer`)
- ✅ Visualización de un **gráfico de dispersión** (`odometer` vs `price`)
- ✅ Tabla con los **10 valores de odómetro más frecuentes**
- ✅ Visualización de un **gráfico de líneas** del precio promedio por año del modelo
- ✅ **Slider interactivo** para filtrar el rango de años en el gráfico de líneas
- ✅ Visualización previa de los datos relacionados con cada gráfico

## 🚀 Cómo ejecutar la app localmente

1. Crea y activa un entorno virtual
2. Instala las dependencias:
   pip install -r requirements.txt
   streamlit run app.py

sprint7_project/
├── app.py
├── vehicles_us.csv
├── requirements.txt
├── README.md
└── notebooks/
    └── EDA.ipynb



