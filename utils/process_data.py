import bar_chart_race as bcr
import pandas as pd

if __name__ == "__main__":
    """
    Script used to process the raw data and write a 'data.csv'
    which will avoid reprocessing in the future
    """
    # cols = 'chrstprot,chrstcat,chrstorth,chrstang,chrstothr,chrstgen,judorth,jdcons,judref,judothr,judgen,islmsun,islmshi,islmibd,islmnat,islmalw,islmahm,islmothr,,budmah,budthr,budothr,,,,,,,,,,,,,'
    cols = "year,chrstgen,judgen,islmgen,budgen,zorogen,hindgen,sikhgen,shntgen,bahgen,taogen,jaingen,confgen,syncgen,anmgen,nonrelig,othrgen"
    cols = cols.split(',')
    new_labels = {
        "chrstgen": "Christianity",
        "judgen": "Judaism",
        "islmgen": "Islam",
        "budgen": "Budhism",
        "zorogen": "Zoroastrian",
        "hindgen": "Hindu",
        "sikhgen": "Sikh",
        "shntgen": "Shinto",
        "bahgen": "Baha'i",
        "taogen": "Taoism",
        "jaingen": "Confucianism",
        "confgen": "Jain",
        "syncgen": "Syncretic Religions",
        "anmgen": "Animist Religions",
        "nonrelig": "Non. Religious",
        "othrgen": "Other Religions",
    }

    df = pd.read_csv('WRP_global.csv', thousands=',')
    df = df[cols]
    df.set_index('year', inplace=True)
    df.rename(columns=new_labels, inplace=True)
    df.to_csv('data.csv')
