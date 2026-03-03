import os
import json


class _DLib:
    def __init__(self, name, url, dict):
        self.name = name
        self.url = url
        self.dict = dict

    def get_name(self):
        return self.name

    def get_url(self):
        return self.url

    def get_dict(self):
        return self.dict

    def set_name(self, new_name):
        self.name = new_name

    def set_url(self, new_url):
        self.url = new_url

    def set_dict(self, new_dict: dict):
        self.dict = new_dict

    def change_url(self, new_url):
        os.replace(self.url, new_url)
        self.url = new_url

    
class Passage(_DLib):
    def __init__(self, name, url, data: dict):
        _DLib.__init__(self, name, url, data)
    
    def search_value(self, argID):
        return dict.get(self.dict, argID)
    
    def check(self, script, args: dict):
        key = args.keys().__str__().lstrip("dict_keys").strip("([''])")
 
        key_dict = self.search_value(key)
        #print(args)
        fi = {key: key_dict}
        #print(fi)

        try:
            assert args == fi
                
        except:
            #print("m")
            return False
            
        else: 
            #print("st")
            try:
                script()
            except:
                script
            return True       

    def __reader__(self):
        try: 
            with open(self.url,"r") as file:
                return json.load(file)
        except: 
            raise FileNotFoundError
    
    def __key_value__(args: dict) -> dict:
        try:
            for data_key, data_value in args.items():
                return data_key, data_value
        except AttributeError as a: 
            print(a)
            return a
        except ReferenceError as r: 
            print(r)
            return r
        
    def __case__(self, args: dict):
        data = self.dict.copy()
        key = args.keys().__str__().lstrip("dict_keys").strip("([''])")
              
        key_dict = self.search_value(key)
 
        try:
            assert args == {key: key_dict}
            
        except:
            data.update(args)
                    
        return data

    def writer_(self, *args: dict):        
        for arg in args:
            new_data = self.__case__(arg)
              
        if new_data != self.dict:
            self.dict.update(new_data)
            try:
                with open(self.url,"w") as file: 
                    json.dump(new_data, file, indent = 4) 
                  
            except FileNotFoundError: 
                os.mkdir("_internal/library/data")
