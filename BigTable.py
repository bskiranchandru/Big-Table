# BigTable in python

'''def mMyTable(data, row, col):
    Table = []
    val = int(input("enter the values"))
    for i in range(row):
        for j in range(col):
            Table.append(i) '''
'''def table_row(column_sizes: list, row: list):
    output = ""
    for idx, value in enumerate(row): # assuming length of row is same as column_sizes
        val = " " + str(value)
        while len(val) < column_sizes[idx]:
            val += " "
        output += val + ""
    return output

def table_top(column_sizes: list):
    output = "" 
    for idx, column_size in enumerate(column_sizes):
        output += "" * column_size
        if idx != len(column_sizes) - 1:
            output += ""
    output += ""
    return output
def table_bottom(column_sizes: list):

    output = "" 
    for idx, column_size in enumerate(column_sizes):
        output += "" * column_size
        if idx != len(column_sizes) - 1:
            output += ""
    output += ""
    return output


# Find the size for each column. This could be implemented
# different ways depending on your data format.

data = [
    [1, 7, 23,44],
    [9,8,88,22],
    [6,8,32,23]
] 
column_sizes = [0 for i in range(len(data[0]))] # eg [0, 0, 0]
print(column_sizes)
for row in data:
    for idx,col in enumerate(row):
        if len(str(col)) > column_sizes[idx]: 
            column_sizes[idx] = len(str(col)) + 4 # spaces on either side
print(column_sizes) # [6, 8, 7]



      

for row in data:
    print(table_row(column_sizes, row))
    

print(table_bottom(column_sizes))'''

class main:
    def __init__(self, Table, row, col):
        self.Table = Table
        self.row = row
        self.col = col
    def Sum(self, directions=0):
        rl= []
        total = 0
        
        if(directions == 0):
            k = 0
            for i in range(self.row):
                #k = 0
                total = 0
                l1 =[]
                for j in range(self.col):
                    if(k<self.col):
                        total += self.Table[k][1]
                    l1.append(total)
                    
                        
                k = k+1
                    
                    
                rl.append(sum(l1))
            return rl
        elif(directions == 1):
            total = 0
            l = []
            l2 = []
            for i in range(self.row):
                k = 0
                for j in range(self.col):
                    if(k<self.row):
                        total += self.Table[k][j]
                    l2.append(total)
                    k = k+1
                l.append(sum(l2))
            return l
            
        else:
            return 
    def max(self, directions=0):
        if(directions == 0):
            k = self.Table[0][0]
            x = 0
            for i in range(self.row):
                
                for j in range(self.col):
                    if(x< self.row and self.Table[x][j] > k):
                        k = self.Table[x][j]
            return k
            #for i in range(self.col):
                #l=[]
                #ma = max(Table[row][1])
                #l.append(ma)
                #return l
            
        elif(directions == 1):
            k = self.Table[0][0]
            x= 0
            for i in range(self.row):
                
                for j in range(self.col):
                    if(x < self.col and self.Table[i][x] > k):
                        k = self.Table[i][x]
            return k
    def min(self, directions=0):
        if(directions == 1):
            k = self.Table[0][0]
            x = 0
            for i in range(self.row):
                
                for j in range(self.col):
                    if(x< self.row and self.Table[i][j] < k):
                        k = self.Table[x][j]
            return k
            #for i in range(self.col):
                #l=[]
                #ma = min(Table[row][1])
                #l.append(ma)
                #return l
            
        elif(directions == 0):
            k = self.Table[0][0]
            x= 0
            for i in range(self.row):
                
                for j in range(self.col):
                    if(x < self.col and self.Table[i][x] < k):
                        k = self.Table[i][x]
            return k
    
    def Sort(self, directions = 0, ind=1):
        l1= []
        if(directions == 0):
            for j in range(self.row):
                l=[]
                for i in range(self.col):
                    l.append(self.Table[j][i])
                l1.append(sorted(l))
            return l1
        elif(directions == 1):
            for i in range(self.row):
                l=[]
                for j in range(self.col):
                    l.append(self.Table[i][j])
                l1.append(sorted(l)) 
            return l1 
    def percentile_rank(self, directions=0):
        #pass
        l=[]
        if(directions == 0):
            ta = []
            for i in range(self.row):
                for j in range(self.col):
                    value = self.Table[i][1]/main(self.Table,2,3).max(0)
                    new = ta.append(value*100)
            return ta
        elif(directions == 1):
            
            ta = []
            for i in range(self.row):
                for j in range(self.col):
                    value = self.Table[1][j]/main(self.Table,2,3).max(0)
                    new = ta.append(value*100)
            return ta
    def Min(self, Sum, min, directions = 0):
        if(directions == 1):
            #print(main(self.Table,2,3).Sum().min(directions=1))
            print(main(self.Table,2,3).Sum(0)[1])
        elif(directions == 0):
            #print(main(self.Table,2,3).Sum().min(directions=0))
            print(main(self.Table,2,3).Sum(0)[0])
    def Percetaile(self,Sum, directions = 0):
        if(directions == 0):
            k= main(self.Table,2,3).Sum(0)[0]/100
            print(k*main(self.Table,2,3).percentile_rank(0)[0]*100)
    def Add(self,ind,):
        table =[1,2,3]
        if(ind< self.col and ind < self.row):
            self.Table[ind][ind] = table
        else:
            self.Table.append(table)

        print(self.Table)
    def get(self, row , col):
        for i in range(self.row):
            for j in range(self.col):
                if(self.row == row and self.col == col):
                    print(self.Table[row][col])
                    return True
        return False

        
            


data = [
    [20, 4, 23,44],
    [44,8,88,22],
    [6,8,32,23]
] 
b= main(data,3,4)
print(b.Sum(1))
#print(b.max(0))
#print(b.min(1))
#print(b.Sort(1))
#print(b.percentile_rank(1))
#b.Min(b.Sum,b.min,0)
#b.Percetaile(b.Sum, 0)
#b.Add(8)
#b.get(1,1)