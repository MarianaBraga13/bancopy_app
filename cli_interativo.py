def escolher_transacao(usuario):
    while True:
        print("\n================== 🏦 BANCO PY ==================")
        resposta = input(
            "Escolha uma opção:\n"
            "1️⃣  Depositar 💰\n"
            "2️⃣  Transferir 💸\n"
            "3️⃣  Empréstimo 💵\n"
            "4️⃣  Solicitar Cartão de Crédito 💳\n"
            "5️⃣  Pagar Conta 🧾\n"
            "6️⃣  Gerar Extrato 📄\n"
            "7️⃣  Sair com Saldo Final 🚪\n"
            "8️⃣  Ver Dashboard 📊\n"
            "9️⃣  Análise de Crédito 🧠\n"
            "👉 "
            )    

        if resposta.isdigit():
            resposta = int(resposta)
            if 1 <= resposta <= 9:
                if resposta == 1:
                    valor_str = input("Digite um valor para depósito: R$ ")
                    try:
                        valor = float(valor_str)
                        deposito = usuario.depositar(valor)
                        if deposito:
                            print("Depósito recebido com sucesso!\nDeseja realizar alguma outra transação?\n")
                        resposta = input("Digite 'S' para 'SAIR' ou QUALQUER tecla para CONTINUAR: ")
                        if resposta.upper() == "S":
                            break
                        else:
                            continue
                    except ValueError:
                        print("Digite um número válido.")

                elif resposta == 2:
                    valor_str = input("Digite um valor para transferência: R$ ")
                    try:
                        valor = float(valor_str)
                        transferencia = usuario.transferir(valor)
                        if transferencia:
                            print("\nDeseja realizar alguma outra transação?\n")
                        resposta = input("Digite 'S' para 'SAIR' ou QUALQUER tecla para CONTINUAR: ")
                        if resposta.upper() == "S":
                            break
                        else:
                            continue
                    except ValueError:
                        print("Digite um número válido.")

                elif resposta == 3:
                    try:
                        limite_emprestimo = usuario.analisar_credito()
                        if limite_emprestimo:
                            print(f"✅ Seu limite para empréstimo : R$ {usuario.limite_emprestimo:.2f}")
                            valor_str = input("Digite um valor que deseja emprestar: R$ ")
                            valor = float(valor_str)
                            emprestimo = usuario.emprestar(valor)
                            if emprestimo:
                                print(f"✅ Empréstimo no valor de R$ {valor:.2f} realizado com sucesso!")
                                resposta = input("Digite 'S' para 'SAIR' ou QUALQUER tecla para CONTINUAR: ")
                                if resposta.upper() == "S":
                                    break
                    except ValueError:
                        print("❌ Valor inválido ou crédito insuficiente.\nCaso ainda não tenha acesso ao serviço, solicite uma análise de crédito.\n")

                elif resposta == 4:
                    usuario.solicitar_cartao()
                elif resposta == 5:
                    valor_str = input("Digite o valor que deseja pagar: R$ ")
                    try:
                        valor = float(valor_str)
                        pagamento = usuario.pagar_conta(valor)
                        if pagamento:
                            print("\nDeseja realizar alguma outra transação?\n")
                        resposta = input("Digite 'S' para 'SAIR' ou QUALQUER tecla para CONTINUAR: ")
                        if resposta.upper() == "S":
                            break
                        else:
                            continue
                    except ValueError:
                        print("Digite um número válido.")
                elif resposta == 6:
                    usuario.mostrar_extrato()
                elif resposta == 7:
                    print("\n================= SALDO FINAL 📄 =================\n")
                    print(f"Saldo final no Banco Py: R${usuario.patrimonio:.2f}")
                    print("Agradecemos sua preferência em contar com os serviços financeiros do nosso Banco Py!\n 👋 Até breve!")
                    break
                elif resposta == 8:
                    usuario.exibir_dashboard()
                elif resposta == 9:
                    usuario.analisar_credito()
            else:
                print("Digite uma opção válida.")    
        else:
            print("Digite um número.")            
    