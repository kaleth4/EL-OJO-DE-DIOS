
# 👁️ **El Ojo de Dios** - Visor de Cámaras IP
<img width="768" height="512" alt="de9c5f58-cd36-45d8-b4f1-472b96d07d4d" src="https://github.com/user-attachments/assets/dbb81635-2d70-488a-a463-b9f15a084aa2" />


**El Ojo de Dios** es una herramienta diseñada para acceder a cámaras IP que, por configuración insegura, exponen sus transmisiones sin autenticación o con credenciales por defecto. Utiliza una interfaz gráfica minimalista basada en `tkinter` y `Pillow` para mostrar múltiples flujos de video en tiempo real.


⚠️ **Advertencia**: Este software **solo debe usarse en entornos controlados** (ej: pruebas de seguridad autorizadas). Acceder a cámaras sin permiso puede ser **ilegal** en la mayoría de jurisdicciones.

---

## 🛠️ **Requisitos Previos**
Antes de ejecutar el programa, instala las dependencias necesarias:

```bash
pip install pillow opencv-python numpy
```

---

## 🚀 **Instalación y Uso**
1. Clona este repositorio o descarga el archivo `eye.py`.
2. Ejecuta el script con Python:
   ```bash
   python eye.py
   ```
3. La interfaz se abrirá automáticamente mostrando las cámaras configuradas.

---

## 📂 **Estructura del Proyecto**
```
el-ojo-de-dios/
├── eye.py          # Código principal de la interfaz
├── README.md       # Este archivo
└── requirements.txt # Dependencias (opcional)
```

---

## 🎨 **Características de la Interfaz**
- **Diseño minimalista**: Interfaz oscura para mayor comodidad visual.
- **Visualización en tiempo real**: Muestra hasta 2 flujos de cámaras simultáneamente.
- **Manejo de errores**: Si una cámara falla, muestra un mensaje de estado sin bloquear la aplicación.
- **Actualización automática**: Refresca los fotogramas cada 30ms.

---

## 🔧 **Configuración Avanzada**
Para modificar las URLs de las cámaras:
1. Edita el diccionario `URLS` en `eye.py`:
   ```python
   URLS = {
       "Camara 1 - Oficina": "http://118.243.56.123/video.mjpg",
       "Camara 2 - Parking": "http://203.181.31.45/stream"
   }
   ```
2. Asegúrate de que las URLs sean accesibles (pueden requerir autenticación).

---

## ⚠️ **Notas de Seguridad**
- **No uses este software para actividades maliciosas**.
- Las URLs proporcionadas en el ejemplo son **inseguras y ficticias**.
- Para cámaras reales, verifica siempre las políticas de privacidad y los permisos legales.



---
## ⛔ **NO Contribuciones**


---
*© 2026 El Ojo de Dios. Todos los derechos reservados.*
```
