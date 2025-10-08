# 🧭 Sistema de Gerenciamento de Frota de Veículos

### 📅 Data
08 de Outubro de 2025  
👨‍💻 Autor: [Seu Nome]

---

## 💡 Conceitos de POO Utilizados

### 🏗️ 1. **Classe e Objeto**
- `Veiculo`, `CarroPasseio` e `CaminhaoCarga` são classes.
- Cada instância criada em `main.py` é um **objeto** dessas classes.

---

### 🔒 2. **Encapsulamento**
- Os atributos são **protegidos** (prefixo `_`) e acessados por meio de **propriedades (`@property`)**.
- Isso evita acesso direto indevido aos dados internos.

---

### 🧬 3. **Herança**
- `CarroPasseio` e `CaminhaoCarga` **herdam** de `Veiculo`.
- Reaproveitam métodos (`exibir_informacoes`, `registrar_manutencao`) e **adicionam comportamentos específicos**.

---

### 🔁 4. **Polimorfismo**
- O método `exibir_informacoes()` é **sobrescrito** nas subclasses, exibindo dados diferentes dependendo do tipo de veículo.

---

### ⚙️ 5. **Abstração**
- A classe `Veiculo` representa o conceito genérico de um veículo, enquanto as subclasses representam tipos concretos.

---

## 🚀 **Fluxo de Execução (main.py)**

1. Criação de um **CarroPasseio** e exibição de informações.
2. Registro de uma **manutenção** e cálculo de **depreciação**.
3. Criação de um **CaminhaoCarga** e exibição detalhada.
4. Registro de **vistoria** e **manutenção**.

---

## 📂 Estrutura de Pastas

