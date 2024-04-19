from flask import Flask, render_template, request
from funciones import carga_csv, peliculas_mas_recientes, crea_diccionario_años
from funciones import crea_diccionario_peliculas, crea_diccionario_letra
from funciones import crea_diccionario_genero
import os

archivo_cartelera = 'cartelera_2024.csv'
app = Flask(__name__)
cartelera = carga_csv(archivo_cartelera)
diccionario_peliculas=crea_diccionario_peliculas(cartelera)
diccionario_generos = crea_diccionario_genero(cartelera)
diccionario_year = crea_diccionario_años(cartelera)
diccionario_letter = crea_diccionario_letra(cartelera)

@app.route("/")
def index():
    global cartelera
    lista_peliculas = peliculas_mas_recientes(cartelera)
    return render_template("index.html",lista=lista_peliculas)

@app.route("/generos")
def generos():
    return render_template("generos.html",dicc_generos=diccionario_generos)

@app.route("/genero/<genero>")
def genero_page(genero:str):
    if genero in diccionario_generos:
        peliculas = diccionario_generos[genero]
        return render_template("pagina_genero.html", peliculas_genero = peliculas, genero_pelicula = genero)
    else:
        return render_template("no_existe.html")

@app.route("/anios")
def anio():
    return render_template("anios.html", dicc_anios = diccionario_year)

@app.route("/anio/<anio>")
def anio_page(anio:str):
    if anio in diccionario_year:
        lista_peliculas = diccionario_year[anio]
        return render_template("pagina_año.html", lista = lista_peliculas, año = anio)
    else:
        return render_template("no_existe.html")

@app.route("/alfabetico")
def alfabetico():
    return render_template("alfabetico.html", dicc_letter = diccionario_letter )

@app.route("/letra/<letter>")
def letra(letter:str):
    if letter in diccionario_letter:
        lista_peliculas = diccionario_letter[letter]
        return render_template("pagina_letra.html", lista_letras =lista_peliculas, letra = letter)
    return render_template("no_existe.html")

@app.route("/pelicula/<id>")
def pelicula(id:str):
    if id in diccionario_peliculas:
        pelicula = diccionario_peliculas[id]
        print(f"movie={pelicula['titulo']}")
        return render_template("movie.html",movie=pelicula)
    else:
        return render_template("no_existe.html")
    
if __name__ == "__main__":
    app.run(debug=True)