import os

if __name__=='__main__':
    print("Welcome to Robo Speaker 1.0. Created by Hirak")
    while True:
        x=input("Enter what you want me to Speak:")
        if x=="q":
            break
        command=f"say {x}"
        os.system(command)
    