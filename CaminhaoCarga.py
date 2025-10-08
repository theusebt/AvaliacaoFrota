# ============================================
# Subclasse: CaminhaoCarga
# ============================================

from Veiculo import Veiculo

class CaminhaoCarga(Veiculo):
    def __init__(self, marca, modelo, ano_fabricacao, chassi, cor, quilometragem, capacidade_toneladas, eixos):
        super().__init__(marca, modelo, ano_fabricacao, chassi, cor, quilometragem)
        self._capacidade_toneladas = capacidade_toneladas
        self._eixos = eixos

    def registrar_vistoria(self, motivo, multa=0):
        print(f"[VISTORIA] Caminhão {self._modelo}: Motivo - {motivo}. Multa: R${multa:.2f}")

    def exibir_informacoes(self, detalhado=False):
        super().exibir_informacoes(detalhado)
        if detalhado:
            print(f"Capacidade: {self._capacidade_toneladas} toneladas")
            print(f"Eixos: {self._eixos}")
