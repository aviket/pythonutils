import json
from datetime import datetime

def chatshow():
    with open("conversations.json" , "r") as fl:
        jsonobj = json.load(fl)
    outfl = open("txt_backup.txt" , "w")
    for itm in jsonobj:
        print(list(itm.keys()))
        continue
        outfl.write(itm["title"] + "\n")
        outfl.write("****\n")
        dd = "Q:"
        for vl in list(itm["mapping"].values()):
            # print(vl)
            
            for cnt in vl:
   
                if type(vl[cnt]) == dict:
                   

                    outfl.write(dd + vl[cnt]["content"]["parts"][0] + "\n")
                    outfl.write( str(datetime.utcfromtimestamp(vl[cnt]["create_time"])) + "\n")
            if dd == "Q:":
                dd = "Ans: "
            else:
                dd = "Q:"
                          
            outfl.write("____\n")
        outfl.write("xxxxx\n")
    outfl.close()
                


chatshow()