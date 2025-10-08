# ============================================
# Classe Base: Veiculo
# ============================================

class Veiculo:
    def __init__(self, marca, modelo, ano_fabricacao, chassi, cor, quilometragem):
        # Atributos encapsulados
        self._marca = marca
        self._modelo = modelo
        self._ano_fabricacao = ano_fabricacao
        self._chassi = chassi
        self._cor = cor
        self._quilometragem = quilometragem

    # ============================
    # Métodos da Superclasse
    # ============================
    def registrar_manutencao(self, tipo, custo):
        print(f"[MANUTENÇÃO] O veículo {self._modelo} ({tipo}) teve custo de R${custo:.2f}.")

    def exibir_informacoes(self, detalhado=False):
        if detalhado:
            print(f"--- Detalhes do Veículo ---")
            print(f"Marca: {self._marca}")
            print(f"Modelo: {self._modelo}")
            print(f"Ano de Fabricação: {self._ano_fabricacao}")
            print(f"Chassi: {self._chassi}")
            print(f"Cor: {self._cor}")
            print(f"Quilometragem: {self._quilometragem} km")
        else:
            print(f"{self._marca} {self._modelo} - {self._quilometragem} km")

    # Getters e Setters (Encapsulamento)
    @property
    def quilometragem(self):
        return self._quilometragem

    @quilometragem.setter
    def quilometragem(self, valor):
        if valor >= 0:
            self._quilometragem = valor
        else:
            print("Erro: quilometragem não pode ser negativa!")
