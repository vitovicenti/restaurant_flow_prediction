import engine
from Regressor import best_regressor, regressor_predict


def p_T( temp ):
    if temp == 1:
        print(" The temperature is very low")

    elif temp == 2:
        print(" The temperature is low")

    elif temp == 3:
        print(" The temperature is good")

    elif temp == 4:
        print(" The temperature is high")

    elif temp == 5:
        print(" The temperature is very high")


def p_Rain(rain):
    if rain == 0:
        print(" It's raining")
    else:
        print(" There is no rain")


def p_Holiday( holiday ):
    if holiday == 0:
        print(" The day is a holiday")
    else:
        print(" The day is working")


def p_Event( event ):
    if event == 0:
        print(" There is no event")

    elif event == 1:
        print(" There is a little event")

    elif event == 2:
        print(" There is a important event")

    elif event == 3:
        print(" There is a great event")




if __name__ == '__main__':

    engine.intro()

    request = engine.create_request()

    bm, bma = best_regressor()

    p_T(request.__getitem__(0)[0])
    p_Rain(request.__getitem__(0)[1])
    p_Holiday(request.__getitem__(0)[2])
    p_Event(request.__getitem__(0)[3])
    print(" The occupancy rate of the hotels is ",request.__getitem__(0)[3]);

    print("\n The best model for this problem is -> ", bm, " with RMSE (0-100 values) -> ", bma)

    # Predizione dell'occupazione risorante
    try:
        prediction = regressor_predict(request, bm)


    except FileNotFoundError:
        prediction = regressor_predict(request, "dataset.csv")

    print("\n The restaurant flow prediction is -> ", int(prediction))
