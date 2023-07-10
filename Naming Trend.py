import pandas as pd
import matplotlib.pyplot as plt

names1880 = pd.read_csv('/Users/caiyilun/Desktop/mini #4/US-Popular-Baby-Names-Trend-Analysis-using-Python/names/yob1880.txt', names=['name', 'sex', 'births'])
names1880.groupby('sex').births.sum()

years = range(1880, 2019)
pieces = []
columns = ['name', 'sex', 'births']
for year in years:
path = '/Users/caiyilun/Desktop/mini #4/US-Popular-Baby-Names-Trend-Analysis-using-Python/names/yob%d.txt' % year
frame = pd.read_csv(path, names=columns)
frame['year'] = year
pieces.append(frame)

names = pd.concat(pieces, ignore_index=True)

total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)
total_births.plot(title='Total births by sex and year')

def add_prop(group):
group['prop'] = group.births / group.births.sum()
return group

names = names.groupby(['year', 'sex']).apply(add_prop)

def get_top1000(group):
return group.sort_values(by='births', ascending=False)[:1000]

grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)
top1000.reset_index(inplace=True, drop=True)

boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']
total_births = top1000.pivot_table('births', index='year', columns='name', aggfunc=sum)

subset = total_births[['John', 'Noah', 'Mary', 'Emma']]
subset.plot(subplots=True, figsize=(12, 10), grid=False, title='A few boy and girl names over time')
