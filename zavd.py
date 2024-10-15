def openFile(file_name, mode):
    try:
        file = open(file_name, mode)
    except IOError:
        print("Файл", file_name, "не відкрився!")
        return None
    else:
        print("Файл", file_name, "відкрився")
        return file

file1_name = "TF13_1.txt"
file2_name = "TF13_2.txt"

file_1_w = openFile(file1_name, "w")
if file_1_w is not None:
    file_1_w.write(
        "створює текстовий файл TF13_1 із символьних рядків різної довжини, слова в яких розділені пробілами і розділовими знаками; ")
    file_1_w.write(
        "читає вміст файла TF13_1, знаходить слова, які розпочинаються голосною літерою і записує кожне в окремий рядок файла TF13_2; ")
    file_1_w.write("читає вміст файла TF13_2 і друкує його по рядках.\n")
    file_1_w.close()
    print("File TF13_1.txt закрито.")

file_2_r = openFile(file1_name, "r")
file_2_w = openFile(file2_name, "w")

if file_2_r is not None and file_2_w is not None:
    vowels = 'аеєиіїоуюяАЕЄИІЇОУЮЯ'
    content = file_2_r.read()
    for word in content.split():
        if word[0] in vowels:
            file_2_w.write(word + '\n')

    file_2_r.close()
    file_2_w.close()
    print(f"Файл {file2_name} закрито.")

file_3_r = openFile(file2_name, "r")

if file_3_r is not None:
    print(f"Вміст файлу {file2_name}:")
    for line in file_3_r:
        print(line.strip())

    file_3_r.close()
    print("File TF13_2.txt закрито!")

