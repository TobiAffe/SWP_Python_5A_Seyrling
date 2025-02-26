def order_pizza(size, *toppings, **details):
    print(f"Order a Size {size} Pizza with the following topics:")
    for topping in toppings:
        print(f"- {topping}")

    for key, value in details.items():
        print(f"- {key}: {value}")

order_pizza("large", "tomato", "pepperonis", delivery=True, tip=4)

# Aufgabe 1: Was passiert, wenn man *args und **kwargs vertauscht (def test(**kwargs,
# *args))?
# Es gibt einen Syntax Error

# Warum sollte man *args nicht mit list oder dict verwechseln?
# Da es sich um einen Tupple handelt und nicht dasselbe ist

# Bei Kwargs handelt es sich um ein dic -> kann mehr informationen beinhalten

# args in recursive

def recursive_sum(*args):
    if not args:  # Abbruchbedingung: Wenn keine Argumente mehr da sind
        return 0
    return args[0] + recursive_sum(*args[1:])  # Erster Wert + Rekursiver Aufruf mit Rest

# Test
print(recursive_sum(1, 2, 3, 4, 5))  # Ausgabe: 15

# Innere Methode
def greet(name):
    def format_name(n):  # Innere Methode
        return n.lower().strip()

    return f"Hallo, {format_name(name)}!"


# Test
print(greet("  alice "))  # Ausgabe: Hello, Alice!
