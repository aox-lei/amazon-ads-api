from enum import Enum


class A(str, Enum):
    a = "A"
    a1 = "A1"


class B(Enum):
    a = A.a
    a1 = A.a1

s = "a"
print(type(B[s].value))