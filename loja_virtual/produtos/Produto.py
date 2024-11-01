class Produto:
    def __init__(self, nome, preco, estoque):
        self._nome = nome       # Atributo "privado"
        self._preco = preco     # Atributo "privado"
        self._estoque = estoque # Atributo "privado"

    # Mostrar as informações do produto
    def mostrar_informacoes(self):
        print(f"Produto: {self._nome}, Preço: {self._preco}, Estoque: {self._estoque}")

# Exemplo
produto = Produto("Camiseta", 29.99, 100)
produto.mostrar_informacoes()

# Acessar diretamente os atributos
produto._preco = 34.99  # Modifica o preço diretamente
produto.mostrar_informacoes()

