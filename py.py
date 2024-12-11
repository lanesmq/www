class Animal:
    def __init__(self, animal_name, animal_type):
        self.animal_name = animal_name
        self.animal_type = animal_type

    def make_sound(self):
        print(f"{self.animal_name} makes a sound.")

    def show_animal_info(self):
        print(f"{self.animal_name} is a {self.animal_type}.")


class Job:
    def __init__(self, job_title, salary):
        self.job_title = job_title
        self.salary = salary

    def work(self):
        print(f"Working as a {self.job_title}.")

    def show_job_info(self):
        print(f"Job: {self.job_title}, Salary: ${self.salary}")


class Human(Animal, Job):
    def __init__(self, name, age, animal_name, animal_type, job_title, salary):
      
        Animal.__init__(self, animal_name, animal_type)
        Job.__init__(self, job_title, salary)
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name}. I am {self.age} years old.")
    
    def interact_with_animal(self):
        print(f"{self.name} is playing with {self.animal_name}.")
        self.make_sound() 

    def perform_work(self):
        print(f"{self.name} is working as a {self.job_title}.")
        self.work()  

human1 = Human(name="John", age=30, animal_name="Rex", animal_type="Dog", job_title="Software Developer", salary=6000)


human1.introduce() 
human1.show_animal_info() 
human1.show_job_info() 
human1.interact_with_animal() 
human1.perform_work()  
