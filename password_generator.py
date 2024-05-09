import random
import string

def gerar_senha(tam_senha):
    '''
    Realiza o tratamento para gerar a senha.
    Parameters
    ----------
    tam_senha : int
        Tamanho da senha a ser gerada
    
    Returns
    -------
    string
        Senha gerada
    '''
    if tam_senha < 4:
        return print(f'O tamanho da senha deve ser maior que 4 digitos, tente novamente.')    
    else:
        # Obter uma lista de caracteres válidos para a senha
        caracteres_senha = string.ascii_letters + string.digits + string.punctuation
         # Escolher caracteres aleatórios para formar a senha
        senha = ''.join(random.choices(caracteres_senha, k=tam_senha))
        return senha
        
        
def main():
    tam_senha = int(input('Digite o comprimento da senha:'))
    print(gerar_senha(tam_senha))

if __name__ == '__main__':
    main()
