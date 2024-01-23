"""
Text types: str
Numeric types: int,float,complex
Sequence types: list, tuple, range
Mapping type: dict
Set Types: set, frozenset
Boolean type: bool
Binary Types: bytes, bytearray, memoryview
None type: NoneType
"""

#Getting the Data Type
x = 5
print(type(x))

#Setting the Data Type

#str --> x = "Hello World"
#int --> x=20
#float --> x=20.5
#complex --> x = 1j
#list --> x=["apple","banana"]
#tuple --> x=("apple","banana")
#range --> x=range(6)
#dict --> x={"name" : "John","age" : 36}
#set --> x={"apple","banana"}
#frozenset --> x=frozenset({"apple","banana"})
#bool --> x=True
#byes --> x =b"Hello"
#bytearray --> x=bytearray(5)
#memoryview x=memoryview(bytes(5))
#NoneType x = None

#To set the specific data type we need to write like data_type(...), for example x =str("Hello")