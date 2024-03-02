import scheldueInputs

day = scheldueInputs.day()
freeHoursArr = day.monday#quick fix, would want to add days seperatly, this is hours they're free

#these variables below are hard coded but would get from car data in acutal practical use but we do not have that ability at this time
timeToCharge = 360#seconds to charge Nyobolt to full from 0(according to chatbot)
currentCharge = 0.2#decimal of current chare, 1 = 100%
capcity = 85#capacity of electric cars in kw


energyCostArr = [0.12, 0.11, 0.12, 0.12, 0.11, 0.13, 0.16, 0.18, 0.17, 0.16, 0.15, 0.15, 0.17, 0.14, 0.14, 0.14, 0.3, 0.31, 0.31, 0.19, 0.18, 0.17, 0.16, 0.16]#avergae energy cost by hour per kw in £
costsAvailiableArr = []#all costs when they're free
timesArr = []#has the corrosponding times of above array

for i in range(len(freeHoursArr) - 1):#adds the costs when they're free
    costsAvailiableArr.append(energyCostArr[freeHoursArr[i]])
    timesArr.append(freeHoursArr[i])

lowestCPH = 1
bestTime = 0
for i in range(len(costsAvailiableArr)):#finds lowest cost per hour
    if costsAvailiableArr[i] < lowestCPH:
        lowestCPH = costsAvailiableArr[i]
        bestTime = timesArr[i]

#maths to find cost
cost = ((((1 - currentCharge) * timeToCharge) / 60) / 60) * lowestCPH * capcity#costo to charge
print(f"You should start charging at {bestTime} and it will cost you £{round(cost, 2)}")