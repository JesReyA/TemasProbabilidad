from PIL import Image, ImageTk
import customtkinter as ctk
from tkinter import messagebox
import sympy as sp

# IMPORTS
from tema_uno import TemaUno
#from tema_dos import TemaDos
#from tema_tres import TemaTres
#from tema_cuatro import TemaCuatro
from tema_cinco import TemaCinco
from tema_nueve import TemaNueve

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

NEON_BLUE = "#00f2ff"
NEON_HOVER = "#00c0cc"
DARK_BG = "#1E1F23"
TEXT_COLOR = "white"


class NeonEntry(ctk.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master, border_width=1, border_color=DARK_BG, **kwargs)
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)

    def on_focus_in(self, event): self.configure(border_color=NEON_BLUE, border_width=2)

    def on_focus_out(self, event): self.configure(border_color=DARK_BG, border_width=1)


class NumericalMethodsApp(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color="#17161B")

        # INSTANCIAS LÓGICAS
        self.logic_tema_uno = TemaUno()
        #self.logic_tema_dos = TemaDos(None)
        #self.logic_tema_tres = TemaTres(None)
        #self.logic_tema_cuatro = TemaCuatro(None)
        self.logic_tema_cinco = TemaCinco()
        self.logic_tema_nueve = TemaNueve()

        self.title("Probabilidad y estadística")
        self.geometry("950x750")
        self.resizable(True, True)
        self.after(0, lambda: self.state('zoomed'))

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color="#1C1D22")
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Probabilidad y\nestadística\n",
                                       font=ctk.CTkFont(size=20, weight="bold"), text_color=TEXT_COLOR)
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # MENU
        self.method_option_menu = ctk.CTkOptionMenu(self.sidebar_frame,
                                                    values=[
                                                        "Tema Uno",
                                                        "Tema Dos",
                                                        "Tema Tres",
                                                        "Tema Cuatro",
                                                        "Tema Cinco",
                                                        "Tema Seis",
                                                        "Tema Siete",
                                                        "Tema Ocho",
                                                        "Tema Nueve"
                                                    ],
                                                    command=self.change_method_event)
        self.method_option_menu.grid(row=2, column=0, padx=20, pady=10)

        self.calc_button = ctk.CTkButton(self.sidebar_frame, text="CALCULAR", height=40,
                                         font=ctk.CTkFont(size=15, weight="bold"), fg_color=NEON_BLUE,
                                         hover_color=NEON_HOVER, border_color=NEON_BLUE, border_width=2,
                                         text_color="black", command=self.calculate_event)
        self.calc_button.grid(row=3, column=0, padx=20, pady=20)

        self.main_frame = ctk.CTkFrame(self, corner_radius=20, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.title_label = ctk.CTkLabel(self.main_frame, text="", font=ctk.CTkFont(size=28, weight="bold"),
                                        text_color=TEXT_COLOR)
        self.title_label.pack(pady=(10, 20))

        self.input_container = ctk.CTkFrame(self.main_frame, fg_color=DARK_BG, corner_radius=15)
        self.input_container.pack(fill="x", padx=20, pady=10)

        self.definition_label = ctk.CTkLabel(self.main_frame, text="Definición:",
                                         font=ctk.CTkFont(size=16, weight="bold"), text_color=NEON_BLUE, anchor="w")
        self.definition_label.pack(pady=(20, 5), padx=20, fill="x")

        self.definition_textbox = ctk.CTkTextbox(self.main_frame, height=100, corner_radius=15, border_width=2,
                                             border_color=NEON_BLUE, fg_color=DARK_BG, text_color=TEXT_COLOR,
                                             font=ctk.CTkFont(family="Consolas", size=12))
        self.definition_textbox.pack(fill="x", padx=20, pady=(0, 10))
        self.definition_textbox.configure(state="disabled")

        self.result_label = ctk.CTkLabel(self.main_frame, text="Demostración:",
                                         font=ctk.CTkFont(size=16, weight="bold"), text_color=NEON_BLUE, anchor="w")
        self.result_label.pack(pady=(10, 5), padx=20, fill="x")

        self.result_textbox = ctk.CTkTextbox(self.main_frame, height=200, corner_radius=15, border_width=2,
                                             border_color=NEON_BLUE, fg_color=DARK_BG, text_color=TEXT_COLOR,
                                             font=ctk.CTkFont(family="Consolas", size=12))
        self.result_textbox.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        self.result_textbox.configure(state="disabled")

        self.entries = {}
        self.change_method_event("Tema Uno")

    def clean_inputs(self):
        for widget in self.input_container.winfo_children(): widget.destroy()
        self.entries = {}

    def create_entry(self, label_text, key):
        lbl = ctk.CTkLabel(self.input_container, text=label_text, font=ctk.CTkFont(size=14), text_color=TEXT_COLOR)
        lbl.pack(pady=(10, 5), padx=20, anchor="w")
        entry = NeonEntry(self.input_container, placeholder_text=f"Ingresa {label_text.lower()}...", height=35)
        entry.pack(pady=(0, 10), padx=20, fill="x")
        self.entries[key] = entry

    def create_horizontal_group(self, title, placeholders, keys):
        lbl = ctk.CTkLabel(self.input_container, text=title, font=ctk.CTkFont(size=14), text_color=TEXT_COLOR)
        lbl.pack(pady=(10, 5), padx=20, anchor="w")
        row_frame = ctk.CTkFrame(self.input_container, fg_color="transparent")
        row_frame.pack(pady=(0, 10), padx=20, fill="x")
        for i in range(3):
            entry = NeonEntry(row_frame, placeholder_text=placeholders[i], height=35, justify="center")
            entry.pack(side="left", fill="x", expand=True, padx=(0 if i == 0 else 10, 0))
            self.entries[keys[i]] = entry

    def create_horizontal_pair(self, title, placeholders, keys):
        lbl = ctk.CTkLabel(self.input_container, text=title, font=ctk.CTkFont(size=14), text_color=TEXT_COLOR)
        lbl.pack(pady=(10, 5), padx=20, anchor="w")
        row_frame = ctk.CTkFrame(self.input_container, fg_color="transparent")
        row_frame.pack(pady=(0, 10), padx=20, fill="x")
        for i in range(2):
            entry = NeonEntry(row_frame, placeholder_text=placeholders[i], height=35, justify="center")
            entry.pack(side="left", fill="x", expand=True, padx=(0 if i == 0 else 10, 0))
            self.entries[keys[i]] = entry

    def create_option_menu(self, label_text, values, key):
        lbl = ctk.CTkLabel(self.input_container, text=label_text, font=ctk.CTkFont(size=14), text_color=TEXT_COLOR)
        lbl.pack(pady=(10, 5), padx=20, anchor="w")
        option_menu = ctk.CTkOptionMenu(self.input_container, values=values)
        option_menu.pack(pady=(0, 10), padx=20, fill="x")
        self.entries[key] = option_menu

    def change_method_event(self, new_method):
        self.clean_inputs()
        self.title_label.configure(text=new_method)
        self.result_textbox.configure(state="normal")
        self.result_textbox.delete("1.0", "end")
        self.result_textbox.configure(state="disabled")

        # Mapeo de temas a sus instancias lógicas
        temas_logic = {
            "Tema Uno": self.logic_tema_uno,
            #"Tema Dos": self.logic_tema_dos,
            #"Tema Tres": self.logic_tema_tres,
            #"Tema Cuatro": self.logic_tema_cuatro,
            "Tema Cinco": self.logic_tema_cinco,
            "Tema Nueve": self.logic_tema_nueve
        }

        # Actualizar el cuadro de Definición
        logic = temas_logic.get(new_method)
        if logic and hasattr(logic, "definicion"):
            self.definition_textbox.configure(state="normal")
            self.definition_textbox.delete("1.0", "end")
            self.definition_textbox.insert("0.0", logic.definicion)
            self.definition_textbox.configure(state="disabled")
        else:
            self.definition_textbox.configure(state="normal")
            self.definition_textbox.delete("1.0", "end")
            self.definition_textbox.configure(state="disabled")

        if "Tema Dos" == new_method:
            self.create_entry("Número", "numero")
        elif "Tema Tres" == new_method:
            self.create_entry("Número", "numero")
        elif "Tema Cuatro" == new_method:
            self.create_entry("Número", "numero")
        elif "Tema Cinco" == new_method:
            opciones_tema_cinco = [
                "Tres corazones seguidos",
                "Rey rojo y carta negra",
                "Cuatro rojas seguidas",
                "Rey y Reina"
            ]
            self.create_option_menu("Selecciona el caso", opciones_tema_cinco, "caso_tema_cinco")


    def append_result(self, text):
        self.result_textbox.configure(state="normal")
        self.result_textbox.insert("end", text + "\n")
        self.result_textbox.configure(state="disabled")
        self.result_textbox.see("end")

    def overwrite_result(self, text):
        self.result_textbox.configure(state="normal")
        self.result_textbox.delete("1.0", "end")
        self.result_textbox.insert("0.0", text + "\n")
        self.result_textbox.configure(state="disabled")

    def calculate_event(self):
        method = self.method_option_menu.get()
        try:
            # --- Tema Uno ---
            if method == "Tema Uno":
                self.logic_tema_uno = TemaUno()

                ruta_carta = self.logic_tema_uno.mostrar_carta()
                img_pil = Image.open(ruta_carta)
                
                img_pil = img_pil.resize((250, 350)) 
                self.foto_carta = ImageTk.PhotoImage(img_pil)
                
                self.result_textbox.configure(state="normal")

                self.result_textbox.delete("1.0", "end")

                self.result_textbox._textbox.image_create("end", image=self.foto_carta)
                self.result_textbox.configure(state="disabled")

            elif method == "Tema Cinco":
                self.logic_tema_cinco = TemaCinco()
                self.logic_tema_cinco.mazoCartas()
                
                caso_seleccionado = self.entries.get("caso_tema_cinco")
                if caso_seleccionado:
                    caso_val = caso_seleccionado.get()
                    if caso_val == "Tres corazones seguidos":
                        probabilidad, cartas = self.logic_tema_cinco.tres_corazones_seguidos()
                    elif caso_val == "Rey rojo y carta negra":
                        probabilidad, cartas = self.logic_tema_cinco.rey_rojo_y_carta_negra()
                    elif caso_val == "Cuatro rojas seguidas":
                        probabilidad, cartas = self.logic_tema_cinco.cuatro_rojas_seguidas()
                    elif caso_val == "Rey y Reina":
                        probabilidad, cartas = self.logic_tema_cinco.rey_reina()
                    else:
                        probabilidad, cartas = 0, []
                    
                    self.result_textbox.configure(state="normal")
                    self.result_textbox.delete("1.0", "end")
                    self.result_textbox.insert("end", f"Probabilidad: {probabilidad}\n\nCartas seleccionadas:\n")
                    
                    self.fotos_tema_cinco = [] 
                    for ruta in cartas:
                        img_pil = Image.open(ruta)
                        img_pil = img_pil.resize((120, 180)) 
                        foto = ImageTk.PhotoImage(img_pil)
                        self.fotos_tema_cinco.append(foto)
                        self.result_textbox._textbox.image_create("end", image=foto)
                        self.result_textbox.insert("end", "   ") 
                    
                    self.result_textbox.insert("end", "\n")
                    self.result_textbox.configure(state="disabled")

            elif method == "Tema Nueve":
                self.logic_tema_nueve = TemaNueve()

                self.result_textbox.configure(state="normal")
                self.result_textbox.delete("1.0", "end")

                self.result_textbox.configure(state="disabled")

                self.logic_tema_nueve.conjuntoNumeros()
                self.append_result("Datos: " + str(self.logic_tema_nueve.datos))
                self.append_result("\n")
                self.append_result("Moda: " + str(self.logic_tema_nueve.calculateModa()))
                self.append_result("Media: " + str(self.logic_tema_nueve.calculateMedia()))
                self.append_result("Mediana: " + str(self.logic_tema_nueve.calculateMediana()))
                self.append_result("Desviacion estandar poblacional: " + str(self.logic_tema_nueve.calculateDesviacionPoblacional()))
                self.append_result("Varianza poblacional: " + str(self.logic_tema_nueve.calculateVarianzaPoblacional()))
                self.append_result("Varianza muestral: " + str(self.logic_tema_nueve.calculateVarianzaMuestral()))
                self.append_result("Desviacion muestral: " + str(self.logic_tema_nueve.calculateDesviacionMuestral()))

            else:
                self.overwrite_result("Método pendiente.")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")


if __name__ == "__main__":
    app = NumericalMethodsApp()
    app.mainloop()