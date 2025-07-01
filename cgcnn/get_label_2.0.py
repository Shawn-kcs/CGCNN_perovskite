import shutil
import os

dir = os.getcwd()
f = open("label", 'w')

def oxi(label):
    with open("/home/kcs11/work/ABO3_auto/element_properties/oxidation_state",'r',encoding='UTF8') as f:
        while True:
            line = f.readline()
            if not line: break
            x = line.split()
            if label in x:
                break
    del(x[0])
    return x


def get_price(label):
    with open("/home/kcs11/work/ABO3_auto/element_properties/price",'r',encoding='UTF8') as f:
        while True:
            line = f.readline()
            if not line: break
            x = line.split()
            if label in x:
                break
    return x[2].replace(",","")


def get_label(m):
    n=0
    with open("../train_data/{0}.cif".format(m),'r',encoding='UTF8') as f:
        label = [m]
        while True:
            n=n+1
            line = f.readline()
            if not line: break
            if n in [23,24,25,26,27,28,29,30]:
               x = line.split()
               label.append(x[7])
    return label


for i in range(1000000):
    if os.path.isfile("../train_data/{0}.cif".format(i)):
        x = get_label(i)
        price = 0.0
        for i in range(1,9):
            price = price + float(get_price(x[i]))
        material_price=round(float(price)/8,4)
        cases = []
        for i in oxi(x[1]):
            for j in oxi(x[2]):
                for k in oxi(x[3]):
                    for l in oxi(x[4]):
                        for m in oxi(x[5]):
                            for n in oxi(x[6]):
                                for o in oxi(x[7]):
                                    for p in oxi(x[8]):
                                        cases.append(int(i)+int(j)+int(k)+int(l)+int(m)+int(n)+int(o)+int(p)-24)
        cases = sorted(set(cases))
        possibility = 0
        if 0 in cases:
            possibility = 1
        label = "{0}	{1}	{2}	{3}	{4}	{5}	{6}	{7}	{8}".format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8])
        f.write("{0}	{1:>e}	{2}	{3} \n".format(label,material_price,possibility,cases))
     
f.close()
