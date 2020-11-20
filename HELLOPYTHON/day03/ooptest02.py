class Animal:
    def __init__(self):#__init__은 constructor 역할  (생성자)  new 하면 생긴다 
        self.age=0
        print("constructor")
    def getOld(self):
        self.age+=1
     
     
        
if __name__=='__main__':
    animal = Animal()
    print(animal.age)    
    animal.getOld()
    print(animal.age)