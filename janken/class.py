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
a = tora.family
tora.say()
tora.growl()

print(a)