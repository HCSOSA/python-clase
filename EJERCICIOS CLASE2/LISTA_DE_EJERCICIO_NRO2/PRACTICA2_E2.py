""" 
-Obtener la lista de categorías de libros.
-Obtener nombres de los libros y autores.
-poder cambiar el estado de un libro a prestado
-Lista de usuarios de la biblioteca.
 """



Biblioteca={
    'UsuariosRegistados': ['usuario1','usuario2','usuario3'],
    'CategoriaLibros': ['Terror','CienciaFiccion','Comedia'],
    'Libros': ['Libro1','Libro2','Libro3','Libro4'],

    'Libro1':{
        'Categoria':'CategoriaLibros[0]',
        'Nombre':'LagunaNegra',
        'Autor':'Nicols',
        'Estado':[],
    },
    'Libro2':{
        'Categoria':'CienciaFiccion',
        'Nombre':'MarteLejano',
        'Autor':'Ivan',
        'Estado':[],
    },
    'Libro3':{
        'Categoria':'Comedia',
        'Nombre':'TresChiflados',
        'Autor':'Juan',
        'Estado':[],
    },
    'Libro4':{
        'Categoria':'Adolescente',
        'Nombre':'DiarioMath',
        'Autor':'Ana',
        'Estado':[],
    }
 }

usuario=input('Que usuario es: ')

if usuario in Biblioteca['UsuariosRegistados']:
    print('Existe usuario')
    #print(Biblioteca['UsuariosRegistados'][2])
    msg="""Que desea realizar:
    a)Obtener lista de categoria de libros
    b)Obtener nombres de los libros y autores
    c)Solicitar libro """
    print(msg)

    OpcionMenu=input("ingrese la opcion de menu: ")
    if(OpcionMenu!='a' or OpcionMenu!='b' or OpcionMenu!='c'):
        if OpcionMenu=='a':
            print('Lista de categoria',Biblioteca['CategoriaLibros'])
        
        elif OpcionMenu=='b':
            print('Nombre libro1: ',Biblioteca['Libro1']['Nombre'],' - Nombre Autor: ',Biblioteca['Libro1']['Autor'])
            print('Nombre libro2: ',Biblioteca['Libro2']['Nombre'],' - Nombre Autor: ',Biblioteca['Libro2']['Autor'])
            print('Nombre libro3: ',Biblioteca['Libro3']['Nombre'],' - Nombre Autor: ',Biblioteca['Libro3']['Autor'])
            print('Nombre libro4: ',Biblioteca['Libro4']['Nombre'],' - Nombre Autor: ',Biblioteca['Libro4']['Autor'])
        
        elif OpcionMenu=='c':
            EstadoLibros=['En biblioteca','Prestado']
            LibroPrestar=input('Escriba libro a solicitar: ')
            
            if LibroPrestar == 'Libro1':  #Escribir libro a solicitar
                Temp=Biblioteca['Libro1']['Estado']
                Temp.append(EstadoLibros[1])
                print('Nuevo Estado libro1',Biblioteca['Libro1']['Estado'])

            elif LibroPrestar == 'Libro2':
                Temp=Biblioteca['Libro2']['Estado']
                Temp.append(EstadoLibros[1])
                print('Nuevo Estado Libro2',Biblioteca['Libro2']['Estado'])

            elif LibroPrestar == 'Libro3':
                Temp=Biblioteca['Libro3']['Estado']
                Temp.append(EstadoLibros[1])
                print('Nuevo Estado Libro3',Biblioteca['Libro3']['Estado'])
                
            elif LibroPrestar == 'Libro3':
                Temp=Biblioteca['Libro3']['Estado']
                Temp.append(EstadoLibros[1])
                print('Nuevo Estado Libro3',Biblioteca['Libro3']['Estado'])

            else:
                print("Libro no existe")
    else:
        print("Digite caracter correcto")

else:
    nuevoUsuario=input('No existe usuario, Registre nuevo usuario: ')
    usuarioTemp=Biblioteca['UsuariosRegistados']
    usuarioTemp.append(nuevoUsuario)
    print(Biblioteca['UsuariosRegistados'])

#print(Biblioteca)