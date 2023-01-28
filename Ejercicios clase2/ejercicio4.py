vLista=[10,23,45,'hello']
vLista.append(2)            #agregamos el valor de 2 al final de la lista,array
a=type(vLista[-1])

if a==str:
    print("el utlimo valor es str")
else:
    print("el elemnto no es str")


print(list(vLista))      #imprimimos vLista como tipo lista[]










""" #mini sistema de notas

sistema={
    'nombreDeInstitucion':"Colegio N",
    'cursos':["python","javascrip","java","php"],
    'profesores':["profesor1","profesor2"],
    'alumnos':{
        "7753":{"nombre":"juan",
                "apellido":"rodriguez",
                "cursos":["python"],
                "notas":{}
                },
        "7754":{"nombre":"juan",
                "apellido":"rodriguez",
                "cursos":["python","java"],
                "notas":{}
                },
        "7755":{"nombre":"juan",
                "apellido":"rodriguez",
                "cursos":["php"],
                "notas":{}
                },
    },
    "cursoProfesor":{}
}

#asignar profesor curso
profesoresActuales=sistema['profesores'] 
profesorPorAsignar=input("que profesor es")
if profesorPorAsignar in profesoresActuales:
    print("existe el profesor")
    print(sistema["cursos"])
    cursoPorAsignar=input("que cursos va a asginar a este   profesor")
else:
    print("no existe profesor,desea agregarlo")
    sistema['profesores']=sistema['profesores'].append(profesorPorAsignar)
    profesoresActuales=sistema['profesores']

#asignar nota alumno """