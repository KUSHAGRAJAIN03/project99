import os, time,shutil
    
path = input("Enter Path : ")
now = time.time()

if os.path.exists(path) :
    for Delete in os.listdir(path):
        os.walk(Delete)
        Delete = os.path.join(path, Delete)
        if os.stat(Delete).st_mtime < now - 30 * 86400:
            if os.path.isfile(Delete):
                os.remove(Delete)
        else :
            print("The file is not 30 days old!")

else :
    print("Path Doesnt Exist")