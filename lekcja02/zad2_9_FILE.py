from shutil import copyfile
import os
dir_path = os.path.dirname(__file__)
filename = 'zad2_9_plik.txt'
filepath = os.path.join(dir_path, filename)
# with open('file2.txt', 'wb+') as output, open('file.txt', 'rb') as input:
#     while True:
#         data = input.read(100000)
#         if data == '':  # end of file reached
#             break
#         output.write(data)