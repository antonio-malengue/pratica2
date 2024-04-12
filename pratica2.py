# Função principal
def main():
    # Solicita a data ao usuário
    data = input("Digite uma data no formato 'dd/mm/aaaa': ")

    # Separa a data em dia, mês e ano utilizando o método split() e o caractere '/'
    dia, mes, ano = data.split("/")

    # Converte as partes da data de string para inteiro
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)

    # Exibe as partes da data separadamente
    print("Dia:", dia)
    print("Mês:", mes)
    print("Ano:", ano)

# Chamada da função principal
if __name__ == "__main__":
    main()