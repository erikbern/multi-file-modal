from modal import Stub, web_endpoint

from .lib import f

stub = Stub()

@stub.function()
@web_endpoint()
def web(x: int):
    res = f(x)
    print("res:", res)
    return res


@stub.function()
def fun(x: int):
    res = f(x)
    print("res:", res)
