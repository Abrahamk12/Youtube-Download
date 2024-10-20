import yt_dlp, yt_dlp.YoutubeDL, tkinter as tk, os, shutil
from tkinter import messagebox, filedialog
#region variablesexternas
link = "vacio"
#endregion

#region Fuciones

# Función para mostrar un mensaje
def moverDescarga(ruta_variable):
    ruta_area_de_trabajo = os.getcwd()
    archivos_mp4 = [archivo for archivo in os.listdir(ruta_area_de_trabajo) if archivo.endswith('.mp4')]
    shutil.move(archivos_mp4[0], ruta_variable)

def gescargar_video(url, ubicacion)->None:
    ruta_variable = ubicacion
    link = url
    if(link != 'vacio'):
        mostrar_mensaje_descarga()
        ydl_opts = {
            'format':'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
            'outtmpl':'%(title)s.%(ext)s',
            'merge_output_format': 'mp4',

            'postprocessors':[
                {
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat':'mp4'
                }
            ]
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
                moverDescarga(ruta_variable)
                mostrar_mensaje_descarga_terminada()
        except Exception as ex:
            mostrar_mensaje_descarga_fallida(ex)
            #print(f"Hubo un problema con la descarga del video: {ex}")

def mostrar_mensaje_descarga_terminada()->None:
    messagebox.showinfo('Aviso',"Descarga terminada, el archvio se encuentra en la carpeta del ejecutable")
def mostrar_mensaje_descarga_fallida(ex)->None:
    messagebox.showinfo('Aviso',f"Hubo un problema con la descarga del video: {ex}")
def mostrar_mensaje_descarga()->None:
    messagebox.showinfo('Aviso',f"Descargando video")
#endregion

#region VentanaPrincipal
def __main__()->None:
    #region configuracionVentana
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Descargador de videos")

    # Establecer las dimensiones de la ventana (ancho x alto)
    # Dimensiones de la ventana
    ancho_ventana = 480
    alto_ventana = 120

    # Obtener el tamaño de la pantalla
    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()

    # Calcular la posición centrada
    pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    pos_y = (alto_pantalla // 2) - (alto_ventana // 2)

    # Establecer la geometría de la ventana
    root.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")
    #endregion
    #region variables
    ruta_variable = tk.StringVar()
    #endregion

    #region funciones anidadas
    # Variable para guardar la ruta
    
    def seleccionar_carpeta():
        ruta_carpeta = filedialog.askdirectory()
        if ruta_carpeta:
            ruta_variable.set(ruta_carpeta)
    
    def abrir_explorador():
        ruta = ruta_variable.get()  # Establece aquí la ruta deseada
        os.startfile(ruta)

    def descagrar():
        gescargar_video(urlEntrada.get(), ruta_variable.get())
        
    #endregion
    
    #region label
    # Crear el Label
    ubicacion = tk.Label(root, text=f"Ubicacion:")
    # Posicionar el Label
    ubicacion.place(x=10, y=10)

    # Crear el Label
    ruta = tk.Label(root, textvariable=ruta_variable)
    # Posicionar el Label
    ruta.place(x=70, y=10)

    # Crear el Label
    urlBusqueda = tk.Label(root, text="Ingrese la URL: ")
    # Posicionar el Label
    urlBusqueda.place(x=10, y=60)
    #endregion

    #region textbox
    # Crear el widget Entry
    urlEntrada = tk.Entry(root, width=50)
    urlEntrada.pack(pady=10)
    urlEntrada.place(x=100, y=60)
    #endregion

    #region botones
    # Crear el Botón
    buscarCarpeta = tk.Button(root, text="Seleccionar Carpeta", command=seleccionar_carpeta)
    # Posicionar el Botón
    buscarCarpeta.place(x=358, y=9)

    # Crear el Botón
    descargar = tk.Button(root, text="Descargar", command=descagrar)
    # Posicionar el Botón
    descargar.place(x=410, y=54)

    # Crear el botón
    boton_abrir = tk.Button(root, text="Abrir Carpeta", command=abrir_explorador)
    boton_abrir.place(x=202, y=85)
    #endregion

    # Iniciar el bucle principal
    root.mainloop()
#endregion
#moverDescarga()
#"""
if __name__ == "__main__":
    __main__()
#"""