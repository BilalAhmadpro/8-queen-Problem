import random

population = []
fitnesscounter=0
board = [[0 for i in range(8)] for j in range(8)]




for i in range(4):    # initialize population (4 random samples)
    sample = []
    randomlist= random.sample(range(1, 9), 8)
    population.append(randomlist)
    
    
for i in population:   # printing initial population
    print('   Intial Population   ')
    print(i)
print('-------------------------------')


def createBoard(list1): # 2-d array visualization creation from one population
        
    for i in range(8):
        n=list1[i]
    
        board[n-1][i]=1
        
 


                 
def fitness_func(row,column,board):  # calculation of fitness of each QUEEN with with relevant Board
    
    flag = True
    
    for i in range(0,8):
      if(i!=column):
         if(board[row][i]==1):
            flag = False
            break
    x = row-1
    y = column+1
    while(x>=0 and y<=7):
        if(board[x][y]==1):
            flag = False
            break
        else:
            x = x-1
            y = y+1
    x = row+1
    y = column-1
    while(x<=7 and y>=0):
        if(board[x][y]==1):
            flag = False
            break
        else:
            x = x+1
            y = y-1

    x = row+1
    y = column+1
    while(x<=7 and y<=7):
        if(board[x][y]==1):
            flag = False
            break
        else:
            x +=1
            y +=1
    x = row-1
    y = column-1
    while(x>=0 and y>=0):
        if(board[x][y]==1):
            flag = False
            break
        else:
            x -=1
            y -=1
    
    if(flag): 
    
        global fitnesscounter 
        fitnesscounter +=1
        
        
def resetkaro():  # setting fitness counter back to 0
    
    global fitnesscounter 
    fitnesscounter=0


def emptyboard(): # Clearing Board for re-use process
    for x in range(8):
        
         for y in range(8):
             
             board[x][y]=0
             
       
def calculate_fitness(population): #fitness calculation of Whole Population
    
    fitnessvalues=[]
    for i in population:
        
        emptyboard()
        createBoard(i)
        
        for j in range(8):
            row = i[j]-1
            column = j
           
            fitness_func(row,column,board)
        fitnessvalues.append(fitnesscounter)
        resetkaro()
       
    return fitnessvalues    
          


def maxgive(fitnesvalues): # returns indices for the best 2 populations
  
  firstmax=fitnesvalues.index(max(fitnesvalues)) 
  secondmax=-1
  for i in range(fitnesvalues.__len__()):
      
    if(i != firstmax):
        if(fitnesvalues[i]>secondmax):
            secondmax=i
 
  list=[firstmax,secondmax]
  return list

fitness=calculate_fitness(population)  


def die_selection():  # dieing worst 2 populations
    for x in range(2):
     fitnesssvalues=calculate_fitness(population)
     firstmin=fitnesssvalues.index(min(fitnesssvalues))
     minlist=population.__getitem__(firstmin)
     population.remove(minlist)
   
    
    
    

    
def mutationcrossover(population): # mutation and cross-over to best 2 offsprings
    
    
 fitneslist=calculate_fitness(population)
 maxlist=maxgive(fitneslist)             
 firstparent=population.__getitem__(maxlist[0])
 
 print('best fitness list ')
 print(firstparent)
 
 secondparent=population.__getitem__(maxlist[1])
 
 print('2nd best fitness list ')
 print(secondparent)
 print('------------------------------------')
 print('Cross Over Under proccess')
 
 firstchild=[]
 secondchild=[]
 
 
 for i in range(8):
    if(i<=3):
      firstchild.append(firstparent[i])
      secondchild.append(secondparent[i])
    else :
      firstchild.append(secondparent[i])
      secondchild.append(firstparent[i])  
      
 rand1=random.randint(0, 7)
 rand2=random.randint(1, 8)
 firstchild[rand1]=rand2
 rand3=random.randint(0, 7)
 rand4=random.randint(1, 8)
 secondchild[rand3]=rand4
 

 list1=[]
 list1.append(firstchild)
 list1.append(secondchild)
 return list1



twochilds=mutationcrossover(population)
die_selection()


for y in range(2):   
 population.append(twochilds[y])
print(population)


for i in range(5000):  #iteratively chek stoopping Condition(result found or not) 
  print('---------------------------------')
  
  print('ITERATION NUMBER '+(str)(i))
  
  fitness=calculate_fitness(population)      
 
  
  flag2=False
  for x in range(4):
      if(fitness[x]>=8):
          print('Congrats Solution to 8-Queen Problem Successfully Found!')
          print('Found fitness  '+(str)(fitness[x]))
          print('population is :'+(str)(population[x]))
          flag2=True
          
  if(flag2):
     break
 
  twochilds=mutationcrossover(population)
  
  print(twochilds)
  
  for y in range(2):   
   population.append(twochilds[y])
   
  die_selection() 
  
  
if(flag2==False):
    print('---------------------------------------')
    print('Sorry for 1000 Iterations, Solution to N Queen Problem could Not Be Found')  
