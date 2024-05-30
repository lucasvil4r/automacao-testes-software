# test_estacionamento.py

import pytest
from datetime import datetime
from estacionamento import Estacionamento
from ticket import Ticket

@pytest.fixture
def estacionamento():
    return Estacionamento()

def test_emitir_ticket(estacionamento):
    # Given
    placa = "ABC-1234"
    modelo = "Sedan"
    
    # When
    ticket = Ticket(placa, modelo)
    estacionamento.emitir_ticket(ticket)
    
    # Then
    assert ticket in estacionamento.tickets_em_aberto

def test_calcular_valor_devido(estacionamento):
    # Given
    placa = "XYZ-5678"
    modelo = "SUV"
    entrada = datetime(2024, 5, 30, 14, 0)  # Entrada às 14:00
    
    # When
    ticket = Ticket(placa, modelo, entrada=entrada)
    estacionamento.registrar_saida(ticket)
    valor_devido = estacionamento.calcular_valor_devido(ticket)
    
    # Then
    assert valor_devido == 15  # R$ 15 para a primeira hora + R$ 5 para a segunda hora

if __name__ == "__main__":
    pytest.main()
