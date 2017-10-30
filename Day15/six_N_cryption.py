# uncompleted project

def prime(m,mx):
    for i in range(m,mx):
        isPrime = is_prime(i)
        if isPrime:
            yield (i)


def is_prime(num):
    return all(num % i for i in xrange(2, num))

def magic_prime(encrypt_data, keys):
    random_prime = prime(1, max(keys)/len(keys))

    magic = []
    for i in random_prime:
        # for k in keys:
        #     if is_prime(int(k/i)):
        #         magic.append(i)


        for k in keys:
            if k%i == 0:
                if is_prime(int(k/i)):
                    magic.append(i)
    return max(magic)

def decrypt(encrypt_data, keys, magic):
    keys_sum = 0
    for k in keys:
        keys_sum += k/magic

    original_data = encrypt_data - keys_sum

    return original_data





#
#
# magic =  magic_prime(encrypt_data, keys)
# print magic
# print decrypt(encrypt_data, keys, magic)

