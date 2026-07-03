"""
Funções auxiliares de avaliação de modelos de classificação.

Extraído do notebook 01_eda.ipynb para evitar repetição do mesmo bloco
de avaliação (classification report + ROC-AUC + matriz de confusão)
para cada um dos três modelos treinados.
"""

import matplotlib.pyplot as plt
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_auc_score,
    ConfusionMatrixDisplay,
)


def avaliar_modelo(y_test, y_pred, y_proba, nome_modelo, numero_figura,
                    output_dir="../results/figures"):
    """
    Gera o classification report, calcula o ROC-AUC e plota/salva a
    matriz de confusão para um modelo de classificação binária.

    Parâmetros
    ----------
    y_test : array-like
        Valores reais da variável alvo (conjunto de teste).
    y_pred : array-like
        Valores previstos pelo modelo (classe 0 ou 1).
    y_proba : array-like
        Probabilidade prevista da classe positiva (classe 1).
    nome_modelo : str
        Nome do modelo, usado nos títulos e no nome do arquivo salvo.
    numero_figura : int or str
        Número usado para manter a numeração sequencial dos arquivos
        de figura salvos em results/figures/.
    output_dir : str
        Caminho para a pasta onde a figura da matriz de confusão será salva.

    Retorna
    -------
    roc_auc : float
        Valor do ROC-AUC calculado para o modelo.
    """
    print(f"Classification Report — {nome_modelo}")
    print(classification_report(
        y_test, y_pred, target_names=["Baixa/Média", "Alta"]
    ))

    roc_auc = roc_auc_score(y_test, y_proba)
    print(f"ROC-AUC: {roc_auc:.3f}")

    fig, ax = plt.subplots(figsize=(6, 5))
    cm = confusion_matrix(y_test, y_pred)
    ConfusionMatrixDisplay(cm, display_labels=["Baixa/Média", "Alta"]).plot(
        cmap="Reds", ax=ax, colorbar=False
    )
    ax.set_title(f"Matriz de Confusão — {nome_modelo}")
    plt.tight_layout()

    slug = nome_modelo.lower().replace(" ", "_")
    plt.savefig(f"{output_dir}/{numero_figura}_confusion_matrix_{slug}.png", dpi=300)
    plt.show()

    return roc_auc
