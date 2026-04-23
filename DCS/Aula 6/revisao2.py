# 2. Crie um programa que pede um login e senha. Se o login informado for 'admin' e a senha for 'pass' mostre na tela "Acesso Concedido: {True/False}

login = input("Digite seu Login: ")
senha = input("Digite sua Senha: ")

verif1 = login == "admin" and senha == "pass"

print(f"Acesso concedido: {verif1}")