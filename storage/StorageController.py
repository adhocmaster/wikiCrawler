from abc import ABC, abstractmethod


class StorageController(ABC):
    
    def __init__(self):
        super().__init__()
    pass


    @abstractmethod
    def save(self, obj:any):
        """must return some sort of ID
        
        Arguments:
            obj {any} -- [description]
        """
        pass