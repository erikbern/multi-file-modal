from modal import Stub

from .lib import f

stub = Stub()

@stub.function()
def run(x: int):
    res = f(x)
    print("res:", res)

