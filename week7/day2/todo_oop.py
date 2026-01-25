import os

class TodoManager:
    def __init__(self,filename="tasks.txt"):
        self.filename=filename

    def add_tasks(self,note):
        with open(self.filename,"a") as f:
            f.write(note + "\n")
            return True

    def read_tasks(self):
        if not os.path.exists(self.filename):
            return []

        with open(self.filename,"r") as f:
            return f.readlines()
    
    def clear_tasks(self):
        with open(self.filename,"w") as f:
            pass
        return True
           


def main():
    Todo=TodoManager()
    print("----------options---------")
    while True:
        print("\n1 for adding task\n2 for reading tasks\n3 for emptying the file\n4 for exit")
        try:
            option=int(input("enter your option :"))
        except:
            print("enter a number next time")
            continue

        if option==1:
            note=input("Enter your task :\n")
            check=Todo.add_tasks(note)
            if check==True:
                print("Task added successfully")
            else:
                print("Task implementation failed")
            
        elif option==2:
            tasks=Todo.read_tasks()
            if not tasks:
                print("No tasks found !")
            for i,task in enumerate(tasks,start=1):
                print(f"{i}.{task.strip()}")
        elif option==3:
            empty=Todo.clear_tasks()
            if empty==True:
                print("Tasks are cleared")
            else:
                print("Task clearing unsuccessful")
        elif option==4:
            print("Exiting...")
            break
        else:
            print("entered the wrong option !")

main()

        
        
