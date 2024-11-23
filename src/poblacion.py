from collections import namedtuple
import csv

RegistroPoblacion = namedtuple('RegistroPoblacion',
                                'pais, codigo, año, censo')

def lee_poblaciones(ruta_fichero):

    with open('poblacion.csv', encoding='utf-8') as f:
        lector=csv.reader(f)
        next(lector)
        poblaciones= []
        for pais, codigo, año, censo in lector:
            pais=str(pais)
            codigo=str(codigo)
            año=int(año)
            censo=int(censo)
            registro = RegistroPoblacion(pais, codigo, año, censo)
            poblaciones.append(registro)
        return poblaciones

def calcula_paises(poblaciones):
    paises = set()
    for registro in poblaciones:
        paises.add(registro.pais)
    return sorted(paises)


def filtra_por_pais(poblaciones, nombre_o_codigo):
    datos_pais = []
    for registro in poblaciones:
        if registro.pais == nombre_o_codigo or registro.codigo == nombre_o_codigo:
            datos_pais.append(registro)
    return datos_pais

def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    datos_filtrados = []
    for registro in poblaciones:
        if registro.año == anyo and registro.pais in paises:
            datos_filtrados.append((registro.pais, registro.censo))
    return datos_filtrados

import matplotlib.pyplot as plt

def muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):
    datos = filtra_por_pais(poblaciones, nombre_o_codigo)
    lista_años = [año for año, _ in datos]
    lista_habitantes = [censo for _, censo in datos]

    titulo = f"Evolución de la población en {nombre_o_codigo}"
    plt.title(titulo)
    plt.plot(lista_años, lista_habitantes)
    plt.show()
