# python 使用类创建结构体
class Myclass(object):
    class Struct(object):
        def __init__(self, name, age, job):
            self.name = name
            self.age = age
            self.job = job

    def make_struct(self, name, age, job):
        return self.Struct(name, age, job)


myclass = Myclass()
test1 = myclass.make_struct('xsk', '22', 'abc')
test2 = myclass.make_struct('mtt', '23', 'def')

print(test1.name)
print(test1.age)
print(test1.job)
# print
# test2.name
# print
# test2.age
# print
# test2.job