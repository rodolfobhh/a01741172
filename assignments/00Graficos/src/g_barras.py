from matplotlib import pyplot as plt

# Ejemplo - Grafico de barras ------------------------------------------------------ 

def grafico_barras():
    print("Grafico de barras")

    movies=["Annie Hall", "Ben Hur", "CasaBlanca", "Gandhi", "West Side Story"]
    num_oscars=[5, 11, 3, 8, 10]

# Coordenadas en el Eje-X para las barras ------------------------------------------

    xs = [i for i,_ in enumerate(movies)]

# Grafico de barras con coordenadas en el Eje-X [xs] y valores [num_oscars] --------
    plt.bar(xs, num_oscars)
    plt.ylabel("# de Academy Awards")
    plt.title("My Favorite Movies")

# Etiquetando el Eje-X con los nombres de las peliculas al centro de las barras -----
    plt.xticks([i for i,_ in enumerate(movies)], movies)

    plt.savefig('grafico_barras.png')
    plt.show()

def main():
    grafico_barras()

if __name__=='__main__':
    main()