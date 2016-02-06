def birthday():
    years_list = [1991,1992,1993,1994,1995,1996]
    #3rd birthday = 1994
    #oldest = 1996
    
    
    print (years_list)

def thingsList(): 
    things = ['mozarella', 'cinderella', 'salmonella']
    print(str.capitalize(things[1]))
    print(str.upper(things[0]))
    things.pop(2)
    print(things)
          
def surpriseList():
    surprise = ["Groucho", "Chico", "Harpo"]
    #str.lower(surprise[2])
    surprise[2] = str.lower(surprise[2])
    surprise.reverse()
    surprise[0] = str.capitalize(surprise[0])
    print(surprise)
    
def frogToYank():
    e2f = {"dog": "chien", "cat": "chat", "walrus": "morse"}
    return e2f
    print(e2f)
    print(e2f["walrus"])
    

def yankToFrog():
    
    yank = frogToYank()
    print(yank["dog"])
    print(yank.values())

def multDict():
    catNames = ["Henri", "Grumpy", "Lucy"]
    animalDict= {"cats": catNames, "octopi": {}, "emus": {}}
    life ={"animals": animalDict, "plants": {}, "other": {}}    
    #There must be another way to do this...
    print (life.keys())
    print(life["animals"])    
    print(life["animals"]["cats"])

yankToFrog()