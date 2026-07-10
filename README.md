# 🍷 Wine Quality Classification

Projeto de machine learning para classificação binária da qualidade de vinhos tintos
com base em suas características físico-químicas.

A variável alvo foi transformada em classificação binária:
- **Alta Qualidade:** nota ≥ 7
- **Baixa/Média Qualidade:** nota < 7

O objetivo é treinar e avaliar modelos capazes de prever essa classificação
a partir de variáveis como teor alcoólico, acidez volátil, sulfatos, entre outras.

> **Dataset:** [Wine Quality Dataset — Kaggle](https://www.kaggle.com/datasets/yasserh/wine-quality-dataset)

## 📁 Estrutura do Repositório

```
wine-quality-classification/
│
├── data/               # Dataset utilizado (WineQT.csv)
├── notebooks/          # Notebook principal com EDA e modelagem
├── src/                # Scripts auxiliares de pré-processamento e modelagem
├── results/
│   ├── figures/        # Gráficos gerados durante a análise
│   └── metrics/        # Métricas de avaliação dos modelos
├── requirements.txt    # Dependências do projeto
└── README.md           # Descrição do projeto
```

## 🛠️ Bibliotecas Utilizadas

| Biblioteca | Finalidade |
|---|---|
| `pandas` | Manipulação e análise de dados |
| `numpy` | Operações matemáticas |
| `matplotlib` / `seaborn` | Visualização de dados |
| `scikit-learn` | Pré-processamento e modelagem |
| `imbalanced-learn` | Tratamento do desbalanceamento de classes |
| `xgboost` | Modelo Gradient Boosting |
| `jupyter` | Ambiente de notebook |

## 📊 Resultados

Três modelos de classificação foram treinados e avaliados: Regressão Logística
(baseline), Random Forest e XGBoost. Dado o desbalanceamento de classes
identificado na EDA (86% Baixa/Média, 14% Alta Qualidade), a comparação
prioriza F1-Score e ROC-AUC na classe minoritária.

| Modelo | Precision (Alta) | Recall (Alta) | F1-Score (Alta) | ROC-AUC |
|---|---|---|---|---|
| Regressão Logística | 0.38 | 0.69 | 0.49 | 0.850 |
| Random Forest | 0.76 | 0.50 | 0.60 | 0.905 |
| **XGBoost** | **0.61** | **0.69** | **0.65** | **0.919** |

**Melhor modelo:** XGBoost, por apresentar o melhor equilíbrio entre Precision
e Recall na classe Alta Qualidade, além do maior ROC-AUC entre os três.

**Variáveis mais influentes:** `alcohol`, `sulphates` e `citric acid` —
resultado consistente entre a correlação de Pearson, a separação visual por
classe na EDA e a importância de features extraída do XGBoost.

Gráficos completos disponíveis em [`results/figures/`](./results/figures/).

## 📚 Fontes Consultadas — Implicações para Produção

A discussão de implicações para o processo de produção foi fundamentada nas seguintes fontes de domínio do vinho:

**Teor alcoólico (`alcohol`):**
- Evino. *Teor alcoólico no vinho (ABV): como ele define corpo, equilíbrio e sabor.*
  https://www.evino.com.br/blog/teor-alcoolico-vinho-abv/

**Sulfatos (`sulphates`):**
- DiVinho. *Sulfitos no Vinho - O que Devo Saber?*
  https://www.divinho.com.br/blog/sulfitos-no-vinho/
- Eno Cultura. *Enxofre no vinho.*
  https://www.enocultura.com.br/enxofre-no-vinho/

**Ácido cítrico (`citric acid`):**
- Ciência do Leite. *Aplicações do ácido cítrico na indústria de alimentos.*
  https://cienciadoleite.com.br/noticia/6141/aplicacoes-do-acido-citrico-na-industria-de-alimentos
- Wikipédia. *Ácidos no vinho.*
  https://pt.wikipedia.org/wiki/%C3%81cidos_no_vinho

**Acidez e pH (validação metodológica na EDA):**
- Wine Fun. *Acidificação do vinho: conheça mais sobre as diversas técnicas disponíveis.*
  https://winefun.com.br/acidificacao-do-vinho-conheca-mais-sobre-as-diversas-tecnicas-disponiveis/

**Limites legais de SO₂ (referenciado na análise de outliers do notebook):**
- OIV — International Code of Oenological Practices.

## 🎥 Vídeo Executivo

Apresentação executiva do projeto.

▶️ [Assistir a apresentação](https://www.youtube.com/watch?v=VR6ipK6yYSw)

## 👤 Autor

Gabriel da Silva Brandão Nascimento [RM374018] — Pós-Tech em Data Analytics FIAP 2026.