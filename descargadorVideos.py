import yt_dlp
import tkinter as tk
from tkinter import messagebox, filedialog
import os, shutil

# ─── Funciones comunes ──────────────────────────────────────
def mover_archivo(extension, destino):
    carpeta = os.getcwd()
    archivos = [f for f in os.listdir(carpeta) if f.endswith(extension)]
    if archivos:
        shutil.move(archivos[0], destino)

def mostrar_mensaje(titulo, mensaje):
    messagebox.showinfo(titulo, mensaje)

def mostrar_estado(estado):
    estados = {
        'descargando_video': "Descargando video...",
        'descargando_audio': "Descargando música...",
        'exito': "Descarga terminada. El archivo se movió correctamente.",
        'error_video': "Hubo un problema con la descarga del video: {}",
        'error_audio': "Hubo un problema con la descarga del audio: {}"
    }
    return estados.get(estado)

# ─── Descarga de video ──────────────────────────────────────
def descargar_video(url, destino):
    opciones = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'postprocessors': [
            {'key': 'FFmpegVideoConvertor', 'preferedformat': 'mp4'}
        ]
    }
    try:
        mostrar_mensaje('Aviso', mostrar_estado('descargando_video'))
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])
        mover_archivo('.mp4', destino)
        mostrar_mensaje('Aviso', mostrar_estado('exito'))
    except Exception as e:
        mostrar_mensaje('Aviso', mostrar_estado('error_video').format(e))

# ─── Descarga de audio ──────────────────────────────────────
def descargar_audio(url, destino):
    opciones = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }
        ]
    }
    try:
        mostrar_mensaje('Aviso', mostrar_estado('descargando_audio'))
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])
        mover_archivo('.mp3', destino)
        mostrar_mensaje('Aviso', mostrar_estado('exito'))
    except Exception as e:
        mostrar_mensaje('Aviso', mostrar_estado('error_audio').format(e))

# ─── Interfaz gráfica ───────────────────────────────────────
def main():
    root = tk.Tk()
    root.title("Descargador de Video y Audio")

    # Centrar ventana
    w, h = 550, 120
    x = (root.winfo_screenwidth() // 2) - (w // 2)
    y = (root.winfo_screenheight() // 2) - (h // 2)
    root.geometry(f"{w}x{h}+{x}+{y}")

    ruta_destino = tk.StringVar()

    def seleccionar_carpeta():
        carpeta = filedialog.askdirectory()
        if carpeta:
            ruta_destino.set(carpeta)

    def abrir_carpeta():
        os.startfile(ruta_destino.get())

    def ejecutar_descarga_video():
        descargar_video(entry_url.get(), ruta_destino.get())

    def ejecutar_descarga_audio():
        descargar_audio(entry_url.get(), ruta_destino.get())

    # UI
    tk.Label(root, text="Ubicación:").place(x=10, y=10)
    tk.Label(root, textvariable=ruta_destino).place(x=80, y=10)
    tk.Label(root, text="Ingrese la URL:").place(x=10, y=60)

    entry_url = tk.Entry(root, width=50)
    entry_url.place(x=120, y=60)

    tk.Button(root, text="Seleccionar Carpeta", command=seleccionar_carpeta).place(x=415, y=8)
    tk.Button(root, text="Descargar Video", command=ejecutar_descarga_video).place(x=415, y=50)
    tk.Button(root, text="Descargar Música", command=ejecutar_descarga_audio).place(x=415, y=84)
    tk.Button(root, text="Abrir Carpeta", command=abrir_carpeta).place(x=202, y=85)

    root.mainloop()

if __name__ == "__main__":
    main()
