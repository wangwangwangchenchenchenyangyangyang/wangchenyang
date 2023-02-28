import cocos
from cocos.layer import ColorLayer
from cocos.text import Label
from cocos.director import director
from cocos.scene import Scene
from cocos.actions import *
from cocos.sprite import Sprite


class HelloWorld(ColorLayer):

    def __init__(self):
        super().__init__(255,0,0,255)
        


if __name__ == "__main__":       
    director.init(resizable = True,caption = "wcy")
    a = HelloWorld()
    main = Scene(a)
    director.run(main)

