import os

if __name__ == "__main__":
    x = input("Type that you speak to AI: ")
    command = f"echo '{x}'"
    os.system(command)
