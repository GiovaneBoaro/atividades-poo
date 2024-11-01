class Autenticacao:
    def __init__(self):
        self.usuarios = {
            'user1': 'senha123',
            'user2': 'senha456'
        }
        self.usuario_logado = None  

    def login(self, username, senha):
        if username in self.usuarios and self.usuarios[username] == senha:
            self.usuario_logado = username
            print(f"Login bem-sucedido! Bem-vindo, {username}.")
            return True
        else:
            print("Falha no login! Usuário ou senha incorretos.")
            return False

    def logout(self):
        if self.usuario_logado:
            print(f"Logout bem-sucedido! Até logo, {self.usuario_logado}.")
            self.usuario_logado = None
        else:
            print("Nenhum usuário está logado.")

autenticacao = Autenticacao()
autenticacao.login('user1', 'senha123')  # Tenta fazer login com credenciais corretas
autenticacao.logout()                    # Faz o logout
autenticacao.login('user1', 'senhaErrada') # Tenta fazer login com senha incorreta