#类名：
#-首字母大写，切记不要使用拼音
class Computer:
    def __init__(self,name,distance,damage,life):#构造函数
        self.CharacterName=name
        self.AttackDistance=distance
        self.AttackDamage=damage
        self.LifeValue=life

    def CharacterIformation(self):
        print('人物:{}'.format(self.CharacterName))
        print('攻击距离:{}'.format(self.AttackDistance))
        print('伤害:{}'.format(self.AttackDamage))
        print('生命值:{}'.format(self.LifeValue))

Monkey=Computer('Monkey',4,8,100)
Tiger=Computer('Tiger',3,10,90)
print(Monkey.CharacterIformation())
print(Tiger.CharacterIformation())
def Match(First,Second):
    First_value=First.LifeValue
    First_Damage=First.AttackDamage
    Second_value=Second.LifeValue
    Second_Damage = Second.AttackDamage
    while First_value>0 and Second_value>0:
        Second_value-=First_Damage
        First_value-=Second_Damage
        print(First_value,Second_value)
    if First_value>0:
        print("{}获胜".format(First.CharacterName))
    elif Second_value>0:
        print("{}获胜".format(Second.CharacterName))
    else:
        print('平局')
Match(Monkey,Tiger)