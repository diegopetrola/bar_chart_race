import bar_chart_race as bcr
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


plt.rcdefaults()
plt.rcParams.update({
    "xtick.major.size": 5,
    "xtick.major.pad": 7,
    "xtick.labelsize": 15,
    "grid.color": "0.5",
    "grid.linestyle": "-",
    "grid.linewidth": 5,
    "lines.linewidth": 2,
    "lines.color": "g",
})
fig: Figure = plt.figure()
fig.tight_layout()
ax: Axes = fig.add_subplot()
ax.set_xlabel('Number of Adherents (millions)')
ax.set_title('Religion Adherents Worldwide')
plt.grid(axis='x', which='both', linewidth=.4, zorder=1)
df = pd.read_csv('data.csv')
df.set_index('year', inplace=True)

bcr.bar_chart_race(
    df=df,
    filename='religion_chart_race.mp4',
    orientation='h',
    sort='desc',
    n_bars=10,
    fixed_order=False,
    fixed_max=True,
    steps_per_period=50,
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
    period_length=2500,
    title={
        'label': 'Religion Adherents Worldwide',
    },
    scale='linear',
    # writer='html',
    # fig=fig,
    bar_kwargs={'alpha': .85},
    filter_column_colors=True,
    fig_kwargs={
        "figsize": (8, 5),
        "dpi": 320,
    }
)
