class CarrinhoCompras:
    def __init__(self):
        self._itens = []

    def adicionar_item(self, item, preco):
        self._itens.append({'item': item, 'preco': preco})

    def remover_item(self):
        if self._itens:
            self._itens.pop() 

    def total(self):
        return sum(item['preco'] for item in self._itens)
    
    def esta_vazio(self):
        return len(self._itens) == 0
    