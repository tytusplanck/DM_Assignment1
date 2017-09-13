# Assignment 1 - Data Mining
# Tytus Planck and Kyle Rossman
import csv
import math


# Function Definition
def defineK():
    # Asks User to define a value for K and then saves it.
    x = 5
    return x


# Function Definition
def getCSVData():
    data = []
    with open('income_tr.csv', 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in csvreader:
            dataRow = []
            for item in row:
                dataRow.append(item)
            data.append(dataRow)
    return data


# Function Definition
def generateApproximationMatrix(k, data):
    # This will call the function that will find all approximations for one instance. It will loop this so it can have an array of approximations for all instances.
    index = 1
    approximationMatrix = []
    resultsMatrix = []
    while index < len(data):
        approximationMatrix.append(approximateOneInstance(data, index))
        index = index + 1
    resultsMatrix = getFormattedResults(approximationMatrix, k)
    printResults(resultsMatrix)
    return approximationMatrix  # returns array of approximations for each

# Will Take one instance and find all of the approximations to the other instances
def approximateOneInstance(data, index):
    instanceIndex = 1
    # Array of 520 floats containing the approximation to current instance for each object.
    approximationArray = []
    while instanceIndex < len(data):
        approximationArray.append(findRowApproximation(
            data[instanceIndex], data[index]))
        instanceIndex = instanceIndex + 1
    # Will return an array of the approximation of each instance to the current one
    return approximationArray

# Takes one row of the table and finds it's approximation to the other.


# Function Definition
def findRowApproximation(row1, row2):
    smc = getSMCProximity(row1, row2)
    smc = 0
    euc = getEuclidianProximation(row1, row2)
    jac = getJaccardProximation(row1, row2)
    jac = 0
    totalApproximation = ((8 * smc) + (4 * euc) + (2 * jac)) / 4.0
    return totalApproximation

def getSMCProximity(row1, row2):
    # Need to determine you can compare strings in python this way
    match = 0.0
    total = 0.0
    # Finds match and total values for SMC algorithm
    if (row1[2] == row2[2]):
        match = match + 1
        total = total + 1
    else:
        total = total + 1
    if (row1[4] == row2[4]):
        match = match + 1
        total = total + 1
    else:
        total = total + 1
    if (row1[6] == row2[6]):
        match = match + 1
        total = total + 1
    else:
        total = total + 1
    if (row1[7] == row2[7]):
        match = match + 1
        total = total + 1
    else:
        total = total + 1
    if (row1[8] == row2[8]):
        match = match + 1
        total = total + 1
    else:
        total = total + 1
    if (row1[9] == row2[9]):
        match = match + 1
        total = total + 1
    else:
        total = total + 1
    if (row1[10] == row2[10]):
        match = match + 1
        total = total + 1
    else:
        total = total + 1
    if (row1[14] == row2[14]):
        match = match + 1
        total = total + 1
    else:
        total = total + 1
    if (row1[15] == row2[15]):
        match = match + 1
        total = total + 1
    else:
        total = total + 1

    return 1 - (match / total)  # Calculates the SMC Proximation

# Function Definition


def getEuclidianProximation(row1, row2):
    fnlwgt95 = 378460.0 #This is the 95th percentile value for the fnlwgt attribute
    weeklyHours95 = 60.0 #This is the 95th percentile value for the hours per week attribute
    #These two attributes have outliers, so dividing the data set by the maximum can make things appear closer in proximity then they actually are if we sue an outlier.

    euc = ((float(row1[1]) / 82.0) - (float(row2[1]) / 82.0))**2 + ((float(row1[3]) / fnlwgt95) - (float(row2[3]) / fnlwgt95))**2 + ((float(row1[5]) / 16.0) - (float(row2[5]) / 16.0))**2 + ((float(row1[13]) / weeklyHours95) - (float(row2[13]) / weeklyHours95))**2 
    return math.sqrt(euc)

def getJaccardProximation(row1, row2):
    M01 = 0
    M10 = 0
    M11 = 0
    if(int(row1[11]) >= 1 and int(row2[11]) == 0):
        M10 += 1
    if(int(row1[12]) >= 1 and int(row2[12]) == 0):
        M10 += 1
    if(int(row1[11]) == 0 and int(row2[11]) >= 1):
        M01 += 1
    if(int(row1[12]) == 0 and int(row2[12]) >= 1):
        M01 += 1
    if(int(row1[11]) == int(row2[11]) and int(row1[11]) >= 1):
        M11 += 1
    if(int(row1[12]) == int(row2[12]) and int(row1[12]) >= 1):
        M11 += 1

    jaccard = 0
    if (M01 + M10 + M11) != 0:
        jaccard = M11 / (M01 + M10 + M11)

    return jaccard

# Function Definition

def getFormattedResults(approximationMatrix, k):
    results = []
    header = ["Transaction ID"]
    count = 1
    while count <= k:
        header.append(count)
        header.append("prox")
        count = count + 1
    results.append(header)
    outerCounter = 0
    while outerCounter < len(approximationMatrix):

        sortedRow = approximationMatrix[outerCounter][:]
        sortedRow.sort()
        sizeKRow = []
        IDList = []
        kIndex = 0
        while kIndex < k:
            sizeKRow.append(sortedRow[kIndex + 1]) #doing plus one will exclude the proximation to itself
            kIndex = kIndex + 1
        counter = 0
        while counter < len(sizeKRow):
            x = 0
            while x < len(sortedRow):
                if sizeKRow[counter] == approximationMatrix[outerCounter][x]:
                    IDList.append(x)
                x = x + 1
            counter = counter + 1
        y = 0
        singleResultsRow = [outerCounter]
        while y < len(IDList):
            singleResultsRow.append(IDList[y])
            singleResultsRow.append(sizeKRow[y])
            y = y + 1
        results.append(singleResultsRow)
        outerCounter = outerCounter + 1
    return results

def printResults(results):
    with open("output.csv", "wb") as f:
        writer = csv.writer(f)
        writer.writerows(results)

# Function Definition


def main():
    k = defineK()
    data = getCSVData()
    generateApproximationMatrix(k, data)

if __name__ == "__main__":
    main()
