class Create1x2:
    def __init__(self,choices,guarantee,singles,doubles,triples,path):
        self.choices = choices
        self.guarantee = guarantee
        self.singles = singles
        self.doubles = doubles
        self.triples = triples
        self.path = path
        self.creator()
    def creator(self):
        wanted = f"{self.singles}_{self.doubles}_{self.triples}"
        try:
            with open(f'{self.path}/{wanted}/{wanted}_{self.guarantee}.txt','r') as reading:
                temp = reading.read().splitlines()
        except:
            return
        sablon = []
        slice = wanted.split("_")
        for c,_slice in enumerate(slice):
            if(int(_slice) == 0):
                continue
            if(c==0):
                for i in range(int(_slice)):
                    sablon.append([1])
            elif(c==1):
                for i in range(int(_slice)):
                    sablon.append([1,0])
            elif(c==2):
                for i in range(int(_slice)):
                    sablon.append([1,0,2])
        singles = []
        doubles = []
        triples = []
        for c,_choices in enumerate(self.choices):
            if(len(_choices) == 1):
                singles.append(c)
            elif(len(_choices) == 2):
                doubles.append(c)
            elif(len(_choices) == 3):
                triples.append(c)

        s_singles = []
        s_doubles = []
        s_triples = []    
        for c,_sablon in enumerate(sablon):
            if(len(_sablon) == 1):
                s_singles.append(c)
            elif(len(_sablon) == 2):
                s_doubles.append(c)
            elif(len(_sablon) == 3):
                s_triples.append(c)
        
        all = []
        for _temp in temp:
            sonuc = [-1 for i in range(15)]
            for c,_s_singles in enumerate(s_singles):
                ekle = _temp[_s_singles]
                if(ekle == "X"):
                    ekle = 0
                sonuc[singles[c]] = int(ekle)
            for c,_s_doubles in enumerate(s_doubles):
                
                if(_temp[_s_doubles] == "1"):
                    ekle = "x"
                elif(_temp[_s_doubles] == "X"):
                    ekle = "y"
                if(ekle == "X"):
                    ekle = 0
                sonuc[doubles[c]] = ekle
            for c,_s_triples in enumerate(s_triples):
                ekle = _temp[_s_triples]
                if(ekle == "X"):
                    ekle = 0
                sonuc[triples[c]] = int(ekle)
            all.append(sonuc)
        for r,_all in enumerate(all):
            for c,__all in enumerate(_all):
                if(len(self.choices[c]) == 1):
                    all[r][c] = self.choices[c][0]
                elif(len(self.choices[c]) == 2):
                    if(all[r][c] == "x"):
                        all[r][c] = self.choices[c][0]
                    else:
                        all[r][c] = self.choices[c][1]
            
        all2 =  set()      
        for i in all:
            all2.add(self.listToString(i))  
        print(len(all2),len(temp))
    def listToString(self,s):
        str1 = ""
        for ele in s:
            if(ele == 0):
                ele = "X"
            str1 += str(ele)
        return str1             
