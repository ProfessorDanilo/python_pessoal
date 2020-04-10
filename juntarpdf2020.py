import os
from PyPDF2 import PdfFileReader, PdfFileMerger


merger = PdfFileMerger()
print("por padrão o nome dos arquivos serão: docxx.pdf em que xx é um número começado por 01.")

n=int(input("Digite o número de arquivos a serem juntados:\n"))



nome=str(input("Digite o nome de saída do arquivo:"))


####criano os nomes dos arquivos a serem lidos
filename=["vazio"]        
for i in range(1,n+1,1):
    filename.append("doc")
    if i<=9:
        filename[i]=filename[i]+"0"
        filename[i]=filename[i]+str(i)
    else:
        filename[i]=filename[i]+str(i)
    filename[i]=filename[i]+".pdf"
print(filename)

#lendo os arquivos
for i in range(1,n+1,1):
    merger.append(PdfFileReader(filename[i],"rb"))




merger.write(os.path.join(nome+".pdf"))
