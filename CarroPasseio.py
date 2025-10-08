# ============================================
# Subclasse: CarroPasseio
# ============================================

from Veiculo import Veiculo

class CarroPasseio(Veiculo):
    def __init__(self, marca, modelo, ano_fabricacao, chassi, cor, quilometragem, numero_portas, tipo_combustivel):
        super().__init__(marca, modelo, ano_fabricacao, chassi, cor, quilometragem)
        self._numero_portas = numero_portas
        self._tipo_combustivel = tipo_combustivel

    def calcular_depreciacao(self, anos_uso, taxa_extra=0.05):
        """
        Depreciação simples com taxa extra anual.
        Fórmula: valor depreciado = anos_uso * taxa_extra * 100 (simulação)
        """
        depreciacao = anos_uso * taxa_extra * 100
        print(f"[DEPRECIAÇÃO] O carro {self._modelo} depreciou R${depreciacao:.2f} após {anos_uso} anos.")
        return depreciacao

    def exibir_informacoes(self, detalhado=False):
        super().exibir_informacoes(detalhado)
        if detalhado:
            print(f"Número de Portas: {self._numero_portas}")
            print(f"Tipo de Combustível: {self._tipo_combustivel}")
