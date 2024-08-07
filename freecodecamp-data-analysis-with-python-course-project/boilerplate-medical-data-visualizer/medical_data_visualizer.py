import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('sample_data/medical_examination.csv')

# 2
df['overweight'] = np.where((df['weight'] / ((df['height'] / 100) ** 2)) > 25, 1, 0).astype(int)

# 3
df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1).astype(int)
df['gluc'] = np.where(df['gluc'] == 1, 0, 1).astype(int)

#

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])


    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index()
    df_cat.rename(columns={0: 'total'}, inplace=True)

    # 7
    graph = sns.catplot(data=df_cat, kind='bar', x='variable', y='total', hue='value', col='cardio')


    # 8
    fig = graph.fig


    # 9
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi'])
        & (df['height'] >= df['height'].quantile(0.025))
        & (df['height'] <= df['height'].quantile(0.975))
        & (df['weight'] >= df['weight'].quantile(0.025))
        & (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()
    

    # 13
    mask = np.triu(corr)



    # 14
    fig, ax = plt.subplots(figsize=(16, 9))

    # 15
    sns.heatmap(corr, linewidths=1, annot=True, square=True, mask=mask, fmt='.1f')


    # 16
    fig.savefig('heatmap.png')
    return fig