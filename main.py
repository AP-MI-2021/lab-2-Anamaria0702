#Problema 1
def get_largest_prime_below(n):
    #returneaza cel mai mare numar prim mai mic decat un numar dat
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
    assert get_largest_prime_below(15) == 13
    assert get_largest_prime_below(25) == 23


#Problema 5
def is_palindrome(n) -> bool:
    #verifica daca un numar este palindrom
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
    assert is_palindrome(1221) == True
    assert is_palindrome(345) == False

#Problema 6
def is_superprime(n) -> bool:
    #verifica daca un numar este superprim sau nu
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
    assert is_superprime(237) == False
    assert is_superprime(233) == True

def main():
    a=int(input("Problema:"))
    if(a==1):
    #largest prime below
        n = int(input("introduceti numarul n = "))
        print(get_largest_prime_below(n))
    if(a==5):
    #is palindrome
        n = int(input("n = "))
        print(is_palindrome(n))
    if(a==6):
    #is superprime
        n = int(input("n = "))
        print(is_superprime(n))


if __name__ == '__main__':
    main()