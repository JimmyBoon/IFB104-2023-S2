####Global
var_a = 10



def scope_function(my_var):

    ##### Local #####
    my_var = 15
    return my_var
    ##### Local End ####






print(scope_function(var_a))
print(var_a)