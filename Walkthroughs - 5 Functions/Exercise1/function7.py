def user_input_checking_list(user_list):
    for input_number in user_list:
        if input_number%2 == 0:
            return True
        else:
            pass
        
    return False
a=user_input_checking_list([1,3,5,7,9,11,21,21])
print(a)