#类名：
#-首字母大写，切记不要使用拼音
#人物大战小游戏。
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
pipifang=Computer('韩芳',1,8,100)
laojiang=Computer('老蒋',1,6,100)
laotang=Computer('唐宇淳',1,4,100)
def Match(First,Second):
    print(First.CharacterIformation())
    print(Second.CharacterIformation())
    print('{}与{}打架'.format(First.CharacterName,Second.CharacterName))

    First_value=First.LifeValue
    First_Damage=First.AttackDamage
    Second_value=Second.LifeValue
    Second_Damage = Second.AttackDamage
    i=0
    while First_value>0 and Second_value>0:
        i+=1
        Second_value-=First_Damage
        First_value-=Second_Damage
        print('第{}回合{} {}'.format(i,First_value,Second_value))
    if First_value>0:
        print("{}获胜,{}被暴捶".format(First.CharacterName,Second.CharacterName))
    elif Second_value>0:
        print("{}获胜,{}被暴捶".format(Second.CharacterName,First.CharacterName))
    else:
        print('平局')
Match(laotang,laojiang)