from storage.StorageController import StorageController
from library.Configuration import Configuration


class FileStorageController(StorageController):

    def __init__(self):
        # check if the directory exists
        self.directory = Configuration.get