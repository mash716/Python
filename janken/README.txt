__init__

オブジェクトとは。「値」と「処理」をまとめたもの

tora.name
'とら'
tora.family
'ねこ'
tora.say()
にゃー
tora.growl()
うー

クラスとは、共通の「値」と「処理」をまとめたもの
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

インスタンス化とはクラスからオブジェクトを作る事
オブジェクト = クラス名()
tora = Cat()
tora.family
'猫'
tora.say()
にゃー
tora.growl()
ウー

__init__とは、インスタンスか化するときの処理を書く関数
tora = Cat()
tora.name = 'とら'

selfという文字をたくさんみるのですが、selfには「生まれたての猫」
が入ってます
