import openpyxl
from wordcloud import WordCloud

bg = openpyxl.load_workbook('../data.xlsx')
sheel = bg['国内疫情实时数据']
frequency = {}
for row in sheel.values:
    if row[0] == '省份':
        pass
    else:
        frequency[row[0]] = float(row[1])
wordcloud = WordCloud(font_path="C:/Windows/Fonts/SIMLI.TTF",background_color="white",width=1920, height=1080)
wordcloud.generate_from_frequencies(frequency)
wordcloud.to_file('../citywordcloude.png')
