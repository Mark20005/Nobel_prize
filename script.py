# Loading in required libraries
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Start coding here!

nb = pd.read_csv('nobel.csv')
top_gender = nb['sex'].value_counts().sort_values(ascending=False).index[0]

top_country = nb['birth_country'].value_counts().sort_values(ascending=False).index[0]
nb['US_winners'] = nb['birth_country'] == 'United States of America'
nb['decade'] = (np.floor(nb['year'] / 10) * 10).astype(int)
decade_win = nb.groupby('decade', as_index=False)['US_winners'].mean()
max_decade_usa = decade_win[decade_win['US_winners'] == decade_win['US_winners'].max()]['decade'].values[0]

sns.relplot(x='decade', y='US_winners', data=decade_win, kind='line')
plt.show()

nb['fems'] = nb['sex'] == "Female"
fems_win = nb.groupby(['decade', 'category'], as_index=False)['fems'].mean()
max_female_row = fems_win[fems_win['fems'] == fems_win['fems'].max()][['decade', 'category']]
max_female_dict = {max_female_row['decade'].values[0]: max_female_row['category'].values[0]}
sns.set_context('talk')
sns.relplot(x='decade', y='fems',col='category', data=fems_win, kind='line')
plt.show()

first_fem = nb[nb['fems']].sort_values('year')
sort_first_fem = first_fem[first_fem['year'] == first_fem['year'].min()]
first_woman_name = sort_first_fem['full_name'].values[0]
first_woman_category = sort_first_fem['category'].values[0]
big_one = nb.value_counts('full_name')
repeat_list = list(big_one[big_one > 1].index)