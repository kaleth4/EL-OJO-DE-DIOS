import urllib.request
import numpy as np
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# URLs de las cámaras
URLS = {
    "Camara 1 - Oficina": "Cámaras IP",
    "Camara 2 - Parking": "Cámaras IP"
}

def obtener_fotograma(url):
    try:
        with urllib.request.urlopen(url, timeout=1) as respuesta:
            img_array = np.array(bytearray(respuesta.read()), dtype=np.uint8)
            frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            if frame is not None:
                # Convertir de BGR (OpenCV) a RGB (Tkinter/Pillow)
                return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    except Exception:
        pass
    return None

def actualizar_camaras():
    # Actualizar Cámara 1
    frame1 = obtener_fotograma(URLS["Camara 1 - Oficina"])
    if frame1 is not None:
        img1 = Image.fromarray(frame1)
        imgtk1 = ImageTk.PhotoImage(image=img1)
        label_cam1.imgtk = imgtk1
        label_cam1.configure(image=imgtk1)
    else:
        label_cam1.configure(image="", text="Cámara 1 fuera de línea", foreground="red")

    # Actualizar Cámara 2
    frame2 = obtener_fotograma(URLS["Camara 2 - Parking"])
    if frame2 is not None:
        img2 = Image.fromarray(frame2)
        imgtk2 = ImageTk.PhotoImage(image=img2)
        label_cam2.imgtk = imgtk2
        label_cam2.configure(image=imgtk2)
    else:
        label_cam2.configure(image="", text="Cámara 2 fuera de línea", foreground="red")

    # Volver a ejecutar esta función tras 30 milisegundos (bucle asíncrono)
    root.after(30, actualizar_camaras)

# Configuración de la interfaz principal (Tkinter)
root = tk.Tk()
root.title("Visor de Cámaras IP")
root.configure(bg="#1e1e1e")  # Fondo oscuro elegante

# Estilo minimalista para los títulos
estilo = ttk.Style()
estilo.configure("TLabel", font=("Arial", 12, "bold"), background="#1e1e1e", foreground="#ffffff")

# Contenedor para Cámara 1
frame_cam1 = tk.Frame(root, bg="#1e1e1e", bd=2, relief="flat")
frame_cam1.grid(row=0, column=0, padx=10, pady=10)
titulo1 = ttk.Label(frame_cam1, text="Cámara 1 - Oficina", style="TLabel")
titulo1.pack(pady=5)
label_cam1 = tk.Label(frame_cam1, bg="#000000", width=640, height=480, text="Cargando...", fg="white")
label_cam1.pack()

# Contenedor para Cámara 2
frame_cam2 = tk.Frame(root, bg="#1e1e1e", bd=2, relief="flat")
frame_cam2.grid(row=0, column=1, padx=10, pady=10)
titulo2 = ttk.Label(frame_cam2, text="Cámara 2 - Parking", style="TLabel")
titulo2.pack(pady=5)
label_cam2 = tk.Label(frame_cam2, bg="#000000", width=640, height=480, text="Cargando...", fg="white")
label_cam2.pack()

# Iniciar el bucle de actualización de video
root.after(100, actualizar_camaras)

# Ejecutar la ventana gráfica
root.mainloop()