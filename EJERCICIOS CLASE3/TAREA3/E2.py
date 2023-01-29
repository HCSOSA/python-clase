texto="""Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto.
Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un
impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos
y los mezcló de tal manera que logró hacer un libro de textos especimen."""
#split
a=print("split: ",texto.split(sep=" "))
#join
b=print("join: "," ".join(texto))
#count
c=print("count: ",texto.count("texto"))
#find
d=print("find: ",texto.find("texto"))
#uppercase
e=print("uppercase: ",texto.upper())
#lowercase
f=print("lowercase: ",texto.lower())