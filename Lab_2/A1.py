width = 17
height = 12.0

expressions = [
    "width // 2",
    "width / 2.0",
    "height / 3",
    "1 + 2 * 5"
]

for expr in expressions:
    result = eval(expr)
    print(f"{expr} = {result} (тип: {type(result).__name__})")
