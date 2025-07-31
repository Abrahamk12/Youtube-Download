import yt_dlp
import os
import shutil
import traceback

# 📍 Enlace y destino de la descarga
link = "https://youtu.be/BaUg0fRNVMQ"
ubicacion = "D:\\Musica Rancheras"
archivo_temporal = "TEMP_AUDIO.mp3"

def mostrar_progreso(d):
    """Imprime progreso de la descarga en consola."""
    if d['status'] == 'downloading':
        print(f"⏳ {d['_percent_str']} | {d['_speed_str']} | ETA {d['_eta_str']}")
    elif d['status'] == 'finished':
        print("✅ Descarga completa. Extrayendo audio...")

def mover_descarga(destino, nombre_archivo):
    """Mueve el archivo descargado al destino indicado."""
    origen = os.path.join(os.getcwd(), nombre_archivo)
    destino_final = os.path.join(destino, nombre_archivo)

    if not os.path.exists(origen):
        print("⚠️ No se encontró el archivo para mover.")
        return

    if not os.path.exists(destino):
        os.makedirs(destino)

    shutil.move(origen, destino_final)
    print(f"📦 Archivo movido a: {destino_final}")

def descargar_audio(url, destino):
    """Descarga audio desde YouTube y lo mueve a la carpeta destino."""
    if not url or url == "vacio":
        print("⚠️ Enlace no válido.")
        return

    print("🎶 Iniciando descarga...")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'TEMP_AUDIO.%(ext)s',
        'quiet': False,
        'progress_hooks': [mostrar_progreso],
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }
        ]
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        mover_descarga(destino, archivo_temporal)
        print("🎉 Proceso finalizado con éxito.")
    except Exception as ex:
        print("💥 Ocurrió un error:")
        print(traceback.format_exc())

# 🚀 Ejecutar
descargar_audio(link, ubicacion)
