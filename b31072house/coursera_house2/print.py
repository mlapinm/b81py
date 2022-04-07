import zipfile
import os



def make_core():

    with zipfile.ZipFile('core.zip', 'w') as myzip:

        path = 'coursera_house/core/'
        os.chdir(path)
        for f in os.listdir():
            myzip.write(f)


if __name__ == "__main__":

    make_core()



