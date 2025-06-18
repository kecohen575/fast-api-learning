import re

EXPR_WHITELIST = re.compile(r'^[0-9+\-*/%.()\s\^]+$')

def safe_eval(expr: str) -> float:
    expr = expr.strip()

    if not EXPR_WHITELIST.match(expr):
        raise ValueError("Expression contains invalid characters")
    try:
        # need to better understand this and hide behind function
        return eval(expr, {"__builtins__": None}, {})
    except Exception as e:
        raise ValueError(f"Invalid expression: {e}")