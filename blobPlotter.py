# Trevor Nierman
# 02/11/2019

#
# This program was made for the Junior Software Engineering Test for LP Technologies.
# 
# It reads data from a mySQL database, converts it from hex to a signed int, and plots each 'blob' for one second.
#


import MySQLdb
import matplotlib.pyplot as pyplot
import time
import numpy as np


######################
##### Variables ######
######################

## Database Variables ##
dbUser = "root"
dbPassword = "changeme"
dbHost = "localhost"
dbName = "lpTechTest"

tableName = "test"

## Graph variables ##
graphDelay = 1
graphBackgroundColor = "black"
graphLineColor = "yellow"
graphLineWidth = 0.5

gridColor = "grey"

## Constants ##
query = "SELECT * FROM " + tableName + ";"
blobLength = 601


#####################
##### Functions #####
#####################

# Converts a list of raw blob data to hex
def convertToHex(rawBlob):

    blobHex = []
    for byte in rawBlob:
        blobHex.append('%02x' % ord(byte))
    # End for 

    return blobHex

# End function


################
##### MAIN #####
################

## Query database

dbConnection = MySQLdb.connect(user = dbUser, password = dbPassword, host = dbHost, database = dbName)
database = dbConnection.cursor()

database.execute(query)

# Database query returns list of tuples -> [trace_id, trace_data (blob), trace_time]
traceList = database.fetchall()
dbConnection.close()


## Parse data from query -> store in blobData for graphing

blobData = []

for trace in traceList:

    blobData.append([])

    # Convert to hex
    blobHex = convertToHex(trace[1])
    
    # Data values are given in 4 byte hexidecimal values -> Create groups of 4's and convert them to signed integers
    hexList = [blobHex[i:i + 4] for i in xrange(0, len(blobHex), 4)] 
    for hex in hexList:
        
        # Join subarray chunks to create hex string, convert to signed int -> signed ints then need to be scaled by a factor of 0.001 (stored as double)
        hex = "".join(hex) 
        intValue = int(hex, 16) 
        if intValue > 0x7FFFFFFF:
            intValue -= 0x100000000

        intValue = (intValue + 0.0) / 1000

        # Append to end of current blob's list of int values
        blobData[-1].append(intValue)

    # End for

# End for


## Graph data

# Create graph objects
figure = pyplot.figure()
graph = figure.add_subplot(111)
xAxis = range(850, 850 + blobLength)

# Stylize graph
graph.set_facecolor(graphBackgroundColor)
graph.set_yticks(np.arange(-130, -30, 10))
graph.set_xticks(np.arange(850, 850 + blobLength, 75))

pyplot.grid(which='both', axis='both', color=gridColor, linestyle='--')
pyplot.axis([850, 850 + blobLength, -130, -30])

# Plot initial graph
line, = graph.plot(xAxis, blobData[0], color=graphLineColor, linewidth=graphLineWidth)
figure.show()

# Loop to replay graph 
while True: 

    for i in range(len(blobData)):

        line.set_ydata(blobData[i])
        graph.set_title("Trace Time: " + str(traceList[i][2]))

        figure.canvas.draw()
        figure.canvas.flush_events()
        time.sleep(graphDelay)

    # End for

# End while

