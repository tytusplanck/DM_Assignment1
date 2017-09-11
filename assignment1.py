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
        approximationMatrix[index] = approximateOneInstance(data[index])
        index = index + 1
    return approximationMatrix #returns array of approximations for each
}

#Will Take one instance and find all of the approximations to the other instances
def approximateOneInstance( index, instanceOfData) {

    
    return []; #Will return an array of the approximation of each instance to the current one.
}

def main():
    int k = defineK()

if __name__ == "__main__":
    main(