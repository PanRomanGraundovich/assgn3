# get-user-country function, returns entered country upper-cased
def getCountry():
    inp = input("Select country: ")
    return inp.upper()


# main function
def getInformation(selectedCountry, rankingFileName, capitalsFileName):
    def loadCVSData(rankingFileName):  # TopUni.csv file loader, returns list with the universities
        list = []
        try:
            fileContent = open(rankingFileName, "r", encoding='utf8')   # opening the file, popping not needed data, exception if there is no file
            for line in fileContent:
                uni = line.split(",")
                for i in range(4):
                    uni.pop(4)
                list.append(uni)
            list.pop(0)
            fileContent.close()
            return list
        except FileNotFoundError:
            file = open("output.txt", "w")
            file.write("file not found")
            file.close()

    def loadCVSData2(capitalsFileName):  # capitals.csv file loader, returns list with the universities
        list = []
        try:
            fileContent = open(capitalsFileName, "r", encoding='utf8')  # doing the same things as in the previous function
            for line in fileContent:
                line.strip()
                uni = line.split(",")
                for i in range(3):
                    uni.pop(2)
                list.append(uni)
            list.pop(0)
            fileContent.close()
            return list
        except FileNotFoundError:
            file = open("output.txt", "w")
            file.write("file not found")
            file.close()

    def numberUnis(list):  # counter of the number of the universities in ToUni.csv file
        counter = 0
        for unis in list:
            counter += 1
        return counter

    def checkCountries(list):  # finder of all available countries
        countries = []
        for unis in list:
            if unis[2].replace('\n', '') not in countries:
                countries.append(unis[2].replace('\n', ''))
        return countries

    def checkContinents(list):  # finder of all available continents
        continents = []
        for units in list:
            if units[2].replace('\n', '') not in continents:
                continents.append(units[2].replace('\n', ''))
        return continents

    def bestByCountryInt(list, selectedCountry):  # looking for the best university by country using the international rank
        unisByCountry = []
        compr = numberUnis(list)
        minima = []
        for univ in list:
            if univ[2].upper() == selectedCountry.upper():
                univ[4] = univ[4].replace('\n', '')
                unisByCountry.append(univ)
        for unis in unisByCountry:
            if int(unis[0]) < compr:
                compr = int(unis[0])
                minima = unis
                # print(minima)
        return minima

    def bestByCountryDom(list, selectedCountry):  # looking for the best university by country using the domestic rank
        unisByCountry = []
        compr = numberUnis(list)
        minima = []
        for univ in list:
            if univ[2].upper() == selectedCountry.upper():
                univ[4] = univ[4].replace('\n', '')
                unisByCountry.append(univ)
        for unis in unisByCountry:
            if int(unis[3]) < compr:
                compr = int(unis[3])
                minima = unis
        return minima

    def average(list, selectedCountry):  # finder of the average value of averages of the universities by country
        counter2 = 0
        # print(">avg: country=", selectedCountry)
        # print(" avg: counter init: counter2=", counter2)
        unisByCountry = []
        sumAvers = 0
        for unis in list:
            # unis[2] = unis[2].upper()
            if unis[2].upper() == selectedCountry:
                unis[4] = unis[4].replace('\n', '')
                unisByCountry.append(unis)
                counter2 += 1
        for unis in unisByCountry:
            sumAvers += float(unis[4])
        # print(counter2)
        if counter != 0:
            averageTotal = (float(sumAvers) / float(counter2))
        return averageTotal

    def findContinent(list2, selectedCountry):  # find the county's continent
        for countries in list2:
            if countries[0].upper() == selectedCountry.upper():
                foundContinent = countries[2].replace('\n', '')
                return foundContinent.upper()

    def countriesByContinent(list2, continent):  # finding all the countries by continent
        foundByContinent = []
        for countries in list2:
            countries[2] = countries[2].replace('\n', '')
            if countries[2].upper() == continent:
                foundByContinent.append(countries[0])
        return foundByContinent

    def maxByContinent(list, countriesByContinent):  # looking for the university with the highest average score by continent
        temp = 0
        currentMax = 0
        for uni in list:
            for country in countriesByContinent:
                if country == uni[2]:
                    uni[4] = uni[4].replace('\n', '')
                    if float(uni[4]) > temp:
                        temp = float(uni[4])
                        currentMax = float(uni[4])
        return currentMax

    def findCapital(list2, selectedCountry):  # finding of the country's capital
        for countries in list2:
            if selectedCountry.upper() == countries[0].upper():
                return countries[1].upper()

    def containsCapital(list, selectedCountry, capital):  # looking for the universities whose names contain name of the capital
        withCapital = []
        for uni in list:
            if uni[2].upper() == selectedCountry.upper():
                if capital in uni[1].upper():
                    withCapital.append(uni[1].upper())
        return withCapital
    file1 = loadCVSData(rankingFileName)
    file2 = loadCVSData2(capitalsFileName)
    fileContent = open("output.txt", "w")
    fileContent.write("Total number of universities => {}\n".format(numberUnis(file1)))  # task 1
    fileContent.write("Available countries => ")  # task 2
    i = 0
    for countries in checkCountries(file1):
        if i > 0:
            fileContent.write(", ")
        fileContent.write("{}".format(countries.upper(), end=" "))
        i += 1
    fileContent.write("\nAvailable continents => ")  # task 3
    j = 0
    for continents in checkContinents(file2):
        if j > 0:
            fileContent.write(", ")
        fileContent.write("{}".format(continents.upper(), end=" "))
        j += 1
    continentCurr = findContinent(file2, selectedCountry)
    bestUniByCountryInt = bestByCountryInt(file1, selectedCountry)
    bestUniByCountryDom = bestByCountryDom(file1, selectedCountry)
    averageScore = average(file1, selectedCountry.upper())
    countriesCont = countriesByContinent(file2, continentCurr)
    continentMaxima = maxByContinent(file1, countriesCont)
    fileContent.write("\nAt international rank => {} ".format(bestUniByCountryInt[0]))  # task 4
    fileContent.write("the university name is => {}".format(bestUniByCountryInt[1].upper()))
    fileContent.write("\nAt national rank => {} ".format(bestUniByCountryDom[3]))  # task 5
    fileContent.write("the university name is => {}\n".format(bestUniByCountryDom[1].upper()))
    fileContent.write("The average score => {}%\n".format(averageScore))  # task 6
    fileContent.write("The relative score to the top university in {} is => ({} / {}) x 100% = {:.2f}%\n".format(continentCurr, averageScore, continentMaxima, averageScore / continentMaxima * 100))  # task 7
    fileContent.write("The capital is => {}\n".format(findCapital(file2, selectedCountry)))  # task 8
    counter = 1  # task 9
    fileContent.write("The universities that contain the capital name =>")
    for universities in containsCapital(file1, selectedCountry, findCapital(file2, selectedCountry)):
        fileContent.write("\n\t#{} {}".format(counter, universities, end=""))
        counter += 1
    fileContent.close()


getInformation(getCountry(), "TopUni.csv", "capitals.csv")  # the main function call
