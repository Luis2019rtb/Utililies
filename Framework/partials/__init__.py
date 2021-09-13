import time
import json
import os
import re


def configurationFile(fileName='config.json'):
    currentDir = f'{os.getcwd()}'
    print(os.getcwd())
    print(os.getcwdb())
    filePath = os.path.join(currentDir, fileName)
    # print(currentDir)
    # print(f"The configuration file is on =>{filePath}")
    isValidPath = os.path.exists(filePath)
    if(isValidPath == True):
        print(filePath)
        return filePath
    # print(f"Is a valid file path =>{isValidPath}")
    if(isValidPath == False):
        # print("Setting valid path")
        frameWorkPath = os.path.join(currentDir, 'Framework')
        filePath = os.path.join(frameWorkPath, fileName)
        # print(filePath)
        return filePath


print('****************************************')
print(configurationFile())
print('****************************************')

# Waiting an amount of time


def wait(seconds):
    print("Waiting ==> " + str(seconds))
    return time.sleep(seconds)


def getJson():
    jsonObject = ''
    configuration_file = configurationFile()
    try:
        with open(configuration_file) as jsonFile:
            jsonObject = json.load(jsonFile)
            jsonFile.close()
            return jsonObject
    except FileNotFoundError as e:
        print(configuration_file)
        raise Exception("An error ocour when reading the json file " + e)
