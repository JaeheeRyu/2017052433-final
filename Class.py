import pandas as pd
import Analysisfunc
import pandas as pd
import numpy as np

infos = pd.read_csv("ACTION.csv")


class Customer:
    def __init__(self, Id1, Id2):
        self.ClientId = Id1
        self.SessionId = Id2
    def info(self):
        b = int(str(self.ClientId)+str(self.SessionId))
        info = list(infos[infos['CLNT_ID_SESS_ID'] == b]['ACTION'])
        for i in range(0, len(info)):
            print(info[i], "\n")


a = Customer(5612428,1876482)
a.info()
