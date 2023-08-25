
var_a = 10

def scope_function(my_var):
    my_var = 15
    return my_var






print(scope_function(var_a))
print(var_a)