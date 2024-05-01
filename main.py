import os


def calc():

    again = True


    while again:

        n1 = eval(input("Digite um número: "))
        n2 = eval(input("Digite outro número: "))
        resul = 0
        simbolo = ""

        while True:

            if simbolo not in ["+", "-", "*", "/"]:
                simbolo = input('''
Digite:
+ para somar
- para subtrair
* para multiplicar
/ para dividir
                    ''')
            else:
                break
            
            
        if simbolo == "+":
            resul = n1 + n2
            print(f'''
{n1} + {n2} = {resul}
                ''')
        elif simbolo == "-":
            resul = n1 - n2
            print(f'''
{n1} - {n2} = {resul}
                ''')
        elif simbolo == "*":
            resul = n1 * n2
            print(f'''
{n1} * {n2} = {resul}
                ''')
        elif simbolo == "/":
            resul = n1 / n2
            print(f'''
{n1} / {n2} = {resul}'''
                )


        calc_gain = input('''
Se quiser fazer outro cálculo
digite S para sim e N para não:
            ''').upper()
        
        if calc_gain == "S":
            lc()
            print('''
Cálculos novos...
                  ''')
            pass
        else:
            print("Cálculos finalizados.")
            break


def lc():

    if os.name == 'posix':  # para sistemas baseados em Unix (Linux/MacOS)
        os.system('clear')
    else:  # para Windows
        os.system('cls')


calc()


 



