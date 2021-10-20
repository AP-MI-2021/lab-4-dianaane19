def neg(x):
    if (x != abs(x)):
        return True
    else:
        return False

def list_neg(list):
    rasp = []
    # for i in range(len(lista)):
    for el in list:
         if neg(el):
             rasp.append(el)
    return rasp

def is_prime(n):
  # codul vostru aici
  if (n==0 or n==1):
    return False
  for d in range(2, n//2):
    if (n%d==0):
      return False
    return True

def superprim(x):
    if (x > 0):
        while (x%10 != 0):
            if (is_prime(x) == True):
                x=x%10
    return False

def list_superprim(list):
    rasp = []
    # for i in range(len(lista)):
    for el in list:
         if superprim(el):
             rasp.append(el)
    return rasp



def show_menu():
    print('''
    1. Citire listă
    2. Afișarea numerelor negative din listă
    4. Afișarea numerelor superprime din listă
    0. Ieșire
    ''')

def read_list():
    list = []
    n = int(input("Introduceți numărul de elem din listă:"))
    for i in range(n):
        x = int(input("a[{}]=".format(i + 1)))
        list.append(x)
    return list

def run():
    list = []
    while True:
        show_menu()
        cmd = input("Comandă:")
        if cmd == '1':
            list = read_list()
        elif cmd == '2':
            rez1 = list_neg(list)
            print(rez1)
        elif cmd == '4':
            rez2 = list_superprim(list)
            print(rez2)
        elif cmd == '0':
            break
        else:
             print("Comandă invalidă")

run()
