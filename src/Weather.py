import csv


def met( var ):
    with open('weather.csv', newline="", encoding="ISO-8859-1") as filecsv:
        lettore = csv.reader(filecsv, delimiter=",")

        dati = [(linea[1], linea[2], linea[10]) for linea in lettore if linea[1] == var]

        temp = dati.pop()
        temperature = temp[1]
        rain = temp[2]

        if (rain == 1):
            rain_txt = "it was raining"
        else:
            rain_txt = "it wasn't raining"

        print("\n The temperature recorded on the day", var, "\n was", temperature, "degree and", rain_txt)

        return temperature, rain
