# To convert our folders to packages because of making any update after submitting the project should update and provide the new package
from setuptools import setup,find_packages
from typing import List

Hypen_e_dot =  '-e .'

def get_requirments(file_path:str) -> List: #file_path is in string converting to List
    requirments = []
    with open(file_path) as file:
        requirments = file.readlines()  #if we see the file there we have one library in one line so while
        #reading this will also calculate that gap also as \n so to avoid this
        '''for req in requirments.txt:
            req.replace("\n","") #and also i can write in another form'''
        requirments = [req.replace('\n','') for req in requirments]
        if Hypen_e_dot in requirments:
            requirments.remove(Hypen_e_dot)
    return requirments



setup(
    name = "House Price",
    version = "0.01",
    author = "Bhuvan",
    author_email = "bhuvankatakam@gmail.com",
    packages = find_packages(),
    install_requires = get_requirments('requirments.txt')
    )

