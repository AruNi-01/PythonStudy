import datetime


# @property 装饰器负责把一个方法变成 属性调用
class Student(object):

    # 把一个 getter 方法变成属性，只需要加上 @property 就可以了
    @property
    def score(self):
        # 注意：属性的方法名不要和实例变量重名，因为调用s.score，首先转换为方法调用，在执行return self.score时，又视为访问self的属性，于是又转换为方法调用，造成无限递归
        return self._score

    # @score.setter，负责把一个 setter 方法变成 属性赋值
    @score.setter
    def score(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('score must be an integer or float')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100')
        self._score = value

    # 定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性，比如下面的 age
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    # age 通过 birth 算出，只暴露 getter 方法
    @property
    def age(self):
        return datetime.date.today() - self._birth


if __name__ == '__main__':
    s = Student()
    s.score = 90  # OK，实际转化为s.set_score(60)
    print(s.score)  # OK，实际转化为s.get_score()
    # s.score = 9999  # ValueError: score must between 0~100

