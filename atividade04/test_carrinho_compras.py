import pytest
from pytest_bdd import scenarios, given, when, then
from carrinho_compras import CarrinhoCompras

scenarios('carrinho.feature')

@pytest.fixture
def carrinho():
    return CarrinhoCompras()

@given('que tenho um carrinho de compras com o item "Camiseta" e preço R$ 29.99')
def item_camiseta(carrinho):
    carrinho.adicionar_item('Camiseta', 29.99)

@when('eu adiciono o item "Calça" com o preço R$ 49.99')
def item_calca(carrinho):
    carrinho.adicionar_item('Calça', 49.99)

@then('o total do carrinho de compras deve ser R$ 79.98')
def verifica_total(carrinho):
    assert carrinho.total() == 79.98

@when('eu removo o item do carrinho')
def remove_item(carrinho):
    carrinho.remover_item()

@then('o carrinho de compras deve estar vazio')
def verifica_vazio(carrinho):
    assert carrinho.esta_vazio()
