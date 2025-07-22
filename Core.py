# Starting easy !
def Hello() -> str:
    """say hello by returning them : "Hello sir !" """
    pass


def MyAge(age: int, name: str) -> int:
    """If name is empty or age is not a valid age (below 1), your god age will be -1, otherwise it will be equal to 42 times
    the size of your name, plus your age"""
    pass


# A little tiny bit of maths !
def MyPow(x: float, n: int) -> float:
    """Return x to the power of n as a float value
    Remember that you need to consider that n may be a negative number
    Note : You are not allowed to use the "**" operator !"""
    pass


def Facto(n: int) -> int:
    """Returns the factorial of n, or -1 if n! does not exist"""
    pass


def Fibo(n: int) -> int:
    """Returns the nth term of the fibonacci sequence"""
    pass


def IsPrime(n: int) -> bool:
    """Returns true if n is a prime number. (n >= 0)"""
    pass


def SplitString(string: str, n: int) -> tuple[str, str]:
    """Split the string str at the nth index and returns the two formed string
    Example : SplitString("Hello gods !", 4) = (Hello, gods !)"""
    pass


def ToUpper(word: str) -> str:
    """Example : "ToUpper("Zeus !") = "ZEUS !" """
    pass


# This is where the fun begins !
def Atoi(string: str) -> int:
    """Convert a string containing numbers (0-9) to an integer.
    Example: Atoi("123") = 123
    Return -1 if the string is not valid: Atoi("Foo123") = -1"""

def ToBinary(n: int) -> str:
    """Convert an integer to its binary representation in a string.
    Example: ToBinary(9) = 1001
    This function won't be tested using negative or decimal numbers. Only worry about converting natural integers"""
    pass


if __name__ == "__main__":
    yourName = "Simon"
    print("Hello and welcome to the python trial, " + yourName + ".")
    assert(Hello() == "Hello sir !")
    assert(MyAge(25, "Zeus") == 4 * 42 + 25)
    assert(MyPow(8, 2) == 8.0);
    assert(Facto(5) == 120)