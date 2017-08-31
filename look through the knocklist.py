import numpy as np
import re
import logging, os, json, sys, time


def getdefaults(pos):
    f = open('ports.txt', 'r')
    u = 1
    for line in f:
        print(line)
        if u == int(pos):
            data = line.split(',')
            f.close()
            z = map(int, data)
            print(type(z))
            return z
        else:
            u=u+1

def getdefault2(pos):
    f = open('ports.txt', 'r')
    u = 1
    for line in f:
        print(line)
        if u == int(pos):
            data = line.split(',')
            f.close()
            z = map(int, data)
            print(type(z))
            return z

def newchecker():
    w, h = 7, 255;
    Matrix = [[0 for x in range(w)] for y in range(h)]
    print(Matrix)
    print(len(Matrix))
    print(len(Matrix[0]))
    # x = default.split(",")
    # y = np.broadcast_to(x, (256, 4))
    # print(y)
    return Matrix


def tailLog(lineno, listofips, portarray, pos):
    locator = pos
    while True:
        try:
            current = open("kern.log", "r")
            stuff = current.readlines()
            currentline = 0
            for line in stuff:
                if currentline >= lineno:
                    # print(line)
                    print("currentline: %d" % currentline)
                    print("lineno: %d" % lineno)

                    pattern = re.compile(
                        r"\w{3}\s\d+\s\d+:\d\d:\d\d\s\w+\skernel:\s\[\s\d+\.\d+\]\sIN=\w+\sOUT=\sMAC=\w\w:\w\w:\w\w:\w\w:\w\w:\w\w:\w\w:\w\w:\w\w:\w\w:\w\w:\w\w:\w\w:\w\w\sSRC=(\d+\.\d+\.\d+\.\d+)\sDST=\d+\.\d+\.\d+\.\d+\sLEN=\d+\sTOS=\S+\sPREC=\S+\sTTL=\d+\sID=\d+\s\w+\sPROTO=\w+\sSPT=\d+\sDPT=(\d+)\sWINDOW=\d+\sRES=\S+\s\w+\sURGP=\d+")
                    string = line
                    something = re.search(pattern, string)
                    if something:
                        ip = something.group(1)
                        # print(something.group(1))  # ip
                        ports = something.group(2)
                        # print(something.group(2))  # port
                        x = int(ip[10:])
                        # print("#####################")
                        # print(x)
                        # print("#####################")
                        print ("192.168.1.%d knockarray is %s" % (x, listofips[int(x)]))
                        if listofips[x][0] <= 35:
                            listofips[x][0] = listofips[x][0] + 1
                            print(listofips[x])
                            time.sleep(.01)

                            if listofips[x][
                                1] == 0:  # if the stuff in the 2nd spot of the array is 0, and the port is correct set it to 1
                                if int(ports) == int(portarray[1]):
                                    listofips[x][1] = 1

                            elif listofips[x][
                                2] == 0:  # else if the stuff in the 3rd spot of the array is 0, and the previous spot in the array is not a 0, and the port is correct, set it to 1
                                if listofips[x][1] != 0:
                                    if int(ports) == int(portarray[2]):
                                        listofips[x][2] = 1

                            elif listofips[x][
                                3] == 0:  # else if the stuff in the 4rd spot of the array is 0, and the previous spot in the array is not a 0, and the port is correct, set it to 1
                                if listofips[x][2] != 0:
                                    if int(ports) == int(portarray[3]):
                                        listofips[x][3] = 1

                            elif listofips[x][
                                4] == 0:  # else if the stuff in the 5th spot of the array is 0, and the previous spot in the array is not a 0, and the port is correct, set it to 1
                                if listofips[x][3] != 0:
                                    if int(ports) == int(portarray[4]):
                                        listofips[x][4] = 1

                            elif listofips[x][
                                5] == 0:  # else if the stuff in the 6th spot of the array is 0, and the previous spot in the array is not a 0, and the port is correct, set it to 1
                                if listofips[x][4] != 0:
                                    if int(ports) == int(portarray[5]):
                                        listofips[x][5] = 1


                            elif listofips[x][
                                6] == 0:  # else if the stuff in the 6th spot of the array is 0, and the previous spot in the array is not a 0, and the port is correct, set it to 1
                                if listofips[x][5] != 0:
                                    if 5 >= (int(ports) - int(portarray[6])):
                                        listofips[x][6] = int((1 + int(ports) - int(portarray[6])))





                            elif (listofips[x][6] != 0) and (listofips[x][5] == 1) and (listofips[x][4] == 1) and (
                                        listofips[x][3] == 1) and (
                                        listofips[x][2] == 1) and (listofips[x][1] == 1):
                                print("POSTKNOCK SUCCESSFUL")
                                if listofips[x][6] == 1:
                                    print("turning left going forwards")
                                elif listofips[x][6] == 3:
                                    print("going forward")
                                elif listofips[x][6] == 2:
                                    print("turning right going forwards")
                                elif listofips[x][6] == 4:
                                    print("going backwards")
                                elif listofips[x][6] == 5:
                                    print("turning left going backwards")
                                elif listofips[x][6] == 5:
                                    print("turning left going backwards")
                                print(portarray)
                                print("*********************************************************************")
                                print("*********************************************************************")
                                print("*********************************************************************")
                                print("*********************************************************************")
                                print("*********************************************************************")
                                print("*********************************************************************")
                                del listofips[:]
                                listofips = newchecker()
                                del portarray[:]

                                locator = locator + 1

                                #things break here....
                                print("locator is:", locator)
                                portarray = []
                                portarray = getdefaults(int(locator))
                                print("portarray:",type(portarray))
                                print("*********************************************************************")
                currentline += 1
                time.sleep(.1)
                # if True == True:  # is the ip not my own?
                # get port
                # get source ip
                # knockport = the port that got knocked
                # ip = the ip that is the source
                #
                # Regex to parse log goes here
                # print("passed002")
        except Exception, e:
            print(e)
            currentline += 1

        lineno = currentline
        time.sleep(1)


while True:
    position = int(raw_input("what position?"))
    porta = getdefaults(position)
    boollock = newchecker()
    tailLog(0, boollock, porta, position)
