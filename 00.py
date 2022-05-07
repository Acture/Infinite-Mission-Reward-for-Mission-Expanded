import os
import re


path = os.getcwd()

files = os.listdir(path)

for file in files:

    filepath = os.path.join(path, file)
    if '.txt' not in filepath:
        continue
    #print(filepath)
    
    encodings = ['utf-8','windows-1250','windows-1251','windows-1252','iso 8859']

    for encoding in encodings:
        try:
            with open(filepath, "r", encoding=encoding) as f:
                filedata = f.read()
                target = re.sub(r'duration = .*', "duration = -1" , filedata)
                f.close()

            with open(filepath, "r", encoding=encoding) as f:
                f = open(filepath, "w", encoding=encoding)
                f.write(target)
                f.close()
        except UnicodeDecodeError:
            print('{file} unicode error with {e} , trying different encoding'.format(file=filepath, e=encoding))
        else:
            print('opening the {file} with encoding:  {e} '.format(file=filepath, e=encoding))
            break




print("Success")
os.system('pause')
