import argparse, os

from Components.virtual_environment import CreateVirtualEnv
from Components.folder import CreateFolder, MoveIntoFolder
from Components.activate_virtualenv import WindowsHandler, LinuxHandler

# Create parameters for script
parser = argparse.ArgumentParser()
parser.add_argument("-f","--folderPath", help="Folder path for new project.")
parser.add_argument("-venv","--virtualEnvironmentName", help="Virtual Environment name.")
args = parser.parse_args()

# Extract arguments
path = args.folderPath
environmentName = args.virtualEnvironmentName

request = {
    "os": os.name,
    "virtualEnvironmentName": environmentName,
    "path": path
}


# Check and create a folder
createFolder = CreateFolder()
# Moves into created or existing folder
moveIntoFolder = MoveIntoFolder()
# Creates a virtual environment
createAVirtualEnvironment = CreateVirtualEnv()

# Handles actions based on Windows or Linux/Mac environment
windowsVirtualEnv = WindowsHandler()
linuxVirtualEnv = LinuxHandler()

createFolder.set_next(moveIntoFolder).set_next(createAVirtualEnvironment).set_next(windowsVirtualEnv).set_next(linuxVirtualEnv)

createFolder.handle(request)
