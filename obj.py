# class Player:
#     pass    # pass does nothing in Python 

""" 
Lets modify the class so that it prints the phrase "Player Object Created" 
when executed. We can do this by adding an __init__ method (function).
Most of the time we want attributes to be set when the object is created. 
Self is the first parameter to init method (function). It provides a reference
or pointer to the object in question - essentially the location in memory
where information about this object is stored. Named values (variables) 
associated with an instance of an object are called instance variables, attributes,
or object variables. 
"""
# class Player:
#     def __init__(self,gender,health):
#         self.gender = gender
#         self.health = health
#         print("Player Object Created",self.gender,self.health) 


# p1 = Player('F',110)
# p2 = Player('M',100)

""""
Once an object is created you can access its atttributes by using the 
dot notation 
"""

# print(p1.health)
# print(p1.gender)
# print(p2.health)
# print(p2.gender) 

#You can also modify the values in an object
# p1.health = 200
# p2.health=p2.health-40
# print(p1.health)
# print(p2.health)

#Function defined inside class are called methods
class Player:
    def __init__(self,gender,health,name,defaultWeapon,credits):
        self.gender=gender
        self.health=health
        self.name = name
        self.defaultWeapon = defaultWeapon
        self.credits=credits 
        print("Player Object Created",self.gender,self.health)

    def playerHurt(self,damage):
        self.health=self.health-damage
        print("Damage=",damage,"New Health=",self.health)
    
    def isDead(self):
        if self.health<=0:
            return True
        else:
            return False

p1=Player("F",110)
p2=Player("M",100)
p1.playerHurt(20)
p2.playerHurt(100)
print(p1.isDead()) 
print(p2.isDead()) 