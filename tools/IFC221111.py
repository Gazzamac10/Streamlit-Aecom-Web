import os
import pandas as pd
import ifcopenshell
from collections import defaultdict
import pandas as pd
import sqlite3 as sq
import numpy as np

filename = '10-132201-0000100595-ACM-STR-MDL-000001_Gary.McCarthy@aecom.ifc'

ifc_file = ifcopenshell.open(filename)

p = 'C:\\Users\\mccarthyg\\PycharmProjects\\Gaz_Python1'

def makecsv(t, name):
    return t.to_csv(os.path.join(p, str(name) + '.csv'))

toList = lambda x: [x] if isinstance(x, str) else x

def flattenlist(list):
    return [item for sublist in list for item in sublist]

def joindict(listofdicts):
    dall = {}
    for d in listofdicts:
        dall.update(d)
    return dall

def dict_reorder(item):
    return {k: dict_reoder(v) if isinstance(v, dict) else v for k, v in sorted(item.items())}

def get_quantity_single_value(x):
    quantities_dicts = {}
    for y in x.Quantities:
        if y.is_a('IfcQuantityArea'):
            quantities_dicts.update({y.Name: y.AreaValue})
        if y.is_a('IfcQuantityLength'):
            quantities_dicts.update({y.Name: y.LengthValue})
        if y.is_a('IfcQuantityVolume'):
            quantities_dicts.update({y.Name: y.VolumeValue})
        if y.is_a('IfcQuantityCount'):
            quantities_dicts.update({y.Name: y.CountValue})
        if y.is_a('IfcQuantityWeight'):
            quantities_dicts.update({y.Name: y.WeightValue})
    return quantities_dicts


def getprops(element):
    ks = element.IsDefinedBy
    ts = element.IsTypedBy
    out1 = [item for item in ks]
    ts1 = []
    for item in ts:
        if len(item) > 0:
            ts1.append(item)
    out2 = [item for item in ts1]
    return out1, out2


def hastag(productlist):
    testelements = []
    for item in productlist:
        try:
            if item.Tag:
                testelements.append(item)
        except:
            testelements = None
    return testelements


def getparamvalues(listofprops, pref):
    out1 = []
    out2 = []
    for item in listofprops:
        out1.append(pref + item.Name.upper())
        out2.append(item.NominalValue.wrappedValue)
    return out1, out2


def createdict(listA, listB):
    return dict(zip(listA, listB))


def mergedicts(listofdicts):
    d = defaultdict(list)
    for other in listofdicts:
        for k, v in other.items():
            d[k].append(v)
    return d


def proptype(params):
    propertyset = []
    quantityset = []
    for item in params:
        if item.is_a('IfcElementQuantity'):
            quantityset.append(item)
        else:
            propertyset.append(item)
    return quantityset, propertyset


def appendingdicts(dict1, dict2):
    data3 = {}
    data3.update(dict1)  # Modifies data3, not data
    data3.update(dict2)
    return data3

def makeupper(list):
    return [item.upper() for item in list]


def getuniqueparamvals(uqp, dic):
    out = []
    for item in uqp:
        if item in dic.keys():
            out.append(dic[item])
        else:
            out.append(None)
    return uqp, out


products = ifc_file.by_type('IfcProduct')
pnames = []
obj_info = []
for product in products:
    pnames.append(product.is_a())

uniquepPnames = (sorted([item for item in set(pnames)]))

listoflistofproducts = [ifc_file.by_type(item) for item in uniquepPnames]

elementswithtags = [hastag(item) for item in listoflistofproducts]
elementsout = [x for x in elementswithtags if x]

ind = 0
testbeams = elementsout[ind]
testonebeam = testbeams[0]
testonebeam2 = testbeams[-1]


def allproducts(productset):
    def getallparameters(element):

        tp = element.get_info()['type']
        tg = element.get_info()['Tag']

        singleval = getprops(element)[0]
        singleparams = [item.RelatingPropertyDefinition for item in singleval]

        propsets = proptype(singleparams)[1]

        singleprop = [item.HasProperties for item in propsets]
        singlepropName = [item.Name for item in propsets]

        instancetitles = [item for item in singlepropName]
        instanceparamnames = [getparamvalues(item, "I_")[0] for item in singleprop]
        instanceparamvalues = [getparamvalues(item, "I_")[1] for item in singleprop]
        instancedict = [createdict(instanceparamnames[i], instanceparamvalues[i]) for i in
                        range(len(instanceparamnames))]
        instancedictjoin = joindict(instancedict)

        typelist = getprops(element)[1]
        type = [item.RelatingType for item in typelist]

        proptypesets = []
        try:
            for property_definition in type[0].HasPropertySets:
                proptypesets.append(property_definition)

            typeparamslist = [item.HasProperties for item in proptypesets]
            typetitles = [item.Name for item in proptypesets]
            typeparamname = [getparamvalues(item, "T_")[0] for item in typeparamslist]
            typeparamvalues = [getparamvalues(item, "T_")[1] for item in typeparamslist]
            typedict = [createdict(typeparamname[i], typeparamvalues[i]) for i in range(len(typeparamname))]
            typedictjoin = joindict(typedict)

            instancedictjoin = appendingdicts(instancedictjoin, typedictjoin)
            instanceparamnames = instanceparamnames + typeparamname
        except:
            None
        try:
            quants = [get_quantity_single_value(item) for item in proptype(singleparams)[0]]
            quantnames = ["z_" + item for item in list(quants[0].keys())]
            quantvals = quants[0].values()
            quantdict = createdict(quantnames, quantvals)
            instanceparamnames = instanceparamnames + [quantnames]
            instancedictjoin = appendingdicts(instancedictjoin, quantdict)
        except:
            None

        return instanceparamnames, instancedictjoin, tg

    b = [getallparameters(item)[0] for item in productset]
    c = [getallparameters(item)[1] for item in productset]
    d = [getallparameters(item)[2] for item in productset]

    typ = (productset[0].get_info()['type'])
    tagdict = {'RevitId': d}

    uniqueparams = [item for item in set(flattenlist([flattenlist(item) for item in b]))]
    up = uniqueparams
    oiu = [createdict(getuniqueparamvals(up, item)[0], getuniqueparamvals(up, item)[1]) for item in c]
    mergdict = mergedicts(oiu)
    mergdict = dict_reorder(mergdict)
    outdict = appendingdicts(tagdict, mergdict)

    return typ, outdict, b

#typings = [allproducts(item)[0] for item in elementsout]
#outInst = [allproducts(item)[1] for item in elementsout]

#dataframes = [pd.DataFrame.from_dict(item) for item in outInst]
#[item.fillna(value=np.nan, inplace=True)for item in dataframes]
#[item.replace(r'', np.NaN, inplace=True) for item in dataframes]

#[makecsv(dataframes[i],typings[i])for i in range(len(dataframes))]

def getallparameters(element):
    tp = element.get_info()['type']
    tg = element.get_info()['Tag']

    singleval = getprops(element)[0]
    singleparams = [item.RelatingPropertyDefinition for item in singleval]

    propsets = proptype(singleparams)[1]

    singleprop = [item.HasProperties for item in propsets]
    singlepropName = [item.Name for item in propsets]

    instancetitles = [item for item in singlepropName]
    instanceparamnames = [getparamvalues(item, "I_")[0] for item in singleprop]
    instanceparamvalues = [getparamvalues(item, "I_")[1] for item in singleprop]
    instancedict = [createdict(instanceparamnames[i], instanceparamvalues[i]) for i in range(len(instanceparamnames))]

    instancedictjoin = joindict(instancedict)

    typelist = getprops(element)[1]
    type = [item.RelatingType for item in typelist]

    proptypesets = []

    try:
        for property_definition in type[0].HasPropertySets:
            proptypesets.append(property_definition)

        typeparamslist = [item.HasProperties for item in proptypesets]
        typetitles = [item.Name for item in proptypesets]
        typeparamname = [getparamvalues(item, "T_")[0] for item in typeparamslist]
        typeparamvalues = [getparamvalues(item, "T_")[1] for item in typeparamslist]
        typedict = [createdict(typeparamname[i], typeparamvalues[i]) for i in range(len(typeparamname))]
        typedictjoin = joindict(typedict)

        instancedictjoin = appendingdicts(instancedictjoin, typedictjoin)
        instanceparamnames = instanceparamnames+typeparamname

    except:
        None

    try:
        quants = [get_quantity_single_value(item) for item in proptype(singleparams)[0]]
        quantnames = list(quants[0].keys())
        quantvals = quants[0].values()
        instanceparamnames = instanceparamnames+quantnames
        instancedictjoin = appendingdicts(instancedictjoin,quants[0])
    except:
        None

    return tg,instanceparamnames

#print (flattenlist([toList(item)for item in getallparameters(testonebeam)[1]]))
#print (flattenlist([toList(item)for item in getallparameters(testonebeam2)[1]]))

def sendtosql(dbname,tablename,data):
    conn = sq.connect('{}.sqlite'.format(dbname)) # creates file
    data.to_sql(tablename, conn, if_exists='replace', index=False) # writes to file
    conn.close() # good practice: close connection
    return "exported"

#[sendtosql(filename,typings[i],dataframes[i])for i in range(len(dataframes))]
