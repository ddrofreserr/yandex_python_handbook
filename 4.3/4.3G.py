def same_type(f):
    
    def decorated(*args):
        base = type(args[0]) 

        for each in args:
            if not isinstance((each), base):
                print('Обнаружены различные типы данных')
                return
            
        return f(*args)
        
    return decorated
