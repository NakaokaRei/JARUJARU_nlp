import pandas as pd
import seaborn as sns
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np

def print_cmx(y_true, y_pred):
    labels = labels = sorted(list(set(y_true)))
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    df_cmx = pd.DataFrame(cm, index=labels, columns=labels)
    
    plt.figure(figsize = (10,7))
    sns.heatmap(df_cmx, annot=True)
    plt.show()