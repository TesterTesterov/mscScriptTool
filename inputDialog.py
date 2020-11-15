import tkinter as tk

class inputDialog():
    def __init__(self, title, text, enter):
        self.__var = ''

        self.__title = title
        self.__txt = text
        self.__enter = enter
        self.__window = tk.Tk()
        self.__width = 300
        self.__height = 100
        self.__window.geometry('{}x{}+{}+{}'.format(
            self.__width,
            self.__height,
            self.__window.winfo_screenwidth()//2-self.__width//2,
            self.__window.winfo_screenheight()//2-self.__height//2))
        self.__window.title(self.__title)
        self.__window.resizable(width=False, height=False)

        self.__lbl_text = tk.Label(
            master=self.__window,
            text=self.__txt,
            font=('Helvetica', 10)
        )
        self.__ent_input = tk.Entry(
            master=self.__window,
            font=('Helvetica', 14)
        )
        self.__btn_enter = tk.Button(
            master=self.__window,
            text=self.__enter,
            command=self.__close,
            font=('Helvetica', 14)
        )
        self.__lbl_text.pack(expand=1, fill=tk.X)
        self.__ent_input.pack(expand=1, fill=tk.X)
        self.__btn_enter.pack()

    def show(self):
        self.__window.mainloop()
        try:
            self.__window.wait_window()
            return self.__var
        except:
            return self.__var
    def __close(self):
        self.__var = self.__ent_input.get()
        self.__window.quit()
        self.__window.destroy()