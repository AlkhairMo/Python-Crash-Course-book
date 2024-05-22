news = ['alhadath', 'aljazira', 'bbc', 'alarabia', 'sky news']
print(news)
news[2] = 'frensh 24'
print(news)
news.append('bbc')
print(news)
news.insert(0, 'al hadath')
print(news)
del news[1]
print(news)
skynews = news.pop()
print(news)
print(f'I do not watch {skynews.title()}.')
alarabia = 'alarabia'
news.remove(alarabia)
print(news)
print(f'{alarabia.title()} is programs channel mor than news one')
news.reverse()
print(news)
news.sort()
print(news)
print('Revers final sort of channels:')
print(sorted(news, reverse=True))
print('Final number of channels=', len(news))