from jdata import jdata
import sys

if __name__ == '__main__':
    if(len(sys.argv) == 1):
        print("no args given" ,file = sys.stderr)
        sys.exit(1)
    for i in range(1, len(sys.argv)):
        print(f"arg is {sys.argv[i]}")
        data_obj = jdata(sys.argv[i])
        if(data_obj.contains("name")):
            print(data_obj.get("name"))
