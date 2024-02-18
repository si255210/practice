class ParentClass:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Parent Class: {self.name}")

class ChildClass(ParentClass):
    def __init__(self, names, child_property):
        # 调用父类的初始化方法
        super().__init__(names)
        self.child_property = child_property

    def display_info(self):
        # 调用父类的方法
        ParentClass('neme').display_name()
        print(f"Child Class: {self.child_property}")

# 创建子类的实例
child_instance = ChildClass("John Doe", "Some Property")

# 调用子类的方法
child_instance.display_info()
