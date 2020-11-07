
def unwrap_op(op):
    if isinstance(op, int):
        return int(op)
    elif isinstance(op, float):
        return float(op)
    else:
        return str(op).strip()


