
import string

class jdata:
    def __init__(self, file_name):
        self.map = {}
        file = open(file_name)
        builder = ""
        
        buffer = file.read()
        in_brace = False
        in_bracket = False
        in_quote = False

        key = None
        val = None

        for i in range(0, len(buffer)):
            c = buffer[i]

            if(not c in string.printable and c != " "):
                continue

            if(c == '{'):
                in_brace = True
            if(c == '}'):
                in_brace = False

            if(not in_brace):
                continue
                
            if(in_bracket or in_quote):
                if(c == ']'):
                    in_bracket = False
                    key = builder
                    builder = ""
                elif(c == '\"'):
                    in_quote = False
                    val = builder
                    builder = ""
                else:
                    builder += c

            if(c == '\n'):
                self.map[key] = val
                key = None
                val = None
            if(c == '['):
                in_bracket = True
            if(c == '\"'):
                in_quote = True

        file.close()
    def contains(self, key):
        try:
            test = self.map[key]
            return True
        except:
            return False

    def get(self, key):
        if(not self.contains(key)):
            return None
        return self.map[key]

