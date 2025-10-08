# AvaliacaoFrota
Nome do Aluno: Matheus Edson Barbosa Turso

🚗 Sistema de Gerenciamento de Frota de Veículos:
🧩 Descrição do Projeto

Este projeto tem como objetivo gerenciar uma frota de veículos (carros e caminhões), aplicando conceitos de Programação Orientada a Objetos (POO) em Python.
Ele simula um sistema que pode ser utilizado por empresas de transporte, locadoras ou organizações que precisem monitorar, registrar e analisar dados de veículos.

⚙️ Funcionalidades principais:

Cadastro de veículos (carros de passeio e caminhões de carga);

Registro de manutenção e vistoria;

Exibição de informações detalhadas ou resumidas;

Cálculo de depreciação com base no tempo de uso;

Aplicação de herança, polimorfismo e encapsulamento;


🧱 Explicação das Classes e Métodos:
🏗️ 1. Classe Base – Veiculo

Representa a estrutura genérica de qualquer veículo.
Outras classes (como CarroPasseio e CaminhaoCarga) herdam dela.

🔹 Atributos encapsulados:

_marca: marca do veículo

_modelo: modelo do veículo

_ano_fabricacao: ano de fabricação

_chassi: número de chassi

_cor: cor do veículo

_quilometragem: quilometragem atual

🔹 Métodos principais:

registrar_manutencao(tipo, custo)
Exibe uma mensagem simulando o registro de manutenção com o tipo e o custo.

exibir_informacoes(detalhado=False)
Mostra as informações do veículo. Se detalhado=True, exibe todos os dados do objeto.

Encapsulamento (Getters e Setters):

@property quilometragem: retorna a quilometragem atual.

@quilometragem.setter: atualiza a quilometragem, impedindo valores negativos.

🚘 2. Subclasse – CarroPasseio

Herdeira de Veiculo, representa veículos de passeio.

🔹 Atributos adicionais:

_numero_portas: número de portas do carro

_tipo_combustivel: tipo de combustível (gasolina, etanol, elétrico etc.)

🔹 Métodos específicos:

calcular_depreciacao(anos_uso, taxa_extra=0.05)
Calcula uma depreciação simbólica com base nos anos de uso e em uma taxa extra.
Fórmula:

valor depreciado = anos_uso * taxa_extra * 100

exibir_informacoes(detalhado=False)
Sobrescreve o método da superclasse, adicionando dados do carro (portas e combustível).

🧠 Conceitos aplicados:

Herança da classe Veiculo

Polimorfismo, pois redefine (override) o método exibir_informacoes

Encapsulamento ao proteger os atributos internos

🚚 3. Subclasse – CaminhaoCarga

Herdeira de Veiculo, representa veículos de transporte de carga.

🔹 Atributos adicionais:

_capacidade_toneladas: capacidade máxima de carga

_eixos: número de eixos do caminhão

🔹 Métodos específicos:

registrar_vistoria(motivo, multa=0)
Simula o registro de uma vistoria no caminhão, incluindo o motivo e o valor da multa (se houver).

exibir_informacoes(detalhado=False)
Sobrescreve o método da classe base, exibindo também a capacidade e o número de eixos.

🧠 4. Arquivo Principal – main.py

Responsável por executar o sistema e demonstrar o uso das classes.

🔹 Fluxo de execução:

Cria um objeto da classe CarroPasseio;

Exibe informações resumidas e detalhadas;

Registra uma manutenção;

Calcula a depreciação do carro;

Cria um objeto da classe CaminhaoCarga;

Exibe informações e registra vistoria e manutenção;


💻 Exemplos de Execução:
▶️ Exemplo 1 — Carro de Passeio
carro = CarroPasseio("Toyota", "Corolla", 2020, "CHS1234", "Prata", 45000, 4, "Gasolina")
carro.exibir_informacoes(detalhado=False)
carro.exibir_informacoes(detalhado=True)
carro.registrar_manutencao("Troca de óleo", 250)
carro.calcular_depreciacao(5, taxa_extra=0.07)

🧾 Saída esperada:
🚗 --- Cadastro de Carro de Passeio ---
Toyota Corolla - 45000 km
--- Detalhes do Veículo ---
Marca: Toyota
Modelo: Corolla
Ano de Fabricação: 2020
Chassi: CHS1234
Cor: Prata
Quilometragem: 45000 km
Número de Portas: 4
Tipo de Combustível: Gasolina
[MANUTENÇÃO] O veículo Corolla (Troca de óleo) teve custo de R$250.00.
[DEPRECIAÇÃO] O carro Corolla depreciou R$35.00 após 5 anos.

▶️ Exemplo 2 — Caminhão de Carga
caminhao = CaminhaoCarga("Volvo", "FH 540", 2018, "CHS9876", "Branco", 220000, 30, 6)
caminhao.exibir_informacoes(detalhado=False)
caminhao.exibir_informacoes(detalhado=True)
caminhao.registrar_manutencao("Revisão geral", 1800)
caminhao.registrar_vistoria("Verificação de pneus", 0)

🧾 Saída esperada:
🚚 --- Cadastro de Caminhão de Carga ---
Volvo FH 540 - 220000 km
--- Detalhes do Veículo ---
Marca: Volvo
Modelo: FH 540
Ano de Fabricação: 2018
Chassi: CHS9876
Cor: Branco
Quilometragem: 220000 km
Capacidade: 30 toneladas
Eixos: 6
[MANUTENÇÃO] O veículo FH 540 (Revisão geral) teve custo de R$1800.00.
[VISTORIA] Caminhão FH 540: Motivo - Verificação de pneus. Multa: R$0.00
