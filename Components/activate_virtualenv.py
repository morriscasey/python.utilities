from Components.Handler import AbstractHandler
from typing import Any, Optional
import os

class WindowsHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request["os"] == "win32":
            print("* Run the following commands:")
            print("  cd " + request["path"])
            print("  "+  request["virtualEnvironmentName"] + "\Scripts\activate.bat")
            #  os.system(request["virtualEnvironmentName"] + "\Scripts\activate.bat")

        return super().handle(request)

class LinuxHandler(AbstractHandler):
    def handle(self, request:Any) -> str:
        if request["os"] == "posix":
            print("* Run the following commands:")
            print("  cd " + request["path"])
            print("  source "+ request["virtualEnvironmentName"] + "/bin/activate")
            #os.system("source "+ request["virtualEnvironmentName"] + "/bin/activate")
            return super().handle(request)