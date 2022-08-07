from Components.Handler import AbstractHandler
from Components.activate_virtualenv import LinuxHandler, WindowsHandler
from typing import Any
import os

class CreateVirtualEnv(AbstractHandler):
    def handle(self, request: Any) -> str:
        os.system("python3 -m venv " + request["virtualEnvironmentName"])
        print("* Created Virtual Environment")
        return super().handle(request)
