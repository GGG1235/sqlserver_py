
import Interface as itf
import SQLoperate as sql

from SQLoperate import Connection



def main():
    try:
        itf.Menu()
        sql.Connection()
        itf.Login()
    except Exception as err:
        print(str(err))

if __name__=="__main__":
    main()