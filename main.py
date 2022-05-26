class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name="Adam", age=25, tracks=["FE","BE"],score=60):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
    def change_name(self,new_name):
        self.name = new_name
    
    def change_age(self,new_age):
            self.age = new_age

    def add_track(self,new_track):
        self.tracks = new_track
    
    def get_score(self):
        if  isinstance(self.age,int):
            print(self.name,self.age,self.tracks,self.score)
        else:
            print('Age must be int. Try again!')
        

Adam = Student(name="Adam", age=25, tracks=["FE","BE"],score=60)

# Expected methods
Adam.change_name("Samuel")
Adam.change_age(34)
Adam.add_track("Product Design")
Adam.get_score()


