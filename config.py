import datetime
from datetime import *
from kivy.storage.jsonstore import JsonStore
from kivy.uix.image import AsyncImage, Image

store = JsonStore('account.json')
userid = -1
dateID = datetime.today().strftime("%m%d%Y")
img_1 = Image(
    source = 'basicwitch-removebg-preview.png',
    pos_hint = {"x": .71, "y": .45},
    size_hint = [.35, .35]
    )

img_2 = Image(
    source = 'crystals-removebg-preview.png',
    pos_hint = {"x": 0, "y": .05},
    size_hint = [.35, .35]
    )
    
citrusIMG1 = Image(
    source = 'orangeflow-removebg-preview.png',
    pos_hint = {"x": .71, "y": .45},
    size_hint = [.32, .32]
    )

citrusIMG2 = Image(
    source = 'yellowflow-removebg-preview.png',
    pos_hint = {"x": 0, "y": .05},
    size_hint = [.32, .32]
    )
    
origIMG1 = Image(
    source = 'dinorain-removebg-preview.png',
    pos_hint = {"x": .71, "y": .45},
    size_hint = [.32, .32]
    )

origIMG2 = Image(
    source = 'blue-removebg-preview.png',
    pos_hint = {"x": 0, "y": .05},
    size_hint = [.32, .32]
    )
    
pinkIMG1 = Image(
    source = 'work-removebg-preview.png',
    pos_hint = {"x": .71, "y": .43},
    size_hint = [.39, .39]
    )

pinkIMG2 = Image(
    source = 'smiles-removebg-preview.png',
    pos_hint = {"x": 0, "y": .05},
    size_hint = [.34, .34]
    )
