import pandas as pd
import random as rd
import keyboard as kb

df = pd.read_excel('Vocabulary.xlsx', sheet_name='N5 Vocab')

dataList = []

for index, row in df.iterrows():
    dataList.append([row["Kana"], row["Kanji"], row["Definition/s"]])
    
total = len(dataList)

while True:
    try:
        index = rd.randrange(0, total)
        line = dataList[index]
        print("Kana : %s\nKanji : %s\nDefinition/s : %s" % (line[0], line[1], line[2]))
        print("\nLength of list : " + str(len(dataList)) + "\n")

        if (kb.read_key() == "enter"):
            dataList.pop(index)
            total = len(dataList)
            print("Pressed enter")

        elif(kb.read_key() == "space"):
            print("Pressed space")
            continue

    except:
        break
