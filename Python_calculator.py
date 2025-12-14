def is_prime (num):

    status_prime = True
    max_test = int(round(num**(1/2),0))+1

    if num == 1:
        status_prime = False
        return status_prime

    for i in range(2, int(max_test), 1):
        if num % i == 0 :
            status_prime = False
            break

    return status_prime


def find_prime (start, end):
    
    prime = [i for i in range (start, end + 1, 1) if is_prime(i) == True]

    return prime



def find_square (start, end):
    
    square = [i for i in range (start, end + 1, 1) if (i ** (1/2)) % 1 == 0]

    return square


def find_factor (target_number):
    
    max_test = int (round ((target_number / 2), 0))

    factor = [i for i in range (1, max_test + 1, 1) if target_number % i == 0]
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

    common_factor = [number_1 for number_1 in factor_1 if number_1 in factor_2]

    least_common_multiple = target_number_1 * target_number_2
    
    for factor in common_factor:
        least_common_multiple /= factor

    return least_common_multiple

def main ():
    mode = 100
    while mode != 0:
        mode = int(input(
            '''input mode:
                1__find_prime(start,end).
                2__find_square(start,end).
                3__find_factor(num).
                4__find_max_common_factor(num_1,num_2).
                5__find_least_common_multiple(num_1,num_2).
                0__leave.\n
                '''))
        if mode == 0:
            break
        elif mode == 1:
            print(f'{find_prime (int(input('\ninput start:  \n')), int(input('\ninput end:  \n')))}\n')
        elif mode == 2:
            print(f'{find_square (int(input('\ninput start:  \n')), int(input('\ninput end:  \n')))}\n')
        elif mode == 3:
            print(f'{find_factor (int (input ('\ninput number to be factored: \n')))}\n')
        elif mode == 4:
            print(f'{find_max_common_factor(int(input('\ninput target number 1:  \n')), int(input('\ninput target number 2:  \n')))}\n')
        elif mode == 5:
            print(f'{find_least_common_multiple(int(input('\ninput target number 1:  \n')), int(input('\ninput target number 2:  \n')))}\n')

    return None
        
main()