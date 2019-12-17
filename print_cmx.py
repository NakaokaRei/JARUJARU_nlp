import pandas as pd
import seaborn as sns
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np

def print_cmx(y_true, y_pred, label):
    labels = sorted(list(set(y_true)))
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    df_cmx = pd.DataFrame(cm, index=label, columns=label)
    
    plt.figure(figsize = (10,10))
    plt.rcParams["font.size"] = 30
    sns.heatmap(df_cmx, annot=True,square = True, cmap='Blues', fmt='.2f',
               cbar=False, annot_kws={'size': 35})
    plt.savefig('fig/cmx.png')
    plt.show()