def two_no(x,y):
    return x/y


def main():
    
    while True:
        try:
            num1=int(input("enter the first number :"))
            num2=int(input("enter the second number :"))
        except ValueError:
            print("Enter a number next time !!")
            return #it should have continue more accurate
        print("--------options--------")
        print("\n1 for num1 divided by num2\n2 for num2/num1\n3 for exiting")
        try:
            option=int(input("Enter the option :"))
        except ValueError:
            print("please enter a number next time")
            continue
        if option==1:
            try:
                div=two_no(num1,num2)
                print(f"the answer is {div}")
            except Exception as e:
                
                print(f"division with {e} not possible")
        elif option==2:
            try:
                div=two_no(num2,num1)
                print(f"the answer is {div}")
            except Exception as e:
                e=0
                print(f"division with {e} is not possible")
        elif option==3:
            print("Exiting...")
            break
        else:
            print("entered the wrong option!!")




    

main()
