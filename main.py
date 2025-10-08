# ============================================
# Sistema de Gerenciamento de Frota de Veículos
# Autor: [Seu Nome]
# Data: 2025-10-08
# ============================================

from CarroPasseio import CarroPasseio
from CaminhaoCarga import CaminhaoCarga

if __name__ == "__main__":
    print("\n🚗 --- Cadastro de Carro de Passeio ---")
    carro = CarroPasseio("Toyota", "Corolla", 2020, "CHS1234", "Prata", 45000, 4, "Gasolina")
    carro.exibir_informacoes(detalhado=False)
    carro.exibir_informacoes(detalhado=True)
    carro.registrar_manutencao("Troca de óleo", 250)
    carro.calcular_depreciacao(5, taxa_extra=0.07)

    print("\n🚚 --- Cadastro de Caminhão de Carga ---")
    caminhao = CaminhaoCarga("Volvo", "FH 540", 2018, "CHS9876", "Branco", 220000, 30, 6)
    caminhao.exibir_informacoes(detalhado=False)
    caminhao.exibir_informacoes(detalhado=True)
    caminhao.registrar_manutencao("Revisão geral", 1800)
    caminhao.registrar_vistoria("Verificação de pneus", 0)

