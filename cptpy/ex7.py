usuario_cadastrado = input("Cadastre seu usuário: ")
senha_cadastrada = input("Cadastre sua senha: ")

usuario = input("Digite seu usuário: ")

while usuario != usuario_cadastrado:
    print("Usuário incorreto!")
    usuario = input("Digite seu usuário novamente: ")

senha = input("Digite sua senha: ")

while senha != senha_cadastrada:
    print("Senha incorreta!")
    senha = input("Digite sua senha novamente: ")

print("Login realizado com sucesso!")