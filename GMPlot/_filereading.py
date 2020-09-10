import numpy as np


def getvalue(string_with_data):
    aa = string_with_data
    hashindex = string_with_data.find('#')
    newstr = ''.join((ch if ch in '0123456789.-e' else ' ')
                        for ch in aa[0:hashindex])

    numbers = [float(i) for i in newstr.split()]

    return numbers


def read_schroedinger(filepath):
    '''
    Reads the file "schrodinger.inp" containing special formated user data
    describing the problem

    Args:
        filepath: Filepath of "schrodinger.inp"

    Returns:
        Dictionary containing the needed data for further calculations
    '''

    list_of_data = open(filepath, 'r').readlines()

    alldata = dict()

    massstring = list_of_data[0]
    alldata['mass'] = getvalue(massstring)[0]

    interpolationstring = list_of_data[1]
    alldata['xmin'] = getvalue(interpolationstring)[0]
    alldata['xmax'] = getvalue(interpolationstring)[1]
    alldata['nPoints'] = getvalue(interpolationstring)[2]

    EVstring = list_of_data[2]
    alldata['EVmin'] = getvalue(EVstring)[0]
    alldata['EVmax'] = getvalue(EVstring)[1]

    inttypestring = list_of_data[3]
    seperator = '\t' if '\t' in inttypestring else ' '
    alldata['inttype'] = inttypestring.split(seperator)[0]

    intpointsstring = list_of_data[4]
    alldata['intpoints'] = getvalue(intpointsstring)[0]

    alldata['xyvalues'] = np.loadtxt(filepath, skiprows=5)

    return(alldata)

file = 'schrodinger.inp'

print(read_schroedinger(file))