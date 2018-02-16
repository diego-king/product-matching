import os
import json
listFile = os.path.join(os.getcwd(), "listings.txt")
ProdFile = os.path.join(os.getcwd(), "products.txt")
ResultFile = os.path.join(os.getcwd(), "results.txt")
manu_dict = dict()
result = {}
with open(ProdFile, "r") as prodLines:
    for line in prodLines:
        lineObj = json.loads(line)
        manu = lineObj['manufacturer'].lower()
        name = lineObj['product_name'].lower()
        keywords = name.split("_")
        if 'family' in  lineObj and lineObj['family'] not in keywords:
            keywords.append(lineObj['family'].lower())

        if 'model' in  lineObj and lineObj['model'] not in keywords:
            keywords.append(lineObj['model'].lower())

        lineObj['keywords'] = keywords

        del lineObj['announced-date']

        if 'family' in lineObj:
            del lineObj['family']
        if 'model' in lineObj:
            del lineObj['model']

        # Use manufactory as key
        # Store list of entity (keywords and product name inside each entity) as value.
        if manu not in manu_dict:
            manu_dict[manu] = [lineObj]
        else:
            manu_dict[manu].append(lineObj)

resultDict = dict()
with open(listFile, "r") as listLines:
    for line in listLines:
        listObj = json.loads(line)
        cur_manu = listObj["manufacturer"].lower()
        cur_title = listObj["title"].lower()
        manu_list =list(manu_dict)
        prodList = []
        for manu in manu_list:
            # If manu is a substr as cur manu
            if (manu in cur_manu):
                prodList = manu_dict[manu]
                break

        if len(prodList) > 0:
            max_count = 0
            prod_name = ""
            for product in prodList:
                count = 0
                keywords = product['keywords']
                for keyword in keywords:
                    if (keyword in cur_title):
                        count = count + 1
                if count > max_count:
                    prod_name = product['product_name']

            if len(prod_name) > 0:
                if prod_name not in resultDict:
                    resultDict[prod_name] = [listObj]
                else:
                    resultDict[prod_name].append(listObj)

with open(ResultFile, "w") as f:
    keys = list(resultDict)
    for key in keys:
        listofListObj = resultDict[key]
        resultObj = { 'product_name':key, "listings": listofListObj}
        line = json.dumps(resultObj)
        f.write(line)
        f.write('\n')