class BaseVector:
    def norm(self):
        return sum([getattr(self, var) ** 2 for var in vars(self)]) ** 0.5
    
    def __str__(self):
        return str(tuple(getattr(self, var) for var in vars(self)))

    def __repr__(self):
        arg_list = [f'{key}={value}' for key, value in vars(self).items()]
        args = ' '.join(arg_list)
        return f'{self.__class__.__name__}({args})'

    def __add__(self, other):
        if type(other) != type(self):
            return NotImplemented
        kwargs = {
            var: getattr(self, var) + getattr(other, var) for var in vars(self)
        }
        return self.__class__(**kwargs)
    
    def __sub__(self, other):
        if type(other) != type(self):
            return NotImplemented
        kwargs = {
            var: getattr(self, var) - getattr(other, var) for var in vars(self)
        }
        return self.__class__(**kwargs)

    def __mul__(self, other):
        if type(other) in (int, float):
            kwargs = {
                var: getattr(self, var) * other for var in vars(self)
            }
            return self.__class__(**kwargs)
        elif type(other) == type(self):
            return sum([getattr(self, var) * getattr(other, var) for var in vars(self)])
        
        return NotImplemented

    def __eq__(self, other):
        if type(other) != type(self):
            return NotImplemented
        return all(getattr(self, var) == getattr(other, var) for var in vars(self))

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if type(other) != type(self):
            return NotImplemented
        return self.norm() < other.norm()

    def __gt__(self, other):
        if type(other) != type(self):
            return NotImplemented
        return self.norm() > other.norm()

    def __le__(self, other):
        return not self > other
    
    def __ge__(self, other):
        return not self < other

class R1Vector(BaseVector):
    def __init__(self, *, x):
        self.x = x

class R2Vector(R1Vector):
    def __init__(self, *, x, y):
        super().__init__(x=x)
        self.y = y

class R3Vector(R2Vector):
    def __init__(self, *, x, y, z):
        super().__init__(x=x, y=y)
        self.z = z
    
    def cross(self, other):
        if type(self) != type(other):
            return NotImplemented
        kwargs = {
            'x': self.y * other.z - self.z * other.y,
            'y': self.z * other.x - self.x * other.z,
            'z': self.x * other.y - self.y * other.x
        }
        return self.__class__(**kwargs)

v1 = R3Vector(x=2, y=3, z=1)
v2 = R3Vector(x=0.5, y=1.25, z=2)
print(f'v1 = {v1}', f'repr(v1)={repr(v1)}')
print(f'v2 = {v2}', f'repr(v2)={repr(v2)}')
v3 = v1 + v2
print(f'v1 + v2 = {v3}')
v4 = v1 - v2
print(f'v1 - v2 = {v4}')
v5 = v1 * v2
print(f'v1 * v2 = {v5}')
v6 = v1.cross(v2)
print(f'v1 x v2 = {v6}')