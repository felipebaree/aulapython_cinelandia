for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    
    if num % 2 == 0:
        print(f"{num} é PAR")
    else:
        print(f"{num} é ÍMPAR")