from b08main import *


cd b81py/b21042op/
python_branch

obj = SomeObject()
obj.integer_field = 42
obj.float_field = 3.14
obj.string_field = "some string"

chain.handle(obj, EventGet(str))



chain = IntHandler(FloatHandler(StrHandler(NullHandler)))
