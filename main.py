#Problema 1
def get_largest_prime_below(n):
    cel_mai_mare_div_prim = 0
    for d in range(2,n):
        nrdiv = 0
        for i in range(2,d//2):
            if d % i == 0:
                nrdiv = nrdiv + 1
        if nrdiv == 0:
            cel_mai_mare_div_prim = d
    return cel_mai_mare_div_prim

def test_get_largest_prime_below():
    n = int(input("introduceti numarul n = "))
    print(get_largest_prime_below(n))


#Problema 5
def is_palindrome(n) -> bool:
    aux = n
    x = 0
    while aux:
        x = x * 10 + aux % 10
        aux = aux // 10
    if x == n:
        return True
    else:
        return False


def test_is_palindrome():
    n = int(input("n = "))
    print(is_palindrome(n))


#Problema 6
def is_superprime(n) -> bool:
    while n:
        nrdiv = 0
        for i in range(2,n):
            if(n % i == 0):
                nrdiv = nrdiv + 1
            if(nrdiv):
                return False
        n = n // 10
    return True

def test_is_superprime():
    n = int(input("n = "))
    print(is_superprime(n))


def main():
    a=int(input("Problema:"))
    if(a==1):
    #largest prime below
        test_get_largest_prime_below()
    if(a==5):
    #is palindrome
        test_is_palindrome()
    if(a==6):
    #is superprime
        test_is_superprime()


if __name__ == '__main__':
    main()