from compy.types import Dict, Any, Self


class nat(int):
    """Representation of a natural number as a positive integer number.

    Static attributes:
        __used  is a dictionary that contains already created natural numbers.
                The key of a number n in that dictionary is str{n}.
    
    No instance attribute.
    
    Class methods:
        __new__(cls, prototype)  provides coercing a prototype to the type nat.  

    Methods:
        __eq__(self, another)    provides checking correctly the equality
                                 self == another.
        __ne__(self, another)    provides checking correctly the inequality
                                 self != another.
    """

    __used: Dict[str, Self] = {}

    def __new__(cls, prototype: Any) -> Self:
        try:
            ix = int(prototype)
        except ValueError:
            raise ValueError("bad prototype for nat()")
        if ix < 0:
            raise ValueError("invalid prototype value for nat()")
        # return super().__new__(cls, ix)
        sx = str(ix)  # determine the key of ix 
        if sx not in nat.__used:
            # a natural number is created only if it is not in __used
            nat.__used[sx] = super().__new__(cls, ix)
        return nat.__used[sx]

    def __eq__(self, another: Any) -> bool:
        if type(another) != nat:
            # two natural numbers can be equal only
            return False
        return super().__eq__(another)

    def __ne__(self, another: Any) -> bool:
        return not (self == another)