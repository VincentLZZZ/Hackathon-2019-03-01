# import pandas as pd


def calc_emission_driver(mdf, division, carline, g_to_m, d):
    return mdf[division][carline][g_to_m] / d * 9.072 / 1000


def calc_emission(persona):
    if persona == "driver":
        return 120
    if persona == "Farmer/Producer":
        return 80
    if persona == "Storage companies":
        return 50
    if persona == "Food processor":
        return 50
    if persona == "Trader/Distributor":
        return 60






