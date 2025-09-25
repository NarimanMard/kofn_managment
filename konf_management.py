import tkinter as tk

class CommandLineEmulator(tk.Tk):
    def __init__(self):
        super().__init__()
# 1 ркно
        self.title("VFS")
        self.wm_attributes("-fullscreen", True)  # Открываем окно на весь экран
        self.output = tk.Text(self, bg="#000000", fg="white", insertbackground="white", font=("Arial", 18))
        self.output.pack(fill=tk.BOTH, expand=True)
        self.output.config(state="disabled")  # Сделаем поле вывода неактивным
    
# Виджет для ввода команд
        input_frame = tk.Frame(self)
        input_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.input_field = tk.Entry(input_frame, bg="#000000", fg="white",insertbackground="white", font=("Courier New", 20))
        self.input_field.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=10)
        self.input_field.bind("<Return>", lambda event: self.execute_command())

# Ставим фокус на поле ввода при запуске
        self.input_field.focus_set()

# Кнопка отправки команды
        submit_button = tk.Button(input_frame, text="Выполнить", font=("Arial", 15), height=2, width=15, bg="#5c5c5c", fg="white", 
                                  activebackground="#7b7b7b", relief=tk.RAISED, borderwidth=25, command=self.execute_command)
        submit_button.pack(side=tk.RIGHT)

#обработка ввод команд :
    def execute_command(self):
        user_input = self.input_field.get()
        if not user_input.strip():
            return
#3
        try:
            cmd_parts = user_input.split() 
            command = cmd_parts[0]
            args = cmd_parts[1:]
            
            output = f"~💲 {command} {' '.join(args)}\n"
            if command == 'ls':
                output += f"{command}: {' '.join(args)}\n"
            elif command == 'cd':
                output += f"{command}: {' '.join(args)}\n"
            elif command == 'exit':
                self.destroy()
            elif command == "echo":
                output += f"{' '.join(args)}😬\n"
            else:
                output += f"Ошибка: неизвестная команда '{command}'🤔\n"
                
            self.display_output(output)
        except Exception as e:
            self.display_output(f"Ошибка выполнения команды: {e}😒")
    
        finally:
            self.input_field.delete(0, tk.END)
    
    def display_output(self, message):
        """Отображает сообщение в области вывода"""
        self.output.config(state='normal')
        self.output.insert('end', message + "\n")
        self.output.see('end')  # Прокручиваем вниз
        self.output.config(state='disabled')
if __name__ == "__main__":
    app = CommandLineEmulator()
    app.mainloop()