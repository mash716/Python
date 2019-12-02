#
# 対話モード >>> に
# コピペで動きます。
#
class Cat:
    family = '猫'
    
    def say(self):
        print('にゃー')
    
    def growl(self):
        print('ウー')

tora = Cat()
tora.family
tora.say()
tora.growl()

tora.name = 'とら'
b = tora.name
print(b)