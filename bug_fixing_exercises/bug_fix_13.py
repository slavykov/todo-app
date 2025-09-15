def calculate_time(h, g=9.80665):
    t = (2 * h / g) ** 0.5
    return t


time = calculate_time(100)
print(time)


def greet(age, name="World"):
    """This function greet someone.
"""
    return f"Hello {name}! Your age is {age}"
