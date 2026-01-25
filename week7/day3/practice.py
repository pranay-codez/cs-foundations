class TodoManager():
    def __init__(self,filename="milestone.txt"):
        self.filename=filename

    def add_task(self,note):
        with open(self.filename,"a") as f:
            f.write(note + "\n")
            return True
    
    def read_task(self):
        try:
            with open(self.filename,"r") as f:
                f.read()
        except FileNotFoundError:
            print("File not found!!")

    def delete_task(self):
        with open(self.filename,"w") as f:
            pass
        
        
        



def main():
    Task=TodoManager()
    while True:
        print("-----------Options-----------")
        print("\n1 Add task\n2 Read task \n3 Delete tasks \n4 Exit")
        try:
            option =int(input("Enter the option :"))
        except ValueError:
            print("Enter a number next time..")
            continue
        if option==1:
            note=input("Enter your tasks")
            operation=Task.add_task(note)
            if operation==True:
                print("Task added succesfully")
            else:
                print("failed")
       



main()