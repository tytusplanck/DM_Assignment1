# Assignment 1 - Data Mining
# Tytus Planck and Kyle Rossman
import csv
import math


#Function Definition
def defineK():
    # Asks User to define a value for K and then saves it.
    x = 5
    return x


#Function Definition
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


#Function Definition
def generateApproximationMatrix(k, data):
    # This will call the function that will find all approximations for one instance. It will loop this so it can have an array of approximations for all instances.
    index = 1
    approximationMatrix = []
    while index < len(data):
        approximationMatrix.append(approximateOneInstance(data, index))
        index = index + 1
    printResults(approximationMatrix)
    return approximationMatrix  # returns array of approximations for each

# Will Take one instance and find all of the approximations to the other instances


#Function Definition
def approximateOneInstance(data, index):
    instanceIndex = 1
    # Array of 520 floats containing the approximation to current instance for each object.
    approximationArray = []
    while instanceIndex < len(data):
        approximationArray.append(findRowApproximation(data[instanceIndex], data[index]))
        instanceIndex = instanceIndex + 1
    # Will return an array of the approximation of each instance to the current one
    return approximationArray

# Takes one row of the table and finds it's approximation to the other.


#Function Definition
def findRowApproximation(row1, row2):
    totalApproximation = 0
    smc = getSMCProximity(row1, row2)
    euc = getEuclidianProximation(row1, row2)
    totalApproximation = ((8 * smc) + (4 * euc)) / 12.0 
    return totalApproximation

#Function Definition
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

    return match / total  # Calculates the SMC Proximation

#Function Definition
def getEuclidianProximation(row1, row2):
    euc = (int(row1[1]) - int(row2[1]))**2 + (int(row1[3]) - int(row2[3]))**2 + (int(row1[5]) - int(row2[5]))**2 + (int(row1[13]) - int(row2[13]))**2 
    return euc

#Function Definition
def printResults(results):
    with open("output.csv", "wb") as f:
        writer = csv.writer(f)
        writer.writerows(results)

#Function Definition
def main():
    k = defineK()
    data = getCSVData()
    generateApproximationMatrix(k, data)

if __name__ == "__main__":
    main()
