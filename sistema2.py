import textwrap

def menu():
    menu = """\n
    =================== MENU ==================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair

    ====> """

    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):# argumentos passados por posição, todos os dados que estão antes da barra /, devem ser passados apenas por posição
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\t R$ {valor:.2f}\n"
        print("\n ==== Depósito realizado com sucesso! ====")
    else:
        print("\n°°°° Operação falhou! O valor informado é inválido. °°°°")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):# os argumentos passados passados nessa função, devem ser somente passados por keyword depois do *, mostrado nos parametros da função.
    excedeuu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeuu_saldo:
        print("\n °°° Operação falhou! Você não tem saldo suficiente.°°°")
    elif excedeu_limite:
        print("\n °°° Operação falhou! O valor do saque excede o limite diário.°°°")
    elif excedeu_saques:
        print("\n°°°Operação falhou! Número máximo de saques atingido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n === Saque realizado com sucesso! ===")
    else:
        print("\n °°°Operação falhou! O valor informado é inválido!°°°")
    return saldo, extrato

def exibir_extrato(saldo, / , * , extrato): # até a barra os argumentos devem ser passados por posição, depois da / os argumentos devem ser passados por KeyWord
    print("\n ============== Extrato ==============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: \t\tR$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuarios(cpf,usuarios)

    if usuario:
        print("\n°°° Já existe usuário com esse CPF!")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento":data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário cadastrado com sucesso! ===")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n === Conta criada com sucesso! ===")
        return {"agencia":agencia, "numero_conta": numero_conta, "usuario":usuario}
    
    print("\n°°°Usuário não encontrado! Encerrando sessão!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            C/C?\t\t{conta['numero_conta']}
            Titular/\t{conta['usuario']['nome']}
        """
        print("=" * 1000)
        print(textwrap.dedent(linha))
    
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1
        elif opcao == "lc":
            listar_contas(contas)


main()