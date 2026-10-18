expressions = [
    "int('123e')",
    "int('91.4')",
    "524.345 ** 435345345311145345",
    "int('7.1 + 4')",
    "'4' - 2",
    "int('4 - 2')",
    "int('42')",
    "int(-12.12)"
]

for expr in expressions:
    try:
        print(f"{expr} = {eval(expr)}")
    except Exception as e:
        print(f"{expr} -> ошибка: {type(e).__name__} ({e})")
