'''
import pandas as pd 
import numpy as np 
class Test:
    def main():
        abc={
            "Name":["raj","ranit","nishi"],
            "Roll":[1,2,3]
        }
        x=pd.DataFrame(abc)
        print(x)
Test.main()
'''

import pandas as pd 
import numpy as np 
class Test:
    def main():
        x = []
        y = []
        n=int(input("Enter number of values:"))
        for i in range(0,n):
            ch1=input("Enter the name:")
            x+=str(ch1)
            ch2=int(input("Enter the roll no.:"))
            y.append(ch2)
        abc={
            "Name" : x,"Roll no.":y}
        ch=pd.DataFrame(abc)
        print(x)
Test.main()

