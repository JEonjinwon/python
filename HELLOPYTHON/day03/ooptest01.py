class Animal:
    def __init__(self):#__init__은 constructor 역할  (생성자)  new 하면 생긴다 
        self.age=0 # self.xxx 이게 전역변수
        print("constructor")
    def getOld(self):
        self.age+=1

class Protoss:
    def __init__(self):
        self.mindcontrol=1
    def thought(self):    
        self.mindcontrol+=1

class Human(Animal,Protoss):
    def __init__(self):    
        Animal.__init__(self) 
        Protoss.__init__(self)
        self.name="김철수"
    def changeName(self,name):
        self.name=name

        
if __name__=='__main__':
    animal = Animal()
    print(animal.age)    
    animal.getOld()
    print(animal.age)
    human = Human()
    human.changeName("전진원")
    print(human.name)
    human.getOld()
    human.thought()
    print(human.age)
    print(human.mindcontrol)
    
    
    
    
