import yt_dlp, yt_dlp.YoutubeDL, tkinter as tk, os, shutil
from android.storage import primary_external_storage_path
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
#region variablesexternas
link = "vacio"
#endregion

#region Fuciones

# Función para mostrar un mensaje
"""
def moverDescarga(ruta_variable):
    ruta_area_de_trabajo = os.getcwd()
    archivos_mp4 = [archivo for archivo in os.listdir(ruta_area_de_trabajo) if archivo.endswith('.mp4')]
    shutil.move(archivos_mp4[0], ruta_variable)
"""
def descargar_video(url, ubicacion):
    ruta_variable = ubicacion
    link = url
    if link != 'vacio':
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
            'outtmpl': f'{ruta_variable}/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
            'postprocessors': [
                {
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4'
                }
            ]
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
        except Exception as ex:
            print(f"Hubo un problema con la descarga del video: {ex}")

class MyApp(App):
    def build(self):
        self.variable = ""
        self.ruta_descargas = os.path.join(primary_external_storage_path(), 'Download')

        layout = BoxLayout(orientation='vertical')

        self.text_input = TextInput(hint_text='Ingrese el enlace')
        layout.add_widget(self.text_input)

        self.result_label = Label(text="Esperando acción...")
        layout.add_widget(self.result_label)

        button = Button(text="Descargar")
        button.bind(on_press=self.descargar_video)
        layout.add_widget(button)

        return layout

    def descargar_video(self, instance):
        self.variable = self.text_input.text
        descargar_video(self.variable, self.ruta_descargas)
        self.result_label.text = f"Video guardado en: {self.ruta_descargas}"

#"""
if __name__ == "__main__":
    #__main__()
    MyApp().run()
#"""