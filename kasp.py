import os
txt_name = input("Введите полный адрес txt файла: ") 
f = open(txt_name, "r", encoding='utf-8')
a = f.read()
j=0
nam = 1
itogo = ""
for i in a:
    if a[j] == "\n":
        nam = 1
    if nam == 1:
        if a[j] == " ":
            nam = 0
        itogo += (a[j])   
    j +=1
    

a = itogo
j=0
nam = 1
itogo = ""
for i in a:
    if a[j] == "\n":
        nam = 1
    if nam == 1:
        if a[j] == " " or a[j] == "\t":
            nam = 0
        else:
            itogo += (a[j])   
    j +=1
    
print("Успешно выполнено!")

txt_name = txt_name[:-4] + "_исправленная.txt"

my_file = open(txt_name, "a+")
my_file.write(itogo)
my_file.close()
