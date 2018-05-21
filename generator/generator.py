import os
from generator.generate_qr import GenerateQR
from xlsx.read_xlsx import ReadXLSX


class Generator:
    def __init__(self, file_name):
        self.__output_folder = "/QR Codes/"
        self.__name = "Name"
        info, rows_counter = ReadXLSX(file_name).get_info()
        output_path = os.path.dirname(os.path.abspath(__file__)) + self.__output_folder
        self.__generate(info, rows_counter, output_path)

    def __generate(self, info, rows_counter, output_path):
        for row in range(0, rows_counter):
            path = output_path
            data = ""
            if self.__name in info:
                name = info[self.__name][row]
                data += "[" + name + "]"

            GenerateQR(data, path)
