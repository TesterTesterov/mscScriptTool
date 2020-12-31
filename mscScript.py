import struct

class mscScript:
    #hex(' ') байтов, структура, название.
    CommandLibrary = [
            [ ##mode 0
                ["00 00", "BIh", "INIT"], #Bh/BhI/BhH // BIh //BIhhhB
                ["00 01", "BBhHBhH", "JUMP_1"], #BBBBBBBBBBB
                ["00 02", "Bh", "JUMP_2"], #BI #BHH
                ["00 03", "Bh", ""],
                ["00 04", "", "RETURN"],
                ["00 05", "BhB", "PAUSE"],
                ["00 06", "", "END"],
                ["00 07", "B", ""],
                ["00 08", "S", "GO_TO_SCRIPT"],
                ["00 09", "", ""],
                ["00 0a", "B", ""],
                ["00 0b", "", ""],
                ["00 0c", "", ""],
                ["00 0d", "", ""],
                ["00 0e", "", ""],
                ["00 0f", "", ""],
                ["00 10", "Bh", ""],
                ["00 11", "Bh", ""],
                ["00 12", "", ""],
                ["00 13", "", ""],
                ["00 14", "", ""],
                ["00 16", "B", ""],
                ["00 17", "Bh", ""],
                ["00 20", "BhBhH", ""],
                ["00 30", "", ""],
                ["00 31", "", ""],
                ["00 32", "", "CONFIRM_SCENARIO_NAME"],
                ["00 33", "Bh", "JUMP_3"],
                ["00 34", "Bh", ""],
                ["00 35", "", ""],
                ["00 36", "B", ""],
                ["00 37", "HiBh", ""],

                ["01 00", "S", "SET_GAME_TITLE"],
                ["01 01", "BS", "CALL_SCRIPT"],
                ["01 02", "Bh", ""],
                ["01 03", "SSS", ""], #ISS
                ["01 04", "BS", ""],
                ["01 05", "BhBh", ""],
                ["01 06", "BhBh", ""],
                ["01 07", "BhBh", ""],
                ["01 08", "BhBhBhBhBhBhBh", ""],
                ["01 09", "SSSB", ""],
                ["01 0a", "BhBh", ""], #BhBhBh #BhBh
                ["01 0b", "BhBhS", ""],
                ["01 0c", "HH", ""],
                ["01 0d", "BHSS", "SET_SCENARIO_NAME"],
                ["01 0e", "HhBhBhBh", ""],
                ["01 0f", "Bh", ""],
                ["01 10", "HhBhBh", ""],
                ["01 11", "Bh", ""],
                ["01 12", "BhBhBhBhBhBhBh", ""],
                ["01 13", "BhBhBhBhBh", ""],
                ["01 14", "Bh", ""],
                ["01 15", "BS", ""],
                ["01 16", "Bh", ""],
                ["01 17", "SS", ""],
                ["01 18", "S", ""],
                ["01 19", "SBh", ""],
                ["01 1a", "H", ""],
                ["01 1b", "Hh", ""],
                ["01 1c", "HhBh", ""],
                ["01 1d", "HhBh", ""],
                ["01 1e", "SS", ""],
                ["01 1f", "SSS", ""],

                ["02 00", "BhS", "SET_BG"],
                ["02 01", "BhBhBh", ""],
                ["02 02", "BhB", ""],
                ["02 03", "BhBhBhBhBh", ""],
                ["02 04", "BhBh", ""],
                ["02 05", "BhBhBh", ""],
                ["02 06", "BhBh", ""],
                ["02 07", "BhBh", ""],
                ["02 08", "BhBhBhBh", "SCREEN_MOTION"],
                ["02 09", "BhBhBhBhBhBh", ""],
                ["02 0a", "BhBhBh", ""],
                ["02 0b", "BhBhBhBh", ""],
                ["02 0c", "BhBhBhBhB", ""],
                ["02 0d", "BhBh", ""],
                ["02 0e", "BhBh", ""],
                ["02 0f", "BhBh", ""],
                ["02 10", "BhBhBh", ""],
                ["02 11", "BhBhBh", ""],
                ["02 12", "BhBhBhBhBhS", "SET_CHOICE_OPTION"],
                ["02 13", "BhBh", ""],
                ["02 14", "BhSBhBhBhB", ""],
                ["02 15", "BhBhBhBh", ""],
                ["02 16", "BhSBhBhBhBh", ""],
                ["02 17", "BhB", ""],

                ["03 00", "BhSBhB", "FADE_SCREEN"],
                ["03 01", "BhBhB", ""],
                ["03 02", "Bh", ""],
                ["03 03", "SB", ""],

                ["04 00", "BhHh", ""],
                ["04 01", "BhB", ""],
                ["04 02", "BhB", ""],
                ["04 03", "BhBh", ""],
                ["04 04", "BhBh", ""],

                ["05 00", "BhS", "MESSAGE"],
                ["05 01", "BhBhBhBhBhBhBhBh", ""],
                ["05 02", "BhBhBhBhBhBhBh", ""],
                ["05 03", "BhBh", ""],
                ["05 04", "BhBh", ""],
                ["05 05", "B", ""],
                ["05 06", "", ""],
                ["05 07", "H", ""],

                ["06 00", "SHh", "SET_BGM"],
                ["06 01", "Bh", ""],
                ["06 02", "S", "PLAY_VIDEO"],
                ["06 03", "", ""],
                ["06 04", "BhS", "PLAY_SE"],
                ["06 05", "BhB", ""],
                ["06 06", "Bh", ""],
                ["06 07", "", ""],
                ["06 08", "Bh", ""],
                ["06 09", "Bh", ""],
                ["06 0a", "S", ""],
                ["06 0b", "HiBh", ""],
                ["06 0c", "BhBhBhBh", ""],
                ["06 0d", "", ""],
                ["06 0e", "BhBh", ""]
            ],
            [ ##mode 1
                ["00 00", "BIBBi", "INIT"],
                ["00 01", "BBiHBiI", "JUMP_1"], #BIBBIBi
                ["00 02", "Bi", "JUMP_2"],
                ["00 03", "Bi", ""],
                ["00 04", "", "RETURN"],
                ["00 05", "BiB", "PAUSE"],
                ["00 06", "", "END"],
                ["00 07", "B", ""],
                ["00 08", "S", "GO_TO_SCRIPT"],
                ["00 09", "", ""],
                ["00 0a", "B", ""],
                ["00 0b", "", ""],
                ["00 0c", "", ""],
                ["00 0d", "", ""],
                ["00 0e", "", ""],
                ["00 0f", "", ""],
                ["00 10", "Bi", ""],
                ["00 11", "Bi", ""],
                ["00 12", "", ""],
                ["00 13", "", ""],
                ["00 14", "", ""],
                ["00 16", "B", ""],
                ["00 17", "Bi", ""],
                ["00 20", "BiBiH", ""],
                ["00 30", "", ""],
                ["00 31", "", ""],
                ["00 32", "", "CONFIRM_SCENARIO_NAME"],
                ["00 33", "Bi", "JUMP_3"],
                ["00 34", "Bi", ""],
                ["00 35", "", ""],
                ["00 36", "B", ""],
                ["00 37", "HiBi", ""],

                ["01 00", "S", "SET_GAME_TITLE"],
                ["01 01", "BS", "CALL_SCRIPT"], #BiS
                ["01 02", "Bi", ""],
                ["01 03", "ISS", ""],
                ["01 04", "BS", ""],
                ["01 05", "BiBi", ""],
                ["01 06", "BiBi", ""],
                ["01 07", "BiBi", ""],
                ["01 08", "BiBiBiBiBiBiBi", ""],
                ["01 09", "SSSB", ""],
                ["01 0a", "BiBi", ""],
                ["01 0b", "BiBiS", ""],
                ["01 0c", "HI", ""],
                ["01 0d", "BiSS", "SET_SCENARIO_NAME"],
                ["01 0e", "HiBiBiBi", ""],
                ["01 0f", "Bi", ""],
                ["01 10", "HiBiBi", ""],
                ["01 11", "Bi", ""],
                ["01 12", "BiBiBiBiBiBiBi", ""],
                ["01 13", "BiBiBiBiBi", ""],
                ["01 14", "Bi", ""],
                ["01 15", "BS", ""],
                ["01 16", "Bi", ""],
                ["01 17", "SS", ""],
                ["01 18", "S", ""],
                ["01 19", "SBi", ""],
                ["01 1a", "H", ""],
                ["01 1b", "Hi", ""],
                ["01 1c", "HiBi", ""],
                ["01 1d", "HiBi", ""],
                ["01 1e", "SS", ""],
                ["01 1f", "SSS", ""],

                ["02 00", "BiS", "SET_BG"],
                ["02 01", "BiBiBi", ""],
                ["02 02", "BiB", ""],
                ["02 03", "BiBiBiBiBi", ""],
                ["02 04", "BiBi", ""],
                ["02 05", "BiBiBi", ""],
                ["02 06", "BiBi", ""],
                ["02 07", "BiBi", ""],
                ["02 08", "BiBiBiBi", ""],
                ["02 09", "BiBiBiBiBiBi", ""],
                ["02 0a", "BiBiBi", ""],
                ["02 0b", "BiBiBiBi", ""],
                ["02 0c", "BiBiBiBiB", ""],
                ["02 0d", "BiBi", ""],
                ["02 0e", "BiBi", ""],
                ["02 0f", "BiBi", ""],
                ["02 10", "BiBiBi", ""],
                ["02 11", "BiBiBi", ""],
                ["02 12", "BiBiBiBiBiS", "SET_CHOICE_OPTION"],
                ["02 13", "BiBi", ""],
                ["02 14", "BiSBiBiBiB", ""],
                ["02 15", "BiBiBiBi", ""],
                ["02 16", "BiSBiBiBiBi", ""],
                ["02 17", "BiB", ""],

                ["03 00", "BiSBiB", "FADE_SCREEN"],
                ["03 01", "BiBiB", ""],
                ["03 02", "Bi", ""],
                ["03 03", "SB", ""],

                ["04 00", "BiHi", ""],
                ["04 01", "BiB", ""],
                ["04 02", "BiB", ""],
                ["04 03", "BiBi", ""],
                ["04 04", "BiBi", ""],

                ["05 00", "BIS", "MESSAGE"],
                ["05 01", "BiBiBiBiBiBiBiBi", ""],
                ["05 02", "BiBiBiBiBiBiBi", ""],
                ["05 03", "BiBi", ""],
                ["05 04", "BiBi", ""],
                ["05 05", "B", ""],
                ["05 06", "", ""],
                ["05 07", "H", ""],

                ["06 00", "SHi", "SET_BGM"],
                ["06 01", "Bi", ""],
                ["06 02", "S", "PLAY_VIDEO"],
                ["06 03", "", ""],
                ["06 04", "BiS", "PLAY_SE"],
                ["06 05", "BiB", ""],
                ["06 06", "Bi", ""],
                ["06 07", "", ""],
                ["06 08", "Bi", ""],
                ["06 09", "Bi", ""],
                ["06 0a", "S", ""],
                ["06 0b", "HiBi", ""],
                ["06 0c", "BiBiBiBi", ""],
                ["06 0d", "", ""],
                ["06 0e", "BiBi", ""],
                ["06 0f", "Bi", ""], #Only latest game?
                ["06 11", "Bi", ""], #Only latest game?
                ["06 13", "BiBi", ""], #Only latest game?
                ["06 14", "BiBiBi", ""], #Only latest game?
                ["06 15", "Bi", ""] #Only latest game?
            ]
        ]

    def __init__(self, mscFile, txtFile, mode, encoding):
        self.__mscFile = mscFile
        self.__txtFile = txtFile
        self.__encoding = encoding
        self.__segments = []
        self.__parametersOne = []
        self.__parametersTwo = []
        self.__pointer = 0
        self.__commands = []
        self.__args = []
        self.__offsets = []
        self.__mode = mode
        #0 - Bullet Butlers, ....
        try:
            extFile = open(self.__mscFile, 'rb')
            self.__file_len = len(extFile.read())
            extFile.close()
        except:
            pass

    def disassemble(self):
        self.__pointer = 0
        self.__segments = []
        self.__parametersOne = []
        self.__parametersTwo = []
        self.__commands = []
        self.__args = []
        self.__offsets = []

        self.__dissHeader()
        self.__dissCommands()
    def just_diss_header(self):
        self.__pointer = 0
        self.__segments = []
        self.__parametersOne = []
        self.__parametersTwo = []
        self.__commands = []
        self.__args = []
        self.__offsets = []

        self.__dissHeader()
    def show_data(self):
        extFile = open(self.__mscFile, 'rb')
        print("- Длина файла:")
        print(len(extFile.read()))
        extFile.close()
        print("- Границы сегментов:")
        print(self.__segments)
        print("- Техсекция один:")
        for i in self.__parametersOne:
            print(i)
        print("- Техсекция два:")
        for i in self.__parametersTwo:
            print(i)
        #print("- Команды с аргументами:")
        #for i in range(len(self.__commands)):
        #    print(self.__commands[i])
        #    print(self.__args)

    def __dissHeader(self):
        extFile = open(self.__mscFile, 'rb')
        assert (extFile.read(2) == b'\x00\x00'), "This is not .msc script!\nСие не скрипт .msc!"
        self.__pointer += 2

        self.__segments.append(struct.unpack('I', extFile.read(4))[0])
        self.__pointer += 4

        sectionStruct = 'II'
        sectionLen = 9
        if (self.__mode == 0):
            sectionStruct = 'HI'
            sectionLen = 7

        for i in range(1, 3, 1):
            self.__segments.append(struct.unpack('I', extFile.read(4))[0])
            self.__pointer += 4
            nay = []
            for j in range(self.__segments[i]//sectionLen):
                assert (extFile.read(1) == b'\x00'), "This can't be possible in true .msc script!\nВ истинном .msc скрипте сие не может быть возможно!"
                #nay.append(list(struct.unpack(sectionStruct, extFile.read(sectionLen-1))))
                nay.append([])
                for z in sectionStruct:
                    if (z.upper() == 'H'):
                        nay[j].append(struct.unpack(z, extFile.read(2))[0])
                    elif (z.upper() == 'I'):
                        nay[j].append(struct.unpack(z, extFile.read(4))[0])
                    else:
                        raise Exception("Unsupported!/Неподдерживаемо!")
                self.__pointer += sectionLen
            if (i == 1):
                self.__parametersOne += nay
            elif (i == 2):
                self.__parametersTwo += nay
        #print(self.__pointer)
        extFile.close()

    def __dissCommands(self):
        out_file = open(self.__txtFile, 'w', encoding=self.__encoding)
        in_file = open(self.__mscFile, 'rb')
        in_file.seek(self.__pointer, 0)
        free_bytes = False
        free_bytes_string = b''
        out_file.write("#VERSION " + str(self.__mode) + "\n")
        out_file.write("#ENCODING " + str(self.__encoding) + "\n")
        while (self.__pointer < self.__file_len):

            for i in self.__parametersOne:
                if ((self.__pointer - self.__segments[0]) == i[1]):
                    out_file.write("#2-" + str(i[0]) + "\n")
            for i in self.__parametersTwo:
                if ((self.__pointer - self.__segments[0]) == i[1]):
                    out_file.write("#3-" + str(i[0]) + "\n")
            for i in self.__offsets:
                if ((self.__pointer - self.__segments[0]) == i[1]):
                    out_file.write("#4-" + str(i[0]) + "\n")

            commandBytes = in_file.read(2)
            self.__pointer += 2
            com_index = -1
            for i in range(len(self.CommandLibrary[self.__mode])):
                if (commandBytes.hex(' ') == self.CommandLibrary[self.__mode][i][0]):
                    com_index = i
            if (com_index == -1):
                if (not (free_bytes)):
                    out_file.write("#0-")
                    free_bytes = True
                if (free_bytes):
                    free_bytes_string += commandBytes
            else:
                if (free_bytes):
                    out_file.write(free_bytes_string.hex(' '))
                    out_file.write('\n')
                    free_bytes = False
                out_file.write("#1-")
                if (self.CommandLibrary[self.__mode][com_index][2] != ''):
                    out_file.write(self.CommandLibrary[self.__mode][com_index][2])
                else:
                    out_file.write(commandBytes.hex(' '))
                #TODO: УБРАТЬ ПОДСКАЗКУ.
                #out_file.write(" " + str(self.__pointer - self.__segments[0] - 2))
                out_file.write('\n')

                args = []
                for i in range(len(self.CommandLibrary[self.__mode][com_index][1])):
                    if (self.CommandLibrary[self.__mode][com_index][1][i].upper() == 'B'):
                        args.append(struct.unpack(self.CommandLibrary[self.__mode][com_index][1][i], in_file.read(1))[0])
                        self.__pointer += 1
                    elif (self.CommandLibrary[self.__mode][com_index][1][i].upper() == 'H'):
                        args.append(struct.unpack(self.CommandLibrary[self.__mode][com_index][1][i], in_file.read(2))[0])
                        self.__pointer += 2
                    elif (self.CommandLibrary[self.__mode][com_index][1][i].upper() == 'I'):
                        args.append(struct.unpack(self.CommandLibrary[self.__mode][com_index][1][i], in_file.read(4))[0])
                        self.__pointer += 4
                    elif (self.CommandLibrary[self.__mode][com_index][1][i].upper() == 'S'):
                        str_struct = 'I'
                        str_struct_len = 4
                        if (self.__mode == 0):
                            str_struct = 'H'
                            str_struct_len = 2
                        str_len = struct.unpack(str_struct, in_file.read(str_struct_len))[0]
                        self.__pointer += str_struct_len
                        string_bytes = in_file.read(str_len)
                        try:
                            args.append(string_bytes.decode(self.__encoding))
                        except:
                            args.append(string_bytes)
                        self.__pointer += str_len
                out_file.write(str(args))
                if (self.__pointer < self.__file_len):
                    out_file.write('\n')
        if (free_bytes):
            out_file.write(free_bytes_string.hex(' '))
            free_bytes = False
        out_file.close()
        in_file.close()

    def assemble(self):
        self.__pointer = 0
        self.__segments = []
        self.__parametersOne = []
        self.__parametersTwo = []
        self.__commands = []
        self.__args = []
        self.__offsets = []

        in_file = open(self.__txtFile, 'r', encoding="shift-jis")
        current_line = in_file.readline()
        mode = int(current_line.split(' ')[1])
        self.__mode = mode
        current_line = in_file.readline()
        encoding = current_line.split(' ')[1][:-1]
        self.__encoding = encoding
        current_line = in_file.readline()

        message_count = 0
        common_section = b''

        while (current_line != ''):
            if (current_line == '\n'):
                current_line = in_file.readline()
                continue
            if (current_line[0] == '$'):
                current_line = in_file.readline()
                continue

            if (current_line[1] == '0'):
                bytez = bytes.fromhex(current_line[3:-1])
                common_section += bytez
                self.__pointer += len(bytez)
            elif (current_line[1] == '1'):
                command_name = current_line[3:-1]
                command_index = -1
                for i in range (len(self.CommandLibrary[self.__mode])):
                    if (command_name == self.CommandLibrary[self.__mode][i][2]):
                        command_index = i
                        command_name = self.CommandLibrary[self.__mode][i][0]
                        break
                    elif (command_name == self.CommandLibrary[self.__mode][i][0]):
                        command_index = i
                        break
                common_section += bytes.fromhex(command_name)
                self.__pointer += 2
                current_line = in_file.readline()
                args = current_line[1:-2].split(', ')
                if (command_name == '05 00'):
                    args[1] = str(message_count)
                    message_count += 1
                for i in range(len(self.CommandLibrary[self.__mode][command_index][1])):
                    if (self.CommandLibrary[self.__mode][command_index][1][i].upper() == 'I'):
                        common_section += struct.pack(self.CommandLibrary[self.__mode][command_index][1][i], int(args[i]))
                        self.__pointer += 4
                    elif (self.CommandLibrary[self.__mode][command_index][1][i].upper() == 'H'):
                        common_section += struct.pack(self.CommandLibrary[self.__mode][command_index][1][i], int(args[i]))
                        self.__pointer += 2
                    elif (self.CommandLibrary[self.__mode][command_index][1][i].upper() == 'B'):
                        common_section += struct.pack(self.CommandLibrary[self.__mode][command_index][1][i], int(args[i]))
                        self.__pointer += 1
                    elif (self.CommandLibrary[self.__mode][command_index][1][i].upper() == 'S'):
                        stringz = args[i][1:-1].replace('\\\\', '\\').encode(self.__encoding)
                        if (self.__mode == 0):
                            common_section += struct.pack('H', len(stringz))
                            self.__pointer += 2
                        elif (self.__mode == 1):
                            common_section += struct.pack('I', len(stringz))
                            self.__pointer += 4
                        common_section += stringz
                        self.__pointer += len(stringz)
            elif (current_line[1] == '2'):
                zlo = []
                label_number = int(current_line[3:-1])
                zlo.append(label_number)
                zlo.append(self.__pointer)
                self.__parametersOne.append(zlo)
            elif (current_line[1] == '3'):
                zlo = []
                label_number = int(current_line[3:-1])
                zlo.append(label_number)
                zlo.append(self.__pointer)
                self.__parametersTwo.append(zlo)
            current_line = in_file.readline()

        sectionStruct = 'II'
        sectionLen = 9
        if (self.__mode == 0):
            sectionStruct = 'HI'
            sectionLen = 7
        out_file = open(self.__mscFile, 'wb')
        out_file.write(b'\x00\x00')
        section_one_len = len(self.__parametersOne)*sectionLen
        section_two_len = len(self.__parametersTwo)*sectionLen
        script_offset = 14 + section_one_len + section_two_len
        out_file.write(struct.pack('I', script_offset))

        out_file.write(struct.pack('I', section_one_len))
        for i in range(len(self.__parametersOne)):
            out_file.write(b'\x00')
            out_file.write(struct.pack(sectionStruct[0], self.__parametersOne[i][0]))
            out_file.write(struct.pack(sectionStruct[1], self.__parametersOne[i][1]))
        out_file.write(struct.pack('I', section_two_len))
        for i in range(len(self.__parametersTwo)):
            out_file.write(b'\x00')
            out_file.write(struct.pack(sectionStruct[0], self.__parametersTwo[i][0]))
            out_file.write(struct.pack(sectionStruct[1], self.__parametersTwo[i][1]))

        out_file.write(common_section)
        out_file.close()
        in_file.close()

    def analyzeScript(self):
        in_file = open(self.__mscFile, 'rb')
        one = in_file.read(1).hex()
        two = in_file.read(1).hex()
        in_file.close()
        if (one != two):
            raise ItsNotMsc("Сие не .msc скрипт!")
        if (one == '00'):
            return 0x00
        else:
            return int(one, 16)
    def cryptScript(self, key):
        in_file = open(self.__mscFile, 'rb')
        out_file = open(self.__mscFile+'.testercrypt333', 'wb')
        reader = in_file.read(1)
        while (reader != b''):
            string_conv = str(hex(int(reader.hex(), 16) ^ 0x88))[2:]
            if (len(string_conv) == 1):
                string_conv = "0" + string_conv
            out_file.write(bytes.fromhex(string_conv))
            reader = in_file.read(1)
        in_file.close()
        out_file.close()

class ItsNotMsc(Exception):
    def __init__(self, text):
        self.txt = text