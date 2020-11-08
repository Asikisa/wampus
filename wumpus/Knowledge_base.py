from wumpus.utils import *
import re


class Expr:

    def __init__(self, op, **args):
        self.op = unwrap_op(op)
        self.args = map(toexpr, args)


def toexpr(e):
    if isinstance(e, Expr):
        return e
    if isinstance(e, int) or isinstance(e, float):
        return Expr(e)
    res = re.sub(r'([a-zA-Z0-9_.]+)', r'Expr("\1")', e)
    return Expr(res)
