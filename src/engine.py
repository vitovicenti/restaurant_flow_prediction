import random

# stampa introduzione
import pyswip

import Weather
import cityMap
import searcher


def intro():
    print(" ---------------------- ICON -----------------------")
    print(" ----------------- Restaurant Flow -----------------")
    print(" This system predicts a restaurant's occupancy rate \n based on various factors, such as:")
    print("  -Weather \n  -Holiday and events \n  -Occupancy of neighboring hotels (ONH parameter) \n")
    print(" Focus: ")
    print(" ONH calculates the score related to the occupancy\n of the hotels closest to the restaurant then it ")
    print(" calculates the minimum path that customers have to\n travel, creating a list of the closest ones")
    print(" with which a score from 1 to 100 is achieved")


# Generazione mappa della città
def calculate_PA( holiday, event ):
    print("\n Calculating ONH parameter ...")
    print("\n City map generation ... \n")
    print(" Calculation of minimum routes \n from hotels to restaurants ... \n")

    # generazione del cityMap e ricerca del percorso minimo
    p1, d1 = searcher.test(searcher.AStarSearcher, cityMap.Path.P1)
    p2, d2 = searcher.test(searcher.AStarSearcher, cityMap.Path.P2)
    p3, d3 = searcher.test(searcher.AStarSearcher, cityMap.Path.P3)
    p4, d4 = searcher.test(searcher.AStarSearcher, cityMap.Path.P4)
    p5, d5 = searcher.test(searcher.AStarSearcher, cityMap.Path.P5)


    kb = pyswip.Prolog()

    kb.assertz("albergo(albergo_1)")
    kb.assertz("albergo(albergo_2)")
    kb.assertz("albergo(albergo_3)")
    kb.assertz("albergo(albergo_4)")
    kb.assertz("albergo(albergo_5)")

    kb.assertz("capienza(albergo_1, 70)")
    kb.assertz("capienza(albergo_2, 90)")
    kb.assertz("capienza(albergo_3, 120)")
    kb.assertz("capienza(albergo_4, 80)")
    kb.assertz("capienza(albergo_5, 150)")

    kb.assertz("distanza(albergo_1, " + str(d1) + ")")
    kb.assertz("distanza(albergo_2, " + str(d2) + ")")
    kb.assertz("distanza(albergo_3, " + str(d3) + ")")
    kb.assertz("distanza(albergo_4, " + str(d4) + ")")
    kb.assertz("distanza(albergo_5, " + str(d5) + ")")

    kb.assertz("rist(albergo_1, 0)")
    kb.assertz("rist(albergo_2, 1)")
    kb.assertz("rist(albergo_3, 0)")
    kb.assertz("rist(albergo_4, 0)")
    kb.assertz("rist(albergo_5, 1)")

    query1 = "albergo(X), distanza(X,D), capienza(X,C), rist(X, R), D<500, R=1"
    r1 = list(kb.query(query1))

    query2 = "albergo(X), distanza(X,D), capienza(X,C), rist(X, R), D<500, R=0"
    r2 = list(kb.query(query2))

    query3 = "albergo(X), distanza(X,D), capienza(X,C), rist(X, R), D>=500, D<1000, R=1"
    r3 = list(kb.query(query3))

    query6 = "albergo(X), distanza(X,D), capienza(X,C), rist(X, R), D>=500, D<1000, R=0"
    r6 = list(kb.query(query6))

    query4 = "albergo(X), distanza(X,D), capienza(X,C), rist(X, R), D>=1000, R=1"
    r4 = list(kb.query(query4))

    query5 = "albergo(X), distanza(X,D), capienza(X,C), rist(X, R), D>=1000, R=0"
    r5 = list(kb.query(query5))

#
    from logic.TopDown_prove import g
    occ_perc = int(g())

    t1 = 0
    t2 = 0
    t3 = 0
    t4 = 0
    t5 = 0
    t6 = 0

    r1_score = 0.7

    for r1_index in r1:
        t1 = t1 + r1_index["C"]
        print("r1 c ", r1_index["C"])

    r1_max = t1 * r1_score

    r1_corr = (random.randint(int(occ_perc - 10), int(occ_perc)) * r1_max) / 100

    r2_score = 1

    for r2_index in r2:
        t2 = t2 + r2_index["C"]

    r2_max = t2 * r2_score
    r2_corr = (random.randint(int(occ_perc - 10), int(occ_perc)) * r2_max) / 100

    r3_score = 0.5

    for r3_index in r3:
        t3 = t3 + r3_index["C"]

    r3_max = t3 * r3_score
    r3_corr = (random.randint(int(occ_perc - 10), int(occ_perc)) * r3_max) / 100

    r4_score = 0.2

    for r4_index in r4:
        t4 = t4 + r4_index["C"]

    r4_max = t4 * r4_score
    r4_corr = (random.randint(int(occ_perc - 10), int(occ_perc)) * r4_max) / 100

    r5_score = 0.4

    for r5_index in r5:
        t5 = t5 + r5_index["C"]

    r5_max = t5 * r5_score
    r5_corr = (random.randint(int(occ_perc - 10), int(occ_perc)) * r5_max) / 100

    r6_score = 0.6

    for r6_index in r6:
        t6 = t6 + r6_index["C"]

    r6_max = t6 * r6_score
    r6_corr = (random.randint(int(occ_perc - 10), int(occ_perc)) * r6_max) / 100

    r_max = r1_max + r2_max + r3_max + r4_max + r5_max + r6_max
    r_corr = r1_corr + r2_corr + r3_corr + r4_corr + r5_corr + r6_corr

    pa = (r_corr * 100) / r_max

    return pa


# Creazione richiesta
def create_request():
    X_Input = [[]]
    list = []

    # richiesta informazioni meteo

    print("\n -------------- Information gathering --------------\n")

    print(" Weather condition ...")

    chose1 = int(input(" Enter: 1 to specify temperature and rain\n \t\t0 if would select a day \n Value entered: "))
    while (chose1 != 0 and chose1 != 1):
        print(" \n !! Input error !!")
        chose1 = int(
            input(" Enter: 1 to specify temperature and rain\n \t\t0 if would select a day \n Value entered: "))

    if chose1 == 1:

        # teperatura
        temperature = int(input("\n Enter the temperature in from 1 to 5 \n Value entered: "))
        while 1 > temperature or temperature > 5:
            print("\n !! Input error !!")
            temperature = int(input(" Enter the temperature in from 1 to 5 \n Value entered: "))

        list.append(temperature)

        # pioggia
        rain = int(input("\n Enter: 0 if no rain \n\t\t1 if rain \n Value entered: "))
        while (rain != 0 and rain != 1):
            print("\n !! Input error !!")
            rain = int(input(" Enter: 0 if no rain \n\t\t1 if rain \n Value entered: "))

        list.append(rain)

    else:

        day = input("\n Enter the day: ")
        month = input(" Enter the month: ")

        date = month + "/" + day + "/" + "2020"

        temperature, rain = Weather.met(date)

        temp = int(temperature)
        if temp < 7:
            temperature_range = 1
        elif temp >= 7 and temp < 17:
            temperature_range = 2
        elif temp >= 17 and temp < 27:
            temperature_range = 3
        elif temp >= 27 and temp < 37:
            temperature_range = 4
        elif temp >= 37:
            temperature_range = 5

        list.append(temperature_range)
        list.append(rain)

    # giorno festivo
    print("\n Holiday ...")
    holiday = int(input(" Enter: 0 if no holiday \n\t\t1 if holiday \n Value entered: "))
    while (holiday != 0 and holiday != 1):
        print("\n !! Input error !!")
        holiday = int(input(" Enter: 0 if no holiday \n\t\t1 if holiday \n Value entered: "))

    list.append(holiday)

    # evento
    print("\n Events ...")
    event = int(input(" Enter a value from 0 to 3 for event \n Value entered: "))
    while event < 0 or event > 3:
        print(" !! Input error !!")
        event = int(input(" Enter a value from 0 to 3 for event \n Value entered: "))

    list.append(event)

    # Score prenotazione alberghi
    # calcolo PA

    pa = calculate_PA(int(holiday), int(event))
    list.append(int(pa))
    X_Input = [list]

    print("\n Parameter for regression: ", X_Input)

    return X_Input
