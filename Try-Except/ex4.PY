class SenhaInvalidaError(Exception):
    pass

def verificar_senha(senha):
    if len(senha) < 8 or not any(char.isdigit() for char in senha):
        raise SenhaInvalidaError("A senha deve ter pelo menos 8 caracteres e conter ao menos um número.")

try:
    senha = input("Digite sua senha: ")
    verificar_senha(senha)
    print("Senha válida!")
except SenhaInvalidaError as e:
    print(f"Erro: {e}")