import bar_chart_race as bcr
import pandas as pd

columns = 'chrstprot,chrstcat,chrstorth,chrstang,chrstothr,chrstgen,judorth,jdcons,judref,judothr,judgen,islmsun,islmshi,islmibd,islmnat,islmalw,islmahm,islmothr,islmgen,budmah,budthr,budothr,budgen,zorogen,hindgen,sikhgen,shntgen,bahgen,taogen,jaingen,confgen,syncgen,anmgen,nonrelig,othrgen'
columns = columns.split(',')

df = pd.read_csv('WRP_global.csv', thousands=',')
df = df[columns]

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
    label_bars=True,
    bar_size=.95,
    period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center'},
    period_fmt='%B %d, %Y',
    period_summary_func=lambda v, r: {'x': .99, 'y': .18,
                                      's': f'Total: no idea',
                                      'ha': 'right', 'size': 8, 'family': 'Courier New'},
    # perpendicular_bar_func='median',
    period_length=500,
    figsize=(5, 3),
    dpi=144,
    cmap='dark12',
    title='Religion Adepts Worldwide',
    title_size='',
    bar_label_size=7,
    tick_label_size=7,
    shared_fontdict={'family': 'Helvetica', 'color': '.1'},
    scale='linear',
    writer=None,
    fig=None,
    bar_kwargs={'alpha': .7},
    filter_column_colors=False)
