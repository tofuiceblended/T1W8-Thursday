def function_a():
    print("Function A started")
    function_b()
    print("Function A ended")

def function_b():
    print("Function B started")
    function_b()
    print("Function A ended")

def function_c():
    print("Function C started")
    # Intentional Error
    result = 10 / 0 
    print("Function C ended")

 # Call the initial function
function_a()