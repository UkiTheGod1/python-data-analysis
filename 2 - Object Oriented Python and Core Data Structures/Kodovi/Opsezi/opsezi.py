# 1 built-in opseg

import builtins
def type(x):
    print(f"You entered x = {x}")
 
x = 1
print(builtins.type(x))  # calls the built-in type() function
type(x)  # calls our new type() function


# 2 globalni opseg

x = 10  # Promenljivu mozemo koristiti bilo gde jer je na globalnom nivou (definisana je sama za sebe, a ne unutar funkcije)

# 3 nelokanli/obuhvatni opseg


def function_outer():
    x = 5  # Defined in the enclosing scope (outer function)
    def function_inner():
        nonlocal x  # Accesses the variable from the enclosing scope
        x = 10 # Menja promenljivu van ugnjezdene funkcije, ali i dalje unutar spoljasnje funkcije
        print(f"Inside inner function x = {x}")
    function_inner()
    print(f"Inside outer function x = {x}")
 
function_outer()

# 4 lokalni opseg

def function():
    x = 10  # Local variable, accessible only within the function
    print(x)
 
function()
# print(x)  # This would raise an error because x is not accessible outside the function





# Primer

x = "global"
def outer():
    x = "enclosing"
 
    def inner():
        x = "local"
        print(x)  # Displays "local" because it's a local variable in the inner function
    inner()
    print(x)  # Displays "enclosing" because `inner` has completed, returning to `outer`
outer()
print(x)  # Displays "global" because it's outside all functions
