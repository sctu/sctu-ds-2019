#新建一个类
class Student:
    #定义课程
    def study_course(self,number,book,):
        self.number = number
        self.book = book


Marry = Student('11门课程','数据结构与算法')
print(Marry.number)
print(Marry.book)