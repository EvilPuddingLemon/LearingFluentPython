class Struggle:
    def __len__(self):
        return 23
from collections import abc
print(isinstance(Struggle(), abc.Sized))
print(issubclass(Struggle, abc.Sized))
