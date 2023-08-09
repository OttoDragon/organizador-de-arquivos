import os
import shutil

from_dir = "C:/Users/tvgge/Downloads"
to_dir = "C:/Users/tvgge/OneDrive/Imagens"
list_of_files = os.listdir(from_dir)

#print(list_of_files)
for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)
    if extension == "":
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Arquivos_Imagem"
        path3 = to_dir + '/' + "Arquivos_Imagem" + '/' + file_name
        print("Path1 ", path1)
        #print("Path2 ", path2)
        print("Path3 ", path3)

        if os.path.exists(path2):
            print("Movendo "+ file_name + "......")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Movendo "+ file_name + ".....")
            shutil.move(path1, path3)



