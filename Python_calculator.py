def find_prime (start, end):
    prime = []

    for i in range (start, end + 1, 1): #test i
        max_test = int(round (i ** (1/2), 0))
        status = True

        for j in range (2, max_test + 1, 1):
            if i % j == 0:  
                status = False
                break
            else:
                True
        if status == True:
            prime.append (i)

    return prime

def find_square (start, end):
    square = []

    for i in range (start, end + 1, 1):
        if (i ** (1 / 2)) % 1 == 0:
            square.append (i)

    return square

def find_factor (target_number):
    factor = []
    
    max_test = int (round ((target_number / 2), 0))
    for i in range (1, max_test + 1, 1):
        if target_number % i == 0:
            factor.append (i)

    factor.append (target_number)

    return factor

def find_max_common_factor (target_number_1, target_number_2):
    factor_1 = find_factor (target_number_1)
    factor_2 = find_factor (target_number_2)

    for number_1 in factor_1[::-1]:
        if number_1 in factor_2:
            max_common_factor = number_1
            break

    return max_common_factor

def find_least_common_multiple (target_number_1, target_number_2):
    factor_1 = find_factor (target_number_1)
    factor_2 = find_factor (target_number_2)

    common_factor = []

    for number_1 in factor_1[::1]:
        if number_1 in factor_2:
            common_factor.append (number_1)

    least_common_multiple = target_number_1 * target_number_2
    
    for factor in common_factor:
        least_common_multiple /= factor
    return least_common_multiple



#print(find_prime (int(input('input start:  (>2)')), int(input('input end:  '))))
#print(find_square (int(input('input start:  ')), int(input('input end:  '))))
#print(find_factor (int(input('input number to be factored: '))))
#print(find_max_common_factor(int(input('input target number 1:  '))), int(input('input target number 2:  ')))
#print (find_least_common_multipleint(input('input target number 1:  '))), int(input('input target number 2:  ')))
