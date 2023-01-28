#minisistema de notas

sistema={
    'nombreDeInstitucion':"Colegio N",                  #tenemos key nombreDeInstitucion
    'cursos':["python","javaScrip","Java","php"],       #la llave cursos contiene una lista de str ["python","javaScrip","Java","php"]
    'profesores':["profesor1","profesor2"],             #lista
    'alumnos':{                                         #dicionario
        "7753":{"nombre" : "juan",                      #creamos diccionario 'alumnos' donde separamos por codigo
                "apellido" : "rodriguez",               #dentro de cada codigo de alumno tenemos un diccionario con datos a llenar
                "cursos" : ["python"],
                "notas" : {}
                },
        "7754":{"nombre" : "juan",
                "apellido" : "rodriguez",
                "cursos" : ["python","java"],
                "notas" : {}
                },
        "7755":{"nombre" : "juan",
                "apellido" : "rodriguez",
                "cursos" : ["python","php"],
                "notas" : {}
                },
    },
    "cursoProfesor":{                                   #cursos a llevar
        "python":[],
        "javaScrip":[],
        "Java":[],
        "php":[],
    }
}

#asignar profesor curso
"""profesoresActuales=sistema['profesores']            #se crea variable profesoresActuales para logica de programacion
profesorPorAsignar=input("que profesor es: ")       #solicitamos entrada por teclado de que profesor es
if profesorPorAsignar in profesoresActuales:        #busca si profesorPorAsignar esta dentro de sistema, responde como booleano
    print("existe el profesor")
    print(sistema["cursos"])                        #imprime lista e cursos de variable sistema
    cursoPorAsignar=input("que curso va asignar a este profesor: ") #solicita entrada por teclado

    if cursoPorAsignar in sistema['cursos']:    #si cursoPorAsignar digitado esta dentro de lista cursos
        cursoTemp=sistema["cursoProfesor"][cursoPorAsignar]
        cursoTemp.append(cursoPorAsignar)
        sistema["cursoProfesor"][cursoPorAsignar]=cursoTemp          
    else:
        print('no existe el curso')
else:
    print("no existe profesor, desea agregarlo?")
    print(profesorPorAsignar,sistema['profesores'])
    profesorTemp=sistema['profesores']
    profesorTemp.append(profesorPorAsignar)
    sistema["profesores"]=profesorTemp

print(sistema) """
#asignar nota alumno
codAlumno=input("ingrese el codigo del alumno: ")
listaAlumnos=list(sistema['alumnos'].keys())   #obtenermos las keys del diccionario
if codAlumno in listaAlumnos:                   #revisa si codigo digitado esta en la lista de diccionario
    print("alumno existe")
    cursosDelAlumno=sistema["alumnos"][codAlumno]["cursos"]     #consultamos con sistema al alumno, empleando codigo de alumno para mostrar los cursos que tiene
    notas=sistema["alumnos"][codAlumno]["notas"]                #
    notaPorIngresar=int(input("ingrese nota por asignar: "))
    sistema["alumnos"][codAlumno]["notas"]={'python':[notaPorIngresar]}     #si la lista no existia tenemos que usar append
    print(sistema)
else:
    print("alumno no existe")



#1:58:00