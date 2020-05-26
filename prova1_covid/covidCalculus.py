
import matplotlib.pyplot as plt
import pandas as pd
import requests
import os
from csv import *
import csv

def main():
    print("\n______________________RUNGE KUTTA -PREDIÇÂO DE DADOS COVID-19 NO BRASIL_____________________________")

    print("###########################################################################################")
    print("###########################################################################################")
    print("___________________________________________________________________________________________\n")


#get the archives with update datas from github repository
def getDataArchive(url, r_address = None):
    if r_address == None:
        r_address = 'archives/' + os.path.basename(url.split("?")[0])
    response = requests.get(url, stream = True)
    if response.status_code == requests.codes.OK:
        with open(r_address + os.path.basename(url.split("?")[0]),
            'wb') as new_archive:
            for i in response.iter_content(chunk_size= 256 ):
                new_archive.write(i)
        print("Dowload com dados da Covid-19 finalizado!\n" + "Salvo em: {}". format(r_address))
    else: response.raise_for_status()


#get the Data from Brazil
def openData(path):
    x = []
    with open(path, 'res') as confirmed:
        data_read = csv.DictReader(confirmed, delimiter = ',')
        for c in data_read:
            if c['Country/Region'] == 'Brazil':
                collum = c
    for i in collum.values():
        x.append(i)
    return x

#values of K's
def kOne1(x1, k12):
    return -1 * k12 * x1

def kTwo1(x1, k1, k12):
    return -1 * k12 * (x1 + k1/2)

def kThree1(x1, k2, k12):
    return -1 * k12 * (x1 + k2/2)

def kFour1(x1, k3, k12):
    return -1 * k12 * (x1 + k3)

def kOne2(x1, x2, k12, k23, k24):
    return k12 * x1 - (k23 + k24) * x2

def kTwo2(x1, x2, k1, k12, k23, k24):
    return k12 * (x1 + k1 / 2) - (k23 + k24) * (x2 + k1 / 2)

def kThree2(x1, x2, k2, k12, k23, k24):
    return k12 * (x1 + k2 / 2) - (k23 + k24) * (x2 + k2 / 2)

def kFour2(x1, x2, k3, k12, k23, k24):
    return k12 * (x1 + k3) - (k23 + k24) * (x2 + k3)

def kOne3(x2 , k23):
    return k23 * x2

def kTwo3(x2, k1, k23):
    return k23 * (x2 + k1/2)

def kThree3(x2, k2, k23):
    return k23 * (x2 + k2/2)

def kFour3(x2, k3, k23):
    return k23 * (x2 + k3)

def kOne4(x2, k24):
    return k24 * x2

def kTwo4(x2, k1, k24):
    return k24 * (x2 + k1/2)

def kThree4(x2, k2, k24):
    return k24 * (x2 + k2/2)

def kFour4(x2, k3, k24):
    return k24 * (x2 + k3)


def functionsToCall():
    variationRates(
    brasilDataRecovery(globalCases()),
    brasilDataDeath(globalDeath()),
    brasilDataRecovery(globalRecovery()))

def DeltaX(case):
    return int(case[len(case) - 1]) - int(case[len(case) - 2])

def globalCases():
    g_contamination = "archives/time_series_covid19_confirmed_global.csvtime_series_covid19_confirmed_global.csv"
    return g_contamination

def globalDeath():
    g_deaths= 'archives/time_series_covid19_deaths_global.csvtime_series_covid19_deaths_global.csv'
    return (g_deaths)

def globalRecovery():
    g_recovery = 'archives/time_series_covid19_recovered_global.csvtime_series_covid19_recovered_global.csv'
    return (g_recovery)

def brasilDataCases(c):

    cases = []

    with open(c) as contamination:
        read = csv.DictReader(contamination)
        for l in read:
            if l['Country/Region']  == 'Brazil':
                b_contamination = l
    for n in b_contamination.values():
        cases.append(n)

    for i in range(len(cases) - 1):
        if cases[i] < 0:
            del cases[i]
        else: return cases
    return cases

def brasilDataDeath(d):
    death_cases = []
    with open(d) as death:
        read = csv.DictReader(death)
        for l in read:
            if l['Country/Region']  == 'Brazil':
                b_death = l
    for n in b_death.values():
        death_cases.append(n)
    # b_death = g_deaths['Country/Region']  == 'Brazil'
    # b_recovery = g_recovery['Country/Region']  == 'Brazil'
    return death_cases

def brasilDataRecovery(r):
    recovery_cases = []
    with open(r) as recovery:
        read = csv.DictReader(recovery)
        for l in read:
            if l['Country/Region']  == 'Brazil':
                b_recovery = l
    for n in b_recovery.values():
        recovery_cases.append(n)
    return recovery_cases

def variationRates(cases, death_cases, recovery_cases):
    variaton_rates = []
    delta_cases = DeltaX(cases)
    delta_deaths = DeltaX(death_cases)
    delta_recovery = DeltaX(recovery_cases)
    cases_brasil = 20900000 * 0.7 - int(cases[len(cases) - 1])

    k12 = delta_cases /  cases_brasil
    k23 = delta_deaths / int(cases[len(cases)-2])
    k24 = delta_recovery / int(cases[len(cases)-2])
    variaton_rates.append(round(k12, 8))
    variaton_rates.append(round(k23,8))
    variaton_rates.append(round(k24,8))
    print("Taxa de variação para contágio, morte e recuperação, respectivamente: ")
    print(variaton_rates)
    print("total de casos: ", cases[len(cases) -1])
    print("total de mortes: ", death_cases[len(death_cases) -1])
    print("total de recuperações: ", recovery_cases[len(recovery_cases) -1])
    return rungeKutta(cases_brasil, cases, death_cases, recovery_cases, variaton_rates)

def rungeKutta(cases_brasil, cases, death_cases, recovery_cases, variation_rates):
    h = 1
    t = 0
    k12 = variation_rates[0]
    k23 = variation_rates[1]
    k24 = variation_rates[2]
    rk11 = 0
    rk12 = 0
    rk13 = 0
    rk14 = 0

    rk21 = 0
    rk22 = 0
    rk23 = 0
    rk24 = 0

    rk31 = 0
    rk32 = 0
    rk33 = 0
    rk34 = 0

    rk41 = 0
    rk42 = 0
    rk43 = 0
    rk44 = 0

    x1 = cases_brasil
    x2 = int( cases[len(cases) - 1])
    x3 = int(death_cases[len(death_cases) - 1])
    x4 = int(recovery_cases[len(recovery_cases) -1])

    aux_one = 0
    aux_two = 0
    aux_three = 0
    aux_four = 0
    error = 0

    graphT = []
    graphX1 = []
    graphX2 = []
    graphX3 = []
    graphX4 = []
    df = pd.read_csv("archives/time_series_covid19_confirmed_global.csvtime_series_covid19_confirmed_global.csv")
    count = df.shape[1]
    days = []

    print(days)

    while t < 45:
        aux_one = x1
        aux_two = x2
        aux_three = x3
        aux_four = x4

        rk11 = h*kOne1(x1, k12)
        rk21 = h*kOne2(x1, x2,k12, k23, k24)
        rk31 = h*kOne3(x2, k23)
        rk41 = h*kOne4(x2, k24)

        rk12 = h*kTwo1(x1, rk11, k12)
        rk22 = h*kTwo2(x1, x2, rk21, k12, k23, k24)
        rk32 = h*kTwo3(x2, rk31, k23)
        rk42 = h*kTwo4(x2, rk41, k24)

        rk13 = h*kThree1(x1, rk12, k12)
        rk23 = h*kThree2(x1, x2, rk22, k12, k23, k24)
        rk33 = h*kThree3(x2, rk32, k23)
        rk43 = h*kThree4(x2, rk42, k24)

        rk14 = h*kFour1(x1, rk13, k12)
        rk24 = h*kFour2(x1, x2, rk23, k12, k23, k24)
        rk34 = h*kFour4(x2, rk43, k24)
        rk34 = h*kFour4(x2, rk33, k24)
        graphT.append(t)
        graphX2.append(x2)
        graphX3.append(x3)
        graphX4.append(x4)


        x1 = x1 + (rk11 + 2 * rk12 + 2 * rk13 + rk14)/6
        x2 = x2 + (rk21 + 2 * rk22 + 2 * rk23 + rk24)/6
        x3 = x3 + (rk31 + 2 * rk32 + 2 * rk33 + rk34)/6
        x4 = x4 + (rk41 + 2 * rk42 + 2 * rk43 + rk44)/6

        k12 = (x2 - aux_two) / x1

        k23 = (x3 - aux_three) / aux_two



        erro = (x1 - aux_one) / aux_one + (x2 - aux_two) / aux_two + (x3 - aux_three) / aux_three + (x4 - aux_four) / aux_four
        t = t + h
    return graphic(graphT, graphX2, graphX3, graphX4)

def graphic(time,x2,x3,x4):

    plt.ioff()

    print("\nCriando gráfico...")
    fig = plt.figure(figsize=(14, 12))
    plt.title(' Covid-19 no Brasil - casos, mortes, recuperações')
    plt.legend()
    plt.xlabel('tempo (t) - dias')
    plt.ylabel('valores (c(t), m(t), r(t)')
    plt.grid(True)
    plt.plot(time,x2,label='c(t) - contagio', color = "orange")
    plt.plot(time,x3,label='m(t) - mortes', color = "green")
    plt.plot(time,x4,label='r(t) - recuperados', color = "blue")
    fig.savefig('grafico_covid1.png', format = 'png', legend = plt.legend())
    print("Grafico criado, arquivo: grafico_covid1.png ")
    print("--Finished the program!--")
    plt.show()


if __name__ == "__main__":
    main()

    url = ["https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv","https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv", "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"]
    for i in range(3):
        getDataArchive(url[i])
        i += 1

    functionsToCall()
