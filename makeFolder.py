import os

def mkFolder(filepath):
    isPathExists = os.path.exists(filepath)
    if not isPathExists:
        os.makedirs(filepath)

if __name__ == "__main__":
    mkFolder(r"D:\MIUI\123")