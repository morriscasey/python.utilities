from Components.Handler import AbstractHandler
from typing import Any,Optional
import os,sys

class CreateFolder(AbstractHandler):
    def handle(self, request: Any) -> str:
        if os.path.exists(request["path"]) == False:
            os.mkdir(request["path"])
            print("* Created folder path of "+ request["path"] + ".")
        else:
            print("* Folder already exists.")
            
        return super().handle(request)

class MoveIntoFolder(AbstractHandler):
    def handle(self, request: Any) -> str:
        initialDirectory = os.getcwd()

        try:
            os.chdir(request["path"])
            print("* Changed directory to ", os.getcwd())
        except:
            print("Not able to change directory. Exception- ", sys.exc_info())
            os.chdir(initialDirectory)
        
        return super().handle(request)
