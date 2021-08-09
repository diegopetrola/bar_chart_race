import bar_chart_race as bcr
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
from utils.hist import get_style
# np.random.seed(19680801)

# mu_x = 200
# sigma_x = 25
# x = np.random.normal(mu_x, sigma_x, size=100)

# mu_w = 200
# sigma_w = 10
# w = np.random.normal(mu_w, sigma_w, size=100)

# fig, axs = plt.subplots(nrows=2, ncols=2)

# axs[0, 0].hist(x, 20, density=True, histtype='stepfilled', facecolor='g',
#                alpha=0.75)
# axs[0, 0].set_title('stepfilled')

# axs[0, 1].hist(x, 20, density=True, histtype='step', facecolor='g',
#                alpha=0.75)
# axs[0, 1].set_title('step')

# axs[1, 0].hist(x, density=True, histtype='barstacked', rwidth=0.8)
# axs[1, 0].hist(w, density=True, histtype='barstacked', rwidth=0.8)
# axs[1, 0].set_title('barstacked')

# # Create a histogram by providing the bin edges (unequally spaced).
# bins = [100, 150, 180, 195, 205, 220, 250, 300]
# axs[1, 1].hist(x, bins, density=True, histtype='bar', rwidth=0.8)
# axs[1, 1].set_title('bar, unequal bins')

# fig.tight_layout()

df = pd.read_csv('data.csv')
df.set_index('year', inplace=True)

bcr.bar_chart_race(
    df=df,
    filename='religion_chart_race.mp4',
    orientation='h',
    sort='desc',
    n_bars=8,
    fixed_order=False,
    fixed_max=True,
    steps_per_period=10,
    interpolate_period=True,
    bar_size=.95,
    # period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center'},
    # period_fmt='Year: {x:.0f}',
    period_template='Year: {x:.0f}',
    img_label_folder='imgs',
    # period_summary_func=lambda v, r: {'x': .99, 'y': .18,
    #                                   's': f'Year: ',
    #                                   'ha': 'right', 'size': 8, 'family': 'Courier New'},
    # perpendicular_bar_func='median',
    period_length=500,
    title={
        'label': 'Religion Adepts Worldwide',
    },
    scale='linear',
    writer=None,
    # fig=None,
    bar_kwargs={'alpha': .7},
    filter_column_colors=True,
    fig_kwargs={
        "figsize": (5, 3),
        "dpi": 144,
    })
