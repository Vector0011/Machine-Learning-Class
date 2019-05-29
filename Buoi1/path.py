class Path(object):
    __path = ""
    __file_name = ""
    __is_exist = True
    def __init__(self, path,file_name):
        self.__path = path
        self.__file_name = file_name
        self.__check_self_exist()
    def output(self):
        return '\t{\n\t\t"path": "'+self.__path+'",\n\t\t"file_name": "'+self.__file_name+'",\n\t\t"oke": "'+ str(self.__is_exist) + '"\n\t}'
    def input(self, path, file_name):
        self.__path = path
        self.__file_name = file_name
        self.__check_self_exist()
    def __check_self_exist(self):
        try:
            f = open(self.__path)
        except FileNotFoundError:
            self.__is_exist = False
        except:
            print("Some errors happening somewhere")
    def write_to_file(self,path):
        try:
            f = open(path,"r")
            r = ''
            for i in f.read():
                r += i
            f.close()
            #check if all file is empty
            if '[' not in r:
                r += '['
            else:
                r = r[0:-2]
            #check if file have the '[]' but doesn't have any element
            if '"' in r:
                r += ','
            f = open(path,"w")
            r += '\n'+self.output()+'\n]'
            f.write(r)
            f.close()
        except FileNotFoundError:
            print("File not found")