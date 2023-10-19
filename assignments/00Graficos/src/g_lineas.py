from matplotlib import pyplot as plt

def grafico_lineas():
    print("Grafico de líneas")
    years=[1950, 1960, 1970, 1980, 1990, 2000, 2010]
    gdp=[300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# Crea un grafico de lineas, años en el eje-X, valores en el eje-Y------------------
    plt.plot(years, gdp, color="green", marker="o", linestyle="solid")

    plt.title("Nominal GDP")
    plt.ylabel("Billions of $")
    plt.savefig('grafico_lineas.png')

def main():
    grafico_lineas()

if __name__=='__main__':
    main()