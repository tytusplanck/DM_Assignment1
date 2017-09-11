# Assignment 1 - Data Mining
# Tytus Planck and Kyle Rossman
import csv
data = []
with open('income_tr.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in csvreader:
        dataRow = []
        for item in row:
            dataRow.append(item)
        data.append(dataRow)
print data[1][0]

def defineK() {
    # Asks User to define a value for K and then saves it.
    int x = 5
    return x
}

#Will break up the data into attributes and return a matrix of approximations for each attribute.
def generateApproximationMatrix( k, data) {
    #This will call the function that will find all approximations for one instance. It will loop this so it can have an array of approximations for all instances.
    index = 0
    approximationMatrix = []
    while index < data.__len__
        approximationMatrix[index] = approximateOneInstance(data, index)
        index = index + 1
    return approximationMatrix #returns array of approximations for each
}

#Will Take one instance and find all of the approximations to the other instances
def approximateOneInstance( data, currentInstance) {

    instanceIndex = 0
    approximationArray = []     #Array of 520 floats containing the approximation to current instance for each object.
    while instanceIndex < data.__len__
        approximationArray[instanceIndex] = findRowApproximation(data[instanceIndex], data[currentIndex])
        instanceIndex = instanceIndex + 1
    return approximationArray #Will return an array of the approximation of each instance to the current one.
}

#Takes one row of the table and finds it's approximation to the other.
def findRowApproximation( row1, row2 ) {
    
}

def main():
    int k = defineK()

if __name__ == "__main__":
    main(