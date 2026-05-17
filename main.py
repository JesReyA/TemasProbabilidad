from PIL import Image, ImageTk
import customtkinter as ctk
from tkinter import messagebox
import sympy as sp

# IMPORTS
from tema_uno import TemaUno
from tema_dos import TemaDos
from tema_tres import TemaTres
from tema_cuatro import TemaCuatro
from tema_cinco import TemaCinco
from tema_seis import TemaSeis
from tema_siete import TemaSiete
from tema_ocho import TemaOcho
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
        self.logic_tema_dos = TemaDos()
        self.logic_tema_tres = TemaTres()
        self.logic_tema_cuatro = TemaCuatro()
        self.logic_tema_cinco = TemaCinco()
        self.logic_tema_seis = TemaSeis()
        self.logic_tema_siete = TemaSiete()
        self.logic_tema_ocho = TemaOcho()
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

    def create_option_menu(self, label_text, values, key, command=None):
        lbl = ctk.CTkLabel(self.input_container, text=label_text, font=ctk.CTkFont(size=14), text_color=TEXT_COLOR)
        lbl.pack(pady=(10, 5), padx=20, anchor="w")
        option_menu = ctk.CTkOptionMenu(self.input_container, values=values, command=command)
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
            "Tema Dos": self.logic_tema_dos,
            "Tema Tres": self.logic_tema_tres,
            "Tema Cuatro": self.logic_tema_cuatro,
            "Tema Cinco": self.logic_tema_cinco,
            "Tema Seis": self.logic_tema_seis,
            "Tema Siete": self.logic_tema_siete,
            "Tema Ocho": self.logic_tema_ocho,
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
            self.tema_dos_dynamic_frame = ctk.CTkFrame(self.input_container, fg_color="transparent")
            
            def update_tema_dos(choice):
                for widget in self.tema_dos_dynamic_frame.winfo_children():
                    widget.destroy()
                
                if choice == "Eventos Disjuntos":
                    desc = self.logic_tema_dos.eventos_disjuntos
                elif choice == "Eventos Complementarios":
                    desc = self.logic_tema_dos.eventos_complementarios
                else:
                    desc = self.logic_tema_dos.eventos_compuestos
                
                lbl_desc = ctk.CTkLabel(self.tema_dos_dynamic_frame, text=desc, font=ctk.CTkFont(size=14), text_color=TEXT_COLOR, wraplength=650, justify="left")
                lbl_desc.pack(pady=(10, 20), padx=20, fill="x", anchor="w")
                
                if choice == "Eventos Complementarios":
                    lbl = ctk.CTkLabel(self.tema_dos_dynamic_frame, text="Probabilidad A", font=ctk.CTkFont(size=14), text_color=TEXT_COLOR)
                    lbl.pack(pady=(10, 5), padx=20, anchor="w")
                    entry = NeonEntry(self.tema_dos_dynamic_frame, placeholder_text="Ingresa Prob. A...", height=35)
                    entry.pack(pady=(0, 10), padx=20, fill="x")
                    self.entries["prob_a_t2"] = entry
                else:
                    lbl = ctk.CTkLabel(self.tema_dos_dynamic_frame, text="Probabilidades", font=ctk.CTkFont(size=14), text_color=TEXT_COLOR)
                    lbl.pack(pady=(10, 5), padx=20, anchor="w")
                    row_frame = ctk.CTkFrame(self.tema_dos_dynamic_frame, fg_color="transparent")
                    row_frame.pack(pady=(0, 10), padx=20, fill="x")
                    entry_a = NeonEntry(row_frame, placeholder_text="Prob. A", height=35, justify="center")
                    entry_a.pack(side="left", fill="x", expand=True)
                    self.entries["prob_a_t2"] = entry_a
                    
                    entry_b = NeonEntry(row_frame, placeholder_text="Prob. B", height=35, justify="center")
                    entry_b.pack(side="left", fill="x", expand=True, padx=(10, 0))
                    self.entries["prob_b_t2"] = entry_b

            opciones_tema_dos = ["Eventos Disjuntos", "Eventos Complementarios", "Eventos Compuestos"]
            self.create_option_menu("Selecciona el tipo de evento", opciones_tema_dos, "caso_tema_dos", command=update_tema_dos)
            self.tema_dos_dynamic_frame.pack(fill="x", pady=0)
            update_tema_dos("Eventos Disjuntos")
        elif "Tema Tres" == new_method:
            lbl_problema = ctk.CTkLabel(self.input_container, text=self.logic_tema_tres.problema, font=ctk.CTkFont(size=14), text_color=TEXT_COLOR, wraplength=650, justify="left")
            lbl_problema.pack(pady=20, padx=20, fill="x", anchor="w")
        elif "Tema Cuatro" == new_method:
            lbl_problema = ctk.CTkLabel(self.input_container, text=self.logic_tema_cuatro.problema, font=ctk.CTkFont(size=14), text_color=TEXT_COLOR, wraplength=650, justify="left")
            lbl_problema.pack(pady=20, padx=20, fill="x", anchor="w")
        elif "Tema Cinco" == new_method:
            opciones_tema_cinco = [
                "Tres corazones seguidos",
                "Rey rojo y carta negra",
                "Cuatro rojas seguidas",
                "Rey y Reina"
            ]
            self.create_option_menu("Selecciona el caso", opciones_tema_cinco, "caso_tema_cinco")
        elif "Tema Seis" == new_method:
            def update_desc_tema_seis(choice):
                self.definition_textbox.configure(state="normal")
                self.definition_textbox.delete("1.0", "end")
                base_def = self.logic_tema_seis.definicion + "\n\nEjemplo:\n"
                if choice == "Evento A":
                    self.definition_textbox.insert("0.0", base_def + self.logic_tema_seis.desc_evento_A)
                else:
                    self.definition_textbox.insert("0.0", base_def + self.logic_tema_seis.desc_evento_B)
                self.definition_textbox.configure(state="disabled")

            opciones_tema_seis = ["Evento A", "Evento B"]
            self.create_option_menu("Selecciona el evento", opciones_tema_seis, "caso_tema_seis", command=update_desc_tema_seis)
            update_desc_tema_seis("Evento A")
            self.create_horizontal_group("Probabilidades", ["Prob. Normal", "Prob. A", "Prob. B"], ["prob_normal", "prob_a", "prob_b"])
        elif "Tema Siete" == new_method:
            opciones = ["2 Eventos (A, B)", "3 Eventos (A, B, C)", "4 Eventos (A, B, C, D)"]
            
            lbl_problema = ctk.CTkLabel(self.input_container, text="", font=ctk.CTkFont(size=14), text_color=TEXT_COLOR, wraplength=650, justify="left")
            lbl_problema.pack(pady=(10, 10), padx=20, anchor="w", fill="x")
            
            wizard_frame = ctk.CTkFrame(self.input_container, fg_color="transparent")
            wizard_frame.pack(fill="x", padx=20, pady=(5, 10))
            
            lbl_step = ctk.CTkLabel(wizard_frame, text="Paso 1", font=ctk.CTkFont(size=14, weight="bold"), text_color=NEON_BLUE)
            lbl_step.pack(pady=(5, 5))
            
            lbl_instruction = ctk.CTkLabel(wizard_frame, text="Ingresa P(A):", font=ctk.CTkFont(size=14), text_color=TEXT_COLOR)
            lbl_instruction.pack(pady=(0, 10))
            
            entry_val = NeonEntry(wizard_frame, placeholder_text="0.0", justify="center", height=35)
            entry_val.pack(pady=(0, 10))
            
            btn_frame = ctk.CTkFrame(wizard_frame, fg_color="transparent")
            btn_frame.pack(fill="x", pady=(0, 10))
            
            self.tema_siete_state = {"step": 0, "values": [], "labels": [], "case": "2 Eventos (A, B)"}
            
            def render_step():
                state = self.tema_siete_state
                total_steps = len(state["labels"])
                if state["step"] < total_steps:
                    lbl_step.configure(text=f"Paso {state['step'] + 1} de {total_steps}")
                    lbl_instruction.configure(text=f"Ingresa {state['labels'][state['step']]}:")
                    entry_val.configure(state="normal")
                    entry_val.delete(0, "end")
                    if state["step"] < len(state["values"]):
                        entry_val.insert(0, str(state["values"][state["step"]]))
                    entry_val.focus()
                    btn_next.configure(text="Siguiente")
                else:
                    lbl_step.configure(text="¡Completado!")
                    lbl_instruction.configure(text="Has ingresado todos los valores. Presiona CALCULAR.")
                    entry_val.delete(0, "end")
                    entry_val.configure(state="disabled")
                    btn_next.configure(text="Terminado")

            def next_step(event=None):
                state = self.tema_siete_state
                if state["step"] >= len(state["labels"]): return
                try:
                    val = float(entry_val.get())
                except ValueError:
                    messagebox.showerror("Error", "Por favor ingresa un número válido.")
                    return
                if state["step"] < len(state["values"]):
                    state["values"][state["step"]] = val
                else:
                    state["values"].append(val)
                state["step"] += 1
                render_step()

            def prev_step():
                state = self.tema_siete_state
                if state["step"] > 0:
                    state["step"] -= 1
                    render_step()
                    
            def reset_wizard():
                state = self.tema_siete_state
                state["step"] = 0
                state["values"] = []
                render_step()

            btn_prev = ctk.CTkButton(btn_frame, text="Atrás", width=80, command=prev_step)
            btn_prev.pack(side="left", padx=10)
            
            btn_reset = ctk.CTkButton(btn_frame, text="Reiniciar", width=80, fg_color="#C0392B", hover_color="#922B21", command=reset_wizard)
            btn_reset.pack(side="left", expand=True)
            
            btn_next = ctk.CTkButton(btn_frame, text="Siguiente", width=80, command=next_step)
            btn_next.pack(side="right", padx=10)
            
            entry_val.bind("<Return>", next_step)
            
            def update_tema_siete_case(choice):
                state = self.tema_siete_state
                state["case"] = choice
                state["step"] = 0
                state["values"] = []
                if choice == "2 Eventos (A, B)":
                    lbl_problema.configure(text=self.logic_tema_siete.problema_uno)
                    state["labels"] = ["P(A)", "P(B)", "P(A ∩ B)"]
                elif choice == "3 Eventos (A, B, C)":
                    lbl_problema.configure(text=self.logic_tema_siete.problema_dos)
                    state["labels"] = ["P(A)", "P(B)", "P(C)", "P(A ∩ B)", "P(A ∩ C)", "P(B ∩ C)", "P(A ∩ B ∩ C)"]
                else:
                    lbl_problema.configure(text=self.logic_tema_siete.problema_tres)
                    state["labels"] = ["P(A)", "P(B)", "P(C)", "P(D)",
                                       "P(A ∩ B)", "P(A ∩ C)", "P(A ∩ D)", "P(B ∩ C)", "P(B ∩ D)", "P(C ∩ D)",
                                       "P(A ∩ B ∩ C)", "P(A ∩ B ∩ D)", "P(A ∩ C ∩ D)", "P(B ∩ C ∩ D)",
                                       "P(A ∩ B ∩ C ∩ D)"]
                render_step()
                
            self.create_option_menu("Selecciona el caso", opciones, "caso_tema_siete", command=update_tema_siete_case)
            wizard_frame.pack_forget() # Repack after option menu
            wizard_frame.pack(fill="x", padx=20, pady=(5, 10))
            update_tema_siete_case("2 Eventos (A, B)")

        elif "Tema Ocho" == new_method:
            lbl_problema = ctk.CTkLabel(self.input_container, text=self.logic_tema_ocho.problema, font=ctk.CTkFont(size=14), text_color=TEXT_COLOR, wraplength=650, justify="left")
            lbl_problema.pack(pady=(10, 10), padx=20, anchor="w", fill="x")
            
            self.create_horizontal_pair("Cantidad de chocolates", ["Cajeta", "Menta"], ["cant_cajeta", "cant_menta"])
            
            opciones = ["Cajeta", "Menta"]
            
            row_frame = ctk.CTkFrame(self.input_container, fg_color="transparent")
            row_frame.pack(fill="x", padx=20, pady=(5, 10))
            
            col1 = ctk.CTkFrame(row_frame, fg_color="transparent")
            col1.pack(side="left", fill="x", expand=True, padx=(0, 10))
            lbl1 = ctk.CTkLabel(col1, text="Primer chocolate", font=ctk.CTkFont(size=14), text_color=TEXT_COLOR)
            lbl1.pack(anchor="w")
            om1 = ctk.CTkOptionMenu(col1, values=opciones)
            om1.pack(fill="x", pady=(5, 0))
            self.entries["evento_a_t8"] = om1
            
            col2 = ctk.CTkFrame(row_frame, fg_color="transparent")
            col2.pack(side="left", fill="x", expand=True, padx=(10, 0))
            lbl2 = ctk.CTkLabel(col2, text="Segundo chocolate", font=ctk.CTkFont(size=14), text_color=TEXT_COLOR)
            lbl2.pack(anchor="w")
            om2 = ctk.CTkOptionMenu(col2, values=opciones)
            om2.pack(fill="x", pady=(5, 0))
            self.entries["evento_b_t8"] = om2


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
                
            elif method == "Tema Dos":
                caso_seleccionado = self.entries.get("caso_tema_dos")
                if caso_seleccionado:
                    caso_val = caso_seleccionado.get()
                    try:
                        prob_a = float(self.entries["prob_a_t2"].get())
                        if caso_val != "Eventos Complementarios":
                            prob_b = float(self.entries["prob_b_t2"].get())
                    except ValueError:
                        messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos en las casillas.")
                        return

                    self.result_textbox.configure(state="normal")
                    self.result_textbox.delete("1.0", "end")

                    if caso_val == "Eventos Disjuntos":
                        total = self.logic_tema_dos.calcular_probabilidad_eventos_disjuntos(prob_a, prob_b)
                        self.result_textbox.insert("end", f"Probabilidad Eventos Disjuntos:\n")
                        self.result_textbox.insert("end", f"P(A ∪ B) = P(A) + P(B) = {prob_a} + {prob_b} = {total:.4f}\n")
                    elif caso_val == "Eventos Complementarios":
                        total = self.logic_tema_dos.calcular_probabilidad_eventos_complementarios(prob_a)
                        self.result_textbox.insert("end", f"Probabilidad Evento Complementario:\n")
                        self.result_textbox.insert("end", f"P(A') = 1 - P(A) = 1 - {prob_a} = {total:.4f}\n")
                    else:
                        total = self.logic_tema_dos.calcular_probabilidad_eventos_compuestos(prob_a, prob_b)
                        self.result_textbox.insert("end", f"Probabilidad Eventos Compuestos (Independientes):\n")
                        self.result_textbox.insert("end", f"P(A ∩ B) = P(A) * P(B) = {prob_a} * {prob_b} = {total:.4f}\n")
                        
                    self.result_textbox.configure(state="disabled")

            elif method == "Tema Tres":
                prob_cond_uno, probabilidad = self.logic_tema_tres.calcular_probabilidad_condicional()
                
                self.result_textbox.configure(state="normal")
                self.result_textbox.delete("1.0", "end")
                
                procedimiento = (
                    f"1. Calcular la probabilidad conjunta P(ICO y Linux):\n"
                    f"   P(ICO y Linux) = P(ICO) * P(Linux|ICO)\n"
                    f"   P(ICO y Linux) = {self.logic_tema_tres.probabilidad_ICO} * {self.logic_tema_tres.probabilidad_ICO_y_Linux} = {prob_cond_uno:.4f}\n\n"
                    f"2. Calcular la probabilidad condicional P(ICO|Linux):\n"
                    f"   P(ICO|Linux) = P(ICO y Linux) / P(Linux)\n"
                    f"   P(ICO|Linux) = {prob_cond_uno:.4f} / {self.logic_tema_tres.probabilidad_Linux} = {probabilidad:.4f}\n\n"
                    f"Respuesta:\nLa probabilidad de que pertenezca a Ingeniería en Computación dado que usa Linux es {probabilidad:.2%}."
                )
                
                self.result_textbox.insert("end", procedimiento)
                self.result_textbox.configure(state="disabled")

            elif method == "Tema Cuatro":
                prob_uno, prob_dos, prob_total = self.logic_tema_cuatro.calcular_probabilidad()
                
                self.result_textbox.configure(state="normal")
                self.result_textbox.delete("1.0", "end")
                
                procedimiento = (
                    f"Teorema de Bayes - Procedimiento paso a paso:\n\n"
                    f"1. Calcular la probabilidad de que el pedido sea de DiDi y llegue tarde (Intersección):\n"
                    f"   P(DiDi ∩ Tarde) = P(DiDi) * P(Tarde | DiDi)\n"
                    f"   P(DiDi ∩ Tarde) = {self.logic_tema_cuatro.p_DiDiFood} * {self.logic_tema_cuatro.p_DiDiFood_tarde:.2f} = {prob_uno:.4f}\n\n"
                    f"2. Calcular la probabilidad total de que cualquier pedido llegue tarde (Probabilidad Total):\n"
                    f"   P(Tarde) = [P(Uber) * P(Tarde | Uber)] + [P(DiDi) * P(Tarde | DiDi)] + [P(Rappi) * P(Tarde | Rappi)]\n"
                    f"   P(Tarde) = [{self.logic_tema_cuatro.p_UberEats} * {self.logic_tema_cuatro.p_UberEats_tarde:.2f}] + "
                    f"[{self.logic_tema_cuatro.p_DiDiFood} * {self.logic_tema_cuatro.p_DiDiFood_tarde:.2f}] + "
                    f"[{self.logic_tema_cuatro.p_Rappi} * {self.logic_tema_cuatro.p_Rappi_tarde:.2f}]\n"
                    f"   P(Tarde) = {prob_dos:.4f}\n\n"
                    f"3. Aplicar el Teorema de Bayes para hallar la probabilidad condicional:\n"
                    f"   P(DiDi | Tarde) = P(DiDi ∩ Tarde) / P(Tarde)\n"
                    f"   P(DiDi | Tarde) = {prob_uno:.4f} / {prob_dos:.4f} = {prob_total:.4f}\n\n"
                    f"Respuesta:\nLa probabilidad de que el pedido tarde haya sido entregado por DiDi Food es {prob_total:.2%}."
                )
                
                self.result_textbox.insert("end", procedimiento)
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

            elif method == "Tema Seis":
                try:
                    prob_normal = float(self.entries["prob_normal"].get())
                    prob_a = float(self.entries["prob_a"].get())
                    prob_b = float(self.entries["prob_b"].get())
                except ValueError:
                    messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos en las 3 casillas.")
                    return
                
                self.logic_tema_seis = TemaSeis()
                self.logic_tema_seis.probabilidad_programada = prob_normal
                self.logic_tema_seis.probabilidad_evento_A = prob_a
                self.logic_tema_seis.probabilidad_evento_B = prob_b
                
                caso_seleccionado = self.entries.get("caso_tema_seis")
                if caso_seleccionado:
                    caso_val = caso_seleccionado.get()
                    if caso_val == "Evento A":
                        total = self.logic_tema_seis.calcular_evento_A()
                    else:
                        total = self.logic_tema_seis.calcular_evento_B()
                    
                    restante = self.logic_tema_seis.probabilidad_restante
                    
                    self.result_textbox.configure(state="normal")
                    self.result_textbox.delete("1.0", "end")
                    self.result_textbox.insert("end", f"Probabilidad Total: {total:.4f}\n")
                    self.result_textbox.configure(state="disabled")

            elif method == "Tema Siete":
                state = self.tema_siete_state
                if state["step"] < len(state["labels"]):
                    messagebox.showerror("Error", "Faltan valores por ingresar. Termina todos los pasos.")
                    return
                
                case = state["case"]
                
                self.result_textbox.configure(state="normal")
                self.result_textbox.delete("1.0", "end")
                
                if case == "2 Eventos (A, B)":
                    self.logic_tema_siete.probabilidades_uno = state["values"]
                    prob = self.logic_tema_siete.calcular_probabilidad_dos_eventos()
                    proc = f"Regla Aditiva (2 Eventos):\n\nP(A U B) = P(A) + P(B) - P(A ∩ B)\nP(A U B) = {state['values'][0]} + {state['values'][1]} - {state['values'][2]}\n= {prob:.4f}"
                elif case == "3 Eventos (A, B, C)":
                    self.logic_tema_siete.probabilidades_dos = state["values"]
                    prob = self.logic_tema_siete.calcular_probabilidad_tres_eventos()
                    v = state["values"]
                    proc = (f"Regla Aditiva (3 Eventos):\n\nP(A U B U C) = P(A) + P(B) + P(C) - P(A ∩ B) - P(A ∩ C) - P(B ∩ C) + P(A ∩ B ∩ C)\n"
                            f"P(A U B U C) = {v[0]} + {v[1]} + {v[2]} - {v[3]} - {v[4]} - {v[5]} + {v[6]}\n= {prob:.4f}")
                else:
                    self.logic_tema_siete.probabilidades_tres = state["values"]
                    prob = self.logic_tema_siete.calcular_probabilidad_cuatro_eventos()
                    v = state["values"]
                    proc = (f"Regla Aditiva (4 Eventos):\n\n"
                            f"P(A U B U C U D) = P(A) + P(B) + P(C) + P(D)\n"
                            f"                 - P(A ∩ B) - P(A ∩ C) - P(A ∩ D) - P(B ∩ C) - P(B ∩ D) - P(C ∩ D)\n"
                            f"                 + P(A ∩ B ∩ C) + P(A ∩ B ∩ D) + P(A ∩ C ∩ D) + P(B ∩ C ∩ D)\n"
                            f"                 - P(A ∩ B ∩ C ∩ D)\n\n"
                            f"Sustituyendo:\n"
                            f"P = {v[0]} + {v[1]} + {v[2]} + {v[3]}\n"
                            f"  - {v[4]} - {v[5]} - {v[6]} - {v[7]} - {v[8]} - {v[9]}\n"
                            f"  + {v[10]} + {v[11]} + {v[12]} + {v[13]}\n"
                            f"  - {v[14]}\n= {prob:.4f}")
                            
                self.result_textbox.insert("end", proc)
                self.result_textbox.configure(state="disabled")

            elif method == "Tema Ocho":
                try:
                    cajeta = int(self.entries["cant_cajeta"].get())
                    menta = int(self.entries["cant_menta"].get())
                except ValueError:
                    messagebox.showerror("Error", "Por favor ingresa cantidades enteras válidas en Cajeta y Menta.")
                    return
                
                self.logic_tema_ocho.cantidad_cajeta = cajeta
                self.logic_tema_ocho.cantidad_menta = menta
                
                ev_a = self.entries["evento_a_t8"].get()
                ev_b = self.entries["evento_b_t8"].get()
                
                self.logic_tema_ocho.evento_a = 1 if ev_a == "Cajeta" else 2
                self.logic_tema_ocho.evento_b = 1 if ev_b == "Cajeta" else 2
                
                prob, proc = self.logic_tema_ocho.calcular_probabilidad()
                
                self.result_textbox.configure(state="normal")
                self.result_textbox.delete("1.0", "end")
                self.result_textbox.insert("end", proc)
                self.result_textbox.insert("end", f"\nRespuesta:\nLa probabilidad de sacar {ev_a} y luego {ev_b} es {prob:.2%}.")
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