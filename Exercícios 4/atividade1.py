for i in range (1,3):
    while True:
        login = input("Informe o nome de usuário número {}: ".format(i))
        senha = input("\nInforme a senha do usuário {} (lembrando que não pode ser igual ao nome de usuário): ".format(i))
        
        if(login == senha):
            print("o nome de usuário e a senha são iguais\nPor favor digite uma senha diferente: ")
        
        else:
            print("Cadastro aceito")    
            
            break
    
    i = i + 1   

print("\n\nCadastros efetuados com sucesso!")