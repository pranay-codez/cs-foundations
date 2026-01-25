import os

FILENAME = "tasks.txt"

def add_tasks():
    with open(FILENAME,"a") as f:
        note=input("Type your desired task :")
        f.write(note + "\n")

def read_tasks():
    if not os.path.exists(FILENAME):
        print("No file available")
    
    with open(FILENAME , "r") as f:
        tasks=f.readlines()
        if not tasks:
            print("No tasks added")
        else:
            print("TASKS :")
            for i,task in enumerate(tasks,start=1):
                print(f"{i}.{task.strip()}")

def main():
    print("-----------options------------")
    print("\n1. For adding task\n2. For reading the tasks\n3. Exit")
    while True:
        option=int(input("enter options 1,2 or 3 : "))
        if option==1:
            add_tasks()
        elif option==2:
            read_tasks()
        elif option==3:
            print("Exiting...")
            break
        else:
            print("Entered the wrong option")

main()
    

