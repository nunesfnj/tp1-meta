# 🧠 Meta-heurísticas para Otimização

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Status](https://img.shields.io/badge/status-concluído-success.svg)
![License](https://img.shields.io/badge/license-academic-lightgrey.svg)

---

## 📌 Descrição

Este projeto tem como objetivo a implementação e análise de algoritmos de meta-heurísticas aplicados à minimização de funções matemáticas não lineares.

Foram desenvolvidos e comparados dois algoritmos:

- 🔹 Busca Tabu (Tabu Search)
- 🔹 Simulated Annealing (Recozimento Simulado)

Os algoritmos foram aplicados em problemas de otimização contínua com duas variáveis de decisão (x1, x2), sob diferentes intervalos.

---

## 🎯 Objetivos

- Implementar algoritmos meta-heurísticos clássicos  
- Resolver problemas de otimização contínua  
- Comparar desempenho entre métodos  
- Analisar resultados estatísticos  

---

## 🧮 Funções Objetivo

### 🔹 Função 1
Função não linear envolvendo raiz quadrada e valor absoluto.

### 🔹 Função 2
Função multimodal baseada em seno, com parâmetro m = 10, que aumenta a complexidade da busca.

---

## ⚙️ Metodologia

Para cada função e intervalo:

- 🔁 30 execuções independentes  
- 📊 Coleta de métricas:
  - Valor mínimo  
  - Valor máximo  
  - Média  
  - Desvio padrão  
- 📦 Geração de boxplots  
- 🏆 Registro da melhor solução encontrada  

---

## 📊 Resultados

Os resultados incluem:

- Comparação entre Busca Tabu e Simulated Annealing  
- Análise estatística das execuções  
- Visualizações gráficas  
- Identificação das melhores soluções  

---

## 🛠️ Tecnologias Utilizadas

- Python 3  
- NumPy  
- Matplotlib  

---

## 📁 Estrutura do Projeto
tp_metaheuristicas

├── busca_tabu.py

├── simulated_annealing.py

└── main.py


---

## ▶️ Como Executar

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
pip install numpy matplotlib
python main.py
