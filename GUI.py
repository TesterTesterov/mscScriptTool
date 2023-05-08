import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import os

from mscScript import mscScript
from mscScript import ItsNotMsc
from inputDialog import inputDialog

class GUI():
    text_dict = {
        'rus': ['mscScriptTool от Tester-а',
                'Русский', 'English', '(Дизз)ассемблирование', '(Де)шифровка', 'Помощь:',
                'Общая', 'По использованию', 'По созданию переносов', 'Тестовая строка',
                '...', '(Де)шифровать', 'Скрипты msc', '*.msc', 'Все файлы', '*',
                'Коль файл шифрован, он будет дешифрован, и наоборот.\nПрограмма сама сделает о том заключение.',
                'Введите имя файла .msc (при необх. с путём) (с расширением):',
                'Заданный файл невозможно открыть, либо он не существует.',
                'Заданный файл не является скриптом .msc.',
                'Дешифровка окончилась неудачно.',
                'Дешифровка окончилась успешно!\nИтоговый файл:\n{}\nКлюч шифрования:\n{}',
                'Шифровка окончилась неудачно.',
                'Шифровка окончилась успешно!\nИтоговый файл:\n{}\nКлюч шифрования:\n{}',
                'Ключ не обнаружен!',
                'Введите ключ (в формате 0xNN, где N есть шестнадцатеричные цифры):',
                'Ввести ключ',
                'Ключ некорректен!',
                'Введите имя файла .msc (при необх. с путём) (с расширением):',
                '...',
                'Введите имя файла .txt (при необх. с путём) (с расширением):',
                '...',
                'Версия скрипта:',
                'Кодировка скрипта:',
                'Разобрать скрипт',
                'Собрать скрипт',
                'Анализировать версию скрипта',
                'Проведите сборку и/или разборку скрипта .msc движка StuffScript.\n'
                '- Все смещения средство перестраивает автоматически.\n'
                '- Все номера сообщений средство перестраивает\nавтоматически.\n'
                'Существует две версии сих скриптов:\n'
                '- 0 в ранних, таких как Пули да дворецкие.\n'
                '- 1 в поздних, таких как Просвет средь сакур и город\nобмана.\n'
                'Можете как попробовать обе, так и проанализировать\nскрипт.\n'
                'Если ни одна не работает, расшифруйте скрипт в соседнем\n'
                'разделе.',
                'Текстовые файлы', '*.txt', 'Все файлы', '*',
                'Анализ прошёл успешно!\nВерсия скрипта: {}.',
                'Не удалось выполнить анализ.\nВозможно, скрипт зашифрован?',
                'Скрипт успешно разобран!',
                'Скрипт разобрать не удалось.\nБыть может, он зашифрован?',
                'Скрипт успешно собран!',
                'Скрипт не удалось собрать.\nСкорее всего где-то в коде ошибка.',
                'Общая помощь',
                '''Двуязычное (рус+англ) средство для разборки и сборки скриптов .msc движка визуальных новелл Stuff Script, известного также как Propeller Engine.\nС ним вы можете полностью редактирвоать код, а не только строки, как с ранее существовшими средствами.\nВы можете добавлять разрывы текста по строкам и даже сообщениям без ограничений!\n\nВ нём есть несколько полезных особенностей.\n- Во-первых, во время сборки все номера сообщений пересчитываются.\n- Во-вторых, можно делать комментарии, при этом в начало строки необходимо ставить "$".\n- В-третьих, опишем некоторые определения: "#0-" есть "вольные байты", "#1-" есть команды (и под ними "\[...]" аргументы) и "#2-"/"#3-" есть метки.''',
                'Помощь по использованию',
                '''1. Введите название файла .mes в верхней форме (заметьте, с расширением). Также можно вводить относительный или абсолютный до него путь.\n1.1. Совершенно так же, а также после нажатия на кнопку "(Де)шифровать" на панели (де)шифровки вы можете расшифровать или зашифровать скрипт, коли вам то требуется.\n2. Введите название файла .txt в нижней форме (заметьте, с расширением). Также можно вводить относительный или абсолютный до него путь.\n2.1. Также опционально вы можете нажать на кнопку "Анализировать скрипт", дабы узнать его версию и зашифрован ли он.\n3. Для разборки нажмите на кнопку "Разобрать скрипт".\n4. Для сборки нажмите на кнопку "Собрать скрипт".\n5. Статус сих операций будет отображаться на текстовом поле ниже.''',
                'Помощь по переносам',
                '''Иногда можно столкнуться с одной большой-пребольшой проблемой: текст может не полностью влезать в текстовое окно. Однако, с сим средством вам не нужно обрезать его, отнюдь. Вы можеет организовывать переносы по строкам и сообщениям. Методы указаны ниже.\n- Для переносов по строкам добавьте в текущее сообщение следующий тэг (работает корректно до выполнения автопереноса по символам).\n\n_r\n\n- Для переносов по сообщениям добавьте под текущее сообщение следующий код (вместо "Какая_то_строка" вставьте ваше сообщение).\n\n#1-MESSAGE\n[0, 0, 'Какая_то_строка_r']'''],

        'eng': ['mscScriptTool by Tester',
                'Русский', 'English', '(Diss)assembling', '(De)cryption', 'Help:',
                'Common', 'About usage', 'About line/message breaks', 'TestLine',
                '...', '(De)crypt', 'Msc scripts', '*.msc', 'All files', '*',
                'If the file is encrypted, then it will be decrypted,\nand otherwise.\nThe program will conclude it itself.',
                'Enter the .msc file name (with path to it if needed) (with extension):',
                'File with this name is impossible to open, or there is\nno such file.',
                'File with this name is not a .msc script.',
                'Decryption failed.',
                'Decryption succeed!\nDestination file:\n{}\nEncryption key:\n{}',
                'Encryption failed.',
                'Encryption succeed!\nDestination file:\n{}\nEncryption key:\n{}',
                'Key is not found!',
                'Enter key (in format 0xNN, N is hex number):',
                'Enter the key',
                'The key is incorrect!',
                'Enter the .msc file name (with path to it if needed) (with extension):',
                '...',
                'Enter the .txt file name (with path to it if needed) (with extension):',
                '...',
                'Script\'s version:',
                'Script\'s encoding:',
                'Disassemble script',
                'Assemble script',
                'Analyze the script\'s version',
                'Assemble or/and disassemble .msc script of StuffScript\nEngine.\n'
                '- All offsets are rebuiled by the tool.\n'
                '- All message numbers are rebuilded by the tool.\n'
                'There are two versions of this script format:\n'
                '- 0, in old ones, for example Bullet Butlers.\n'
                '- 1, in later ones, for example Sukimazakura to Uso no\nMachi.\n'
                'Thou can just try both or analyze the script.\n'
                'If thou can\'t (dis)assemble script with both ones,\n'
                'just decrypt it in the next section.',
                'Text files', '*.txt', 'All files', '*',
                'Analysis succeed!\nThe script\'s version: {}.',
                'The script\'s analysis failed.\nMaybe it\'s encrypted?',
                'Disassembling succeed!',
                'Disassembling failed.\nMaybe the script is encrypted?',
                'Assembling succeed!',
                'Assembling failed.\nThere is a bug somewhere in the .txt.',
                'Common help',
                '''Dual languaged (rus+eng) tool for disassembling and assembling scripts .mes from the visual novel's engine Stuff Script Engine.\nWith it thou can fully edit code, not just strings, as with some earlier tools.\nThou can add line or even message breaks without restrictions!\n\nIt has some useful features.\n- Firstly, during disassembling all opcodes '\x0A' changes to '\x0B', so the engine wouldn't try to decrypt new strings and break latin and half-width kana symbols.\n- Secondly, thou can make comments in txt file with "$" at the beginning of the string.\n- Thirdly, some definations: "#0-" are "free bytes", "#1-" are commands (and "\[...]" are arguments below) and "#2-" are labels.''',
                'Usage help',
                '''1. Enter a title of the .msc file in the top entry (do see, with extension). Thou can also enter relative or absolute path.\n1.1. Just as so and after pushing the "(De)crypt" bytton thou can use (de)cryption panel to decrypt or encrypt script as needed.\n2. Enter a title of the .txt file (do see, with extension). Thou can also enter relative or absolute path.\n2.1. After that thou can optionaly to push the button "Analyze script" to get to know it's version or if it's encrypted.\n3. For dissassemble push the button "Disassemble script".\n4. For assemble push the button "Assemble script".\n5. Status will be displayed on the text area below.''',
                'Line/message breaks help',
                '''Sometimes there could be a very big problem: text may not fully get in textbox. But with this tool thou don't need to cut some part of text, no. Thou can use line and message breaks. Methods are below.\n- For line breaks insert in the current message this tag (works correctly only before the autolinebreak).\n\n_r\n\n- For message breaks insert this below the current message ('SomeString' -> text on the new message).\n\n#1-MESSAGE\n[0, 0, 'SomeString_r']''']
    }

    def __init__(self):
        self.__window = tk.Tk()
        self.__width = 500
        self.__height = 500
        self.__possible_versions = [0, 1]
        self.__lang = 'eng'
        self.__currentPanel = 0
        self.__mode = tk.StringVar()
        self.__encoding = tk.StringVar()
        self.__fileCrypto = tk.StringVar()
        self.__mscFile = tk.StringVar()
        self.__txtFile = tk.StringVar()
        self.__window.geometry('{}x{}+{}+{}'.format(
            self.__width,
            self.__height,
            self.__window.winfo_screenwidth()//2-self.__width//2,
            self.__window.winfo_screenheight()//2-self.__height//2))
        self.__window.resizable(width=False, height=False)
        self.__window["bg"] = 'grey'

        self.__topButtons = []
        self.__topButtons.append(tk.Button(master=self.__window,
                                           command=self.__toRussian,
                                           relief=tk.RAISED,
                                           font=('Helvetica', 14)))
        self.__topButtons.append(tk.Button(master=self.__window,
                                           command=self.__toEnglish,
                                           relief=tk.RAISED,
                                           font=('Helvetica', 14)))
        self.__topButtons[0].place(relx=0.0, rely=0.0, relwidth=0.5, relheight=0.1)
        self.__topButtons[1].place(relx=0.5, rely=0.0, relwidth=0.5, relheight=0.1)
        self.__razdelButtons = []
        self.__razdelButtons.append(tk.Button(master=self.__window,
                                           command=self.__toZeroFrame,
                                           relief=tk.RAISED,
                                           borderwidth=10,
                                           font=('Helvetica', 14)))
        self.__razdelButtons.append(tk.Button(master=self.__window,
                                           command=self.__toFirstFrame,
                                           relief=tk.RAISED,
                                           borderwidth=10,
                                           font=('Helvetica', 14)))
        self.__razdelButtons[0].place(relx=0.0, rely=0.115, relwidth=0.5, relheight=0.1)
        self.__razdelButtons[1].place(relx=0.5, rely=0.115, relwidth=0.5, relheight=0.1)

        self.__lblpnlHelp = tk.LabelFrame(master=self.__window,
                                           relief=tk.RAISED,
                                           font=('Helvetica', 14),
                                           borderwidth=10)
        self.__btn_helps = []
        for i in range(4):
            self.__btn_helps.append(tk.Button(
                master=self.__lblpnlHelp,
                font=('Helvetica', 12)
            ))
        self.__btn_helps[0]["command"] = self.__commonHelp
        self.__btn_helps[1]["command"] = self.__usageHelp
        self.__btn_helps[2]["command"] = self.__breakHelp
        self.__btn_helps[0].place(relx=0.0, rely=0.0, relwidth=0.5, relheight=0.5)
        self.__btn_helps[1].place(relx=0.5, rely=0.0, relwidth=0.5, relheight=0.5)
        self.__btn_helps[2].place(relx=0.0, rely=0.5, relwidth=1.0, relheight=0.5)
        self.__lblpnlHelp.place(relx=0.0, rely=0.8, relwidth=1.0, relheight=0.2)

        self.__frm = []
        self.__frm.append(tk.Frame(
            master=self.__window,
            background='white',
            relief=tk.RAISED,
            borderwidth=10
        ))
        self.__frm.append(tk.Frame(
            master=self.__window,
            background='white',
            relief=tk.RAISED,
            borderwidth=10
        ))

        ##Первая панель:
        self.__lbl_inputfile = tk.Label(
            master=self.__frm[1],
            bg='white',
            font=('Helvetica', 12)
        )
        self.__ent_crypto = tk.Entry(
            master=self.__frm[1],
            textvariable=self.__fileCrypto,
            borderwidth=5
        )
        self.__what_file_crypto = tk.Button(
            master=self.__frm[1],
            command=self.__what_file_crypto,
            relief=tk.RAISED,
            font=('Helvetica', 14)
        )
        self.__btn_crypto = tk.Button(
            master=self.__frm[1],
            command=self.__crypter,
            relief=tk.RAISED,
            font=('Helvetica', 14)
        )
        self.__txt_crypto = tk.Text(
            master=self.__frm[1],
            bg='white',
            state=tk.DISABLED
        )
        self.__lbl_inputfile.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.1)
        self.__ent_crypto.place(relx=0.0, rely=0.1, relwidth=0.85, relheight=0.1)
        self.__what_file_crypto.place(relx=0.85, rely=0.1, relwidth=0.15, relheight=0.1)
        self.__btn_crypto.place(relx=0.0, rely=0.2, relwidth=1.0, relheight=0.1)
        self.__txt_crypto.place(relx=0.0, rely=0.3, relwidth=1.0, relheight=0.7)

        #Нулевая панель:
        self.__lbl_input_msc_file = tk.Label(
            master=self.__frm[0],
            bg='white',
            font=('Helvetica', 12)
        )
        self.__ent_msc_file = tk.Entry(
            master=self.__frm[0],
            textvariable=self.__mscFile,
            borderwidth=5
        )
        self.__btn_what_file_msc = tk.Button(
            master=self.__frm[0],
            relief=tk.RAISED,
            font=('Helvetica', 14),
            command=self.__what_msc_file
        )
        self.__lbl_input_txt_file = tk.Label(
            master=self.__frm[0],
            bg='white',
            font=('Helvetica', 12)
        )
        self.__ent_txt_file = tk.Entry(
            master=self.__frm[0],
            textvariable=self.__txtFile,
            borderwidth=5
        )
        self.__btn_what_file_txt = tk.Button(
            master=self.__frm[0],
            relief=tk.RAISED,
            font=('Helvetica', 14),
            command=self.__what_txt_file
        )
        self.__lbl_what_version = tk.Label(
            master=self.__frm[0],
            bg='white',
            font=('Helvetica', 12)
        )
        self.__cmb_choose_version = ttk.Combobox(
            master=self.__frm[0],
            font=('Helvetica', 14),
            values=self.__possible_versions,
            textvariable=self.__mode,
            state='readonly'
        )
        self.__lbl_what_encoding = tk.Label(
            master=self.__frm[0],
            bg='white',
            font=('Helvetica', 12)
        )
        self.__cmb_choose_encoding = ttk.Combobox(
            master=self.__frm[0],
            font=('Helvetica', 14),
            values=['cp932', 'cp1251', 'utf-8'],
            textvariable=self.__encoding,
            state='readonly'
        )
        self.__encoding.set('cp932')
        self.__mode.set(self.__possible_versions[0])
        self.__btn_disassembler = tk.Button(
            master=self.__frm[0],
            relief=tk.RAISED,
            font=('Helvetica', 14),
            command=self.__disassemble_script
        )
        self.__btn_assembler = tk.Button(
            master=self.__frm[0],
            relief=tk.RAISED,
            font=('Helvetica', 14),
            command=self.__assemble_script
        )
        self.__btn_analyzer = tk.Button(
            master=self.__frm[0],
            relief=tk.RAISED,
            font=('Helvetica', 14),
            command=self.__get_script_version
        )
        self.__scroll_txt_assembler = tk.Scrollbar(
            master=self.__frm[0],
            orient='vertical'
        )
        self.__txt_assembler = tk.Text(
            master=self.__frm[0],
            bg='white',
            state=tk.DISABLED,
            yscrollcommand=self.__scroll_txt_assembler.set,
        )
        self.__scroll_txt_assembler["command"] = self.__txt_assembler.yview
        self.__lbl_input_msc_file.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.1)
        self.__ent_msc_file.place(relx=0.0, rely=0.1, relwidth=0.85, relheight=0.1)
        self.__btn_what_file_msc.place(relx=0.85, rely=0.1, relwidth=0.15, relheight=0.1)
        self.__lbl_input_txt_file.place(relx=0.0, rely=0.2, relwidth=1.0, relheight=0.1)
        self.__ent_txt_file.place(relx=0.0, rely=0.3, relwidth=0.85, relheight=0.1)
        self.__btn_what_file_txt.place(relx=0.85, rely=0.3, relwidth=0.15, relheight=0.1)
        self.__lbl_what_version.place(relx=0.0, rely=0.4, relwidth=0.3, relheight=0.1)
        self.__cmb_choose_version.place(relx=0.3, rely=0.4, relwidth=0.1, relheight=0.1)
        self.__lbl_what_encoding.place(relx=0.4, rely=0.4, relwidth=0.3, relheight=0.1)
        self.__cmb_choose_encoding.place(relx=0.7, rely=0.4, relwidth=0.3, relheight=0.1)
        self.__btn_disassembler.place(relx=0.0, rely=0.5, relwidth=0.5, relheight=0.1)
        self.__btn_assembler.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.1)
        self.__btn_analyzer.place(relx=0.0, rely=0.6, relwidth=1.0, relheight=0.1)
        self.__txt_assembler.place(relx=0.0, rely=0.7, relwidth=0.96, relheight=0.3)
        self.__scroll_txt_assembler.place(relx=0.96, rely=0.7, relwidth=0.04, relheight=0.3)

        self.__toEnglish()
        self.__changeFrame()

        self.__window.mainloop()
    def __toRussian(self):
        self.__changeLang("rus")
    def __toEnglish(self):
        self.__changeLang("eng")
    def __toZeroFrame(self):
        self.__currentPanel = 0
        self.__changeFrame()
    def __toFirstFrame(self):
        self.__currentPanel = 1
        self.__changeFrame()
    def __changeFrame(self):
        other_frame = (self.__currentPanel + 1) % 2
        self.__razdelButtons[other_frame]["state"] = tk.NORMAL
        self.__razdelButtons[other_frame]["relief"] = tk.RAISED
        self.__razdelButtons[self.__currentPanel]["state"] = tk.DISABLED
        self.__razdelButtons[self.__currentPanel]["relief"] = tk.SUNKEN
        self.__frm[other_frame].place_forget()
        self.__frm[self.__currentPanel].place(relx=0.0, rely=0.215, relwidth=1.0, relheight=0.575)
    def __changeLang(self, lang : str):
        self.__lang = lang
        self.__window.title(self.text_dict[self.__lang][0])
        self.__topButtons[0]["text"] = self.text_dict[self.__lang][1]
        self.__topButtons[1]["text"] = self.text_dict[self.__lang][2]
        self.__razdelButtons[0]["text"] = self.text_dict[self.__lang][3]
        self.__razdelButtons[1]["text"] = self.text_dict[self.__lang][4]
        self.__lblpnlHelp["text"] = self.text_dict[self.__lang][5]
        for i in range(4):
            self.__btn_helps[i]["text"] = self.text_dict[self.__lang][i+6]
        self.__what_file_crypto["text"] = self.text_dict[self.__lang][10]
        self.__btn_crypto["text"] = self.text_dict[self.__lang][11]
        self.__txt_crypto["state"] = tk.NORMAL
        self.__txt_crypto.delete(1.0, tk.END)
        self.__txt_crypto.insert(1.0, self.text_dict[self.__lang][16])
        self.__txt_crypto["state"] = tk.DISABLED
        self.__lbl_inputfile["text"] = self.text_dict[self.__lang][17]
        self.__lbl_input_msc_file["text"] = self.text_dict[self.__lang][28]
        self.__btn_what_file_msc["text"] = self.text_dict[self.__lang][29]
        self.__lbl_input_txt_file["text"] = self.text_dict[self.__lang][30]
        self.__btn_what_file_txt["text"] = self.text_dict[self.__lang][31]
        self.__lbl_what_version["text"] = self.text_dict[self.__lang][32]
        self.__lbl_what_encoding["text"] = self.text_dict[self.__lang][33]
        self.__btn_disassembler["text"] = self.text_dict[self.__lang][34]
        self.__btn_assembler["text"] = self.text_dict[self.__lang][35]
        self.__btn_analyzer["text"] = self.text_dict[self.__lang][36]
        self.__txt_assembler["state"] = tk.NORMAL
        self.__txt_assembler.delete(1.0, tk.END)
        self.__txt_assembler.insert(1.0, self.text_dict[self.__lang][37])
        self.__txt_assembler["state"] = tk.DISABLED

    def __commonHelp(self):
        messagebox.showinfo(self.text_dict[self.__lang][48], self.text_dict[self.__lang][49])
    def __usageHelp(self):
        messagebox.showinfo(self.text_dict[self.__lang][50], self.text_dict[self.__lang][51])
    def __breakHelp(self):
        messagebox.showinfo(self.text_dict[self.__lang][52], self.text_dict[self.__lang][53])

    def __crypter(self):
        filer = self.__fileCrypto.get()
        try:
            file_analyze = mscScript(filer, '', int(self.__mode.get()), self.__encoding.get())
            is_key = file_analyze.analyzeScript()
            if (is_key == 0):
                key = 0
                try:
                    file_key = open(filer + '.key')
                    key = int(file_key.readline())
                except:
                    new_dialog = inputDialog(self.text_dict[self.__lang][24],
                                             self.text_dict[self.__lang][25],
                                             self.text_dict[self.__lang][26])
                    try:
                        key = int(new_dialog.show()[2:], 16)
                    except:
                        self.__txt_crypto["state"] = tk.NORMAL
                        self.__txt_crypto.delete(1.0, tk.END)
                        self.__txt_crypto.insert(1.0, self.text_dict[self.__lang][26])
                        self.__txt_crypto["state"] = tk.DISABLED
                        del new_dialog
                        return False
                try:
                    end_file = ''
                    file_analyze.cryptScript(key)
                    try:
                        os.rename(filer, filer + '.old')
                    except:
                        try:
                            os.remove(filer)
                        except:
                            end_file = filer + '.testercrypt333'
                    if (end_file == ''):
                        try:
                            os.rename(filer + '.testercrypt333', filer)
                            end_file = filer
                        except:
                            end_file = filer + '.testercrypt333'
                    self.__txt_crypto["state"] = tk.NORMAL
                    self.__txt_crypto.delete(1.0, tk.END)
                    self.__txt_crypto.insert(1.0, self.text_dict[self.__lang][23].replace('{}', end_file, 1).replace('{}', hex(key), 1))
                    self.__txt_crypto["state"] = tk.DISABLED
                    key_file = open(end_file + '.key', 'w')
                    key_file.write(str(key))
                    key_file.close()
                except:
                    self.__txt_crypto["state"] = tk.NORMAL
                    self.__txt_crypto.delete(1.0, tk.END)
                    self.__txt_crypto.insert(1.0, self.text_dict[self.__lang][22])
                    self.__txt_crypto["state"] = tk.DISABLED
                finally:
                    del file_analyze
            else:
                try:
                    end_file = ''
                    file_analyze.cryptScript(is_key)
                    try:
                        os.rename(filer, filer + '.old')
                    except:
                        try:
                            os.remove(filer)
                        except:
                            end_file = filer + '.testercrypt333'
                    if (end_file == ''):
                        try:
                            os.rename(filer + '.testercrypt333', filer)
                            end_file = filer
                        except:
                            end_file = filer + '.testercrypt333'
                    self.__txt_crypto["state"] = tk.NORMAL
                    self.__txt_crypto.delete(1.0, tk.END)
                    self.__txt_crypto.insert(1.0, self.text_dict[self.__lang][21].format(end_file, hex(is_key)))
                    self.__txt_crypto["state"] = tk.DISABLED
                    key_file = open(end_file + '.key', 'w')
                    key_file.write(str(is_key))
                    key_file.close()
                except:
                    self.__txt_crypto["state"] = tk.NORMAL
                    self.__txt_crypto.delete(1.0, tk.END)
                    self.__txt_crypto.insert(1.0, self.text_dict[self.__lang][20])
                    self.__txt_crypto["state"] = tk.DISABLED
                finally:
                    del file_analyze
        except FileNotFoundError:
            self.__txt_crypto["state"] = tk.NORMAL
            self.__txt_crypto.delete(1.0, tk.END)
            self.__txt_crypto.insert(1.0, self.text_dict[self.__lang][18])
            self.__txt_crypto["state"] = tk.DISABLED
            self.__fileCrypto.set('')
        except ItsNotMsc:
            self.__txt_crypto["state"] = tk.NORMAL
            self.__txt_crypto.delete(1.0, tk.END)
            self.__txt_crypto.insert(1.0, self.text_dict[self.__lang][19])
            self.__txt_crypto["state"] = tk.DISABLED
            self.__fileCrypto.set('')

    def __what_file_crypto(self):
        ftypes = [(self.text_dict[self.__lang][12], self.text_dict[self.__lang][13]), (self.text_dict[self.__lang][14], self.text_dict[self.__lang][15])]
        dialg = filedialog.Open(self.__window, filetypes=ftypes, initialdir=os.getcwd())
        file = dialg.show()
        if (file != ''):
            self.__fileCrypto.set(file)
    def __what_msc_file(self):
        ftypes = [(self.text_dict[self.__lang][12], self.text_dict[self.__lang][13]), (self.text_dict[self.__lang][14], self.text_dict[self.__lang][15])]
        dialg = filedialog.Open(self.__window, filetypes=ftypes, initialdir=os.getcwd())
        file = dialg.show()
        if (file != ''):
            self.__mscFile.set(file)
    def __what_txt_file(self):
        ftypes = [(self.text_dict[self.__lang][38], self.text_dict[self.__lang][39]), (self.text_dict[self.__lang][40], self.text_dict[self.__lang][41])]
        dialg = filedialog.Open(self.__window, filetypes=ftypes, initialdir=os.getcwd())
        file = dialg.show()
        if (file != ''):
            self.__txtFile.set(file)
    def __get_script_version(self):
        version = -1
        for i in self.__possible_versions:
            try:
                try:
                    del new_script
                except:
                    pass
                new_script = mscScript(self.__mscFile.get(), self.__mscFile.get() + '.thisfileshouldnotexist',
                                       i, self.__encoding.get())
                new_script.just_diss_header()
                version = i
                del new_script
                break
            except Exception as ex:
                continue
        if (version == -1):
            self.__txt_assembler["state"] = tk.NORMAL
            self.__txt_assembler.delete(1.0, tk.END)
            self.__txt_assembler.insert(1.0, self.text_dict[self.__lang][43])
            self.__txt_assembler["state"] = tk.DISABLED
        else:
            self.__mode.set(version)
            self.__txt_assembler["state"] = tk.NORMAL
            self.__txt_assembler.delete(1.0, tk.END)
            self.__txt_assembler.insert(1.0, self.text_dict[self.__lang][42].format(version))
            self.__txt_assembler["state"] = tk.DISABLED
    def __disassemble_script(self):
        try:
            newScript = mscScript(self.__mscFile.get(), self.__txtFile.get(),
                                  int(self.__mode.get()), self.__encoding.get())
            newScript.disassemble()
            newScript.show_data()
            del newScript
            self.__txt_assembler["state"] = tk.NORMAL
            self.__txt_assembler.delete(1.0, tk.END)
            self.__txt_assembler.insert(1.0, self.text_dict[self.__lang][44])
            self.__txt_assembler["state"] = tk.DISABLED
        except Exception as ex:
            try:
                del newScript
            except:
                pass
            print(ex)
            self.__txt_assembler["state"] = tk.NORMAL
            self.__txt_assembler.delete(1.0, tk.END)
            self.__txt_assembler.insert(1.0, self.text_dict[self.__lang][45])
            self.__txt_assembler["state"] = tk.DISABLED
    def __assemble_script(self):
        try:
            newScript = mscScript(self.__mscFile.get(), self.__txtFile.get(),
                                  int(self.__mode.get()), self.__encoding.get())
            newScript.assemble()
            newScript.show_data()
            del newScript
            self.__txt_assembler["state"] = tk.NORMAL
            self.__txt_assembler.delete(1.0, tk.END)
            self.__txt_assembler.insert(1.0, self.text_dict[self.__lang][46])
            self.__txt_assembler["state"] = tk.DISABLED
        except Exception as ex:
            try:
                del newScript
            except:
                pass
            print(ex)
            self.__txt_assembler["state"] = tk.NORMAL
            self.__txt_assembler.delete(1.0, tk.END)
            self.__txt_assembler.insert(1.0, self.text_dict[self.__lang][47])
            self.__txt_assembler["state"] = tk.DISABLED