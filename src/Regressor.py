# IMPORTIAMO LE LIBRERIE

import numpy as np
import pandas as pd
from sklearn import ensemble
from sklearn.ensemble import BaggingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score


# carico il dataset con path passato come stringa
# genero il train set dal dataset importato


def best_regressor():
    rmse_list = list()

    train_data = pd.read_csv('dataset.csv')

    X = train_data.values[:, 0:5]
    Y = train_data.values[:, 5]

    gbr = ensemble.GradientBoostingRegressor(n_estimators=400, max_depth=5, min_samples_split=2,
                                             learning_rate=0.1, loss='squared_error')

    score_gbr = cross_val_score(gbr, X, Y, cv=5, scoring='neg_root_mean_squared_error')
    a_gbr = np.mean(score_gbr)
    std_gbr = np.std(score_gbr)
    rmse_list.append(a_gbr)

    lm = LinearRegression()

    score_lm = cross_val_score(lm, X, Y, cv=5, scoring='neg_root_mean_squared_error')
    a_lm = np.mean(score_lm)
    std_lm = np.std(score_lm)
    rmse_list.append(a_lm)

    BR = BaggingRegressor(n_estimators=100, max_samples=1.0)

    score_BR = cross_val_score(BR, X, Y, cv=5, scoring='neg_root_mean_squared_error')
    a_BR = np.mean(score_BR)
    std_BR = np.std(score_BR)
    rmse_list.append(a_BR)

    if a_gbr == max(rmse_list):
        bm = gbr
        bm_acc = a_gbr

    elif a_lm == max(rmse_list):
        bm = lm
        bm_acc = a_lm

    elif a_BR == max(rmse_list):
        bm = BR
        bm_acc = a_BR

    print("nrmse -> " , a_gbr, " + ", a_BR, " + ", a_lm)
    print("std -> ", std_gbr, " + ", std_BR, " + ", std_lm)

    return bm, bm_acc


# funzione che crea il modello, lo addestra ed effettua la previsione
def regressor_predict( test, model ):
    train_data = pd.read_csv('dataset.csv')

    X = train_data.values[:, 0:5]
    Y = train_data.values[:, 5]

    model.fit(X, Y)

    pred = model.predict(test)

    return pred
