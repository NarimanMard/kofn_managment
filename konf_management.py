import tkinter as tk
import os
import argparse

class CommandLineEmulator(tk.Tk):
    def __init__(self, script_path=None):
        super().__init__()
        
        # Настройка окна
        self.title("VFS")
        self.wm_attributes("-fullscreen", True)  # Открываем окно на весь экран
        self.output = tk.Text(self, bg="#000000", fg="white", insertbackground="white", font=("Arial", 18))
        self.output.pack(fill=tk.BOTH, expand=True)
        self.output.config(state="disabled")  # Сделаем поле вывода неактивным
    
        # Виджет для ввода команд
        input_frame = tk.Frame(self)
        input_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.input_field = tk.Entry(input_frame, bg="#000000", fg="white", insertbackground="white", font=("Courier New", 20))
        self.input_field.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=10)
        self.input_field.bind("<Return>", lambda event: self.execute_command())

        # Ставим фокус на поле ввода при запуске
        self.input_field.focus_set()

        # Кнопка отправки команды
        submit_button = tk.Button(input_frame, text="Выполнить", font=("Arial", 15), height=2, width=15, bg="#5c5c5c", fg="white", 
                                  activebackground="#7b7b7b", relief=tk.RAISED, borderwidth=25, command=self.execute_command)
        submit_button.pack(side=tk.RIGHT)

        # Инициализация команд
        self.commands = {
            'ls': self.ls,
            'cd': self.cd,
            'exit': self.exit,
            'echo': self.echo
        }
        self.current_dir = os.getcwd()
        
        # Запуск эмулятора
        if script_path:
            self.run_script(script_path)
        else:
            self.display_output(f"{self.current_dir}~> ")

    def run_script(self, script_path):
        with open(script_path, 'r') as file:
            lines = file.readlines()
            print(lines)
            print(script_path)
            for line in lines:
                line = line.strip()
                if line.startswith('#'):
                    continue  # Пропускаем комментарии
                if line:
                    self.execute_command(line)

    def execute_command(self, command=None):
        if command is None:
            command = self.input_field.get()
            self.input_field.delete(0, tk.END)
        if not command.strip():
            return
    
        try:
            cmd_parts = command.split()
            cmd = cmd_parts[0]
            args = cmd_parts[1:]
            
            output = f"{self.current_dir}~💲 {command}\n"
            self.display_output(output)
            if cmd in self.commands:
                self.commands[cmd](args)
            else:
                output = f"Ошибка: неизвестная команда '{cmd}'🤔\n"
                self.display_output(output)

                
            
        except Exception as e:
            self.display_output(f"Ошибка выполнения команды: {e}😒")
    
    def ls(self, args):
        output = f"{' '.join(args)}\n"
        self.display_output(output)
        
    def cd(self, args):
        output = f"{' '.join(args)}\n"
        self.display_output(output)

    def exit(self, args):
        self.destroy()

    def echo(self, args):
        self.display_output(" ".join(args))

    def display_output(self, message):
        """Отображает сообщение в области вывода"""
        self.output.config(state='normal')
        self.output.insert('end', message + "\n")
        self.output.see('end')  # Прокручиваем вниз
        self.output.config(state='disabled')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Command Line Emulator")
    parser.add_argument("--script", help="Path to the script file to run")
    args = parser.parse_args()

    app = CommandLineEmulator(script_path=args.script)
    app.mainloop()