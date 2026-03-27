import traceback

def catch(fn):
    def catch_inner(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except:
            traceback.print_exc()
            return None
    return catch_inner 

def to__dict(fn):
    def to__dict_inner(*args, **kwargs):
       
        return (fn(*args, **kwargs))   
    return to__dict_inner 