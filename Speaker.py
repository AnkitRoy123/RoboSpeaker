import os

if __name__ == "__main__":
    while True :
        x = input("Type that you speak to AI: ")
        if x == "q":
            break
        command = f"echo '{x}'"
        os.system(command)
