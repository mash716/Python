class Cat:
    family = ''

    def say(self):
        print('にゃー')
    
    def growl(self):
        print('ウー')
    
    def __init__(self):
        #１．第一引数 selfには名前のない猫オブジェクトが
        #   自動敵に代入されます
        #頭にselfをつける(参照するため)
        self.name = 'とら'

        #３．self はreturnしない
        #return self

tora = Cat()
tora.name

print(tora.name)