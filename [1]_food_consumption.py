import pandas as pd

FNAME = 'food_consumption.csv'

df = pd.read_csv(FNAME)

# a. How many different food categories appear in the dataset?
num_food_cat = df['food_category'].nunique()
print(f'The dataset contains: {num_food_cat} food categories.\n')

# b. Return a list of the food categories appearing in the dataset.
food_cat = df['food_category'].unique()
print(f'Food categories: {food_cat}\n')

# c. How many countries are in the dataset?
num_countries = df['country'].nunique()
print(f'The dataset contains: {num_countries} countries.\n')

# d. What is the maximum co2_emmission in the dataset and which food type and country does it belong to?
max_co2_emmission = df.sort_values(by='co2_emmission', ascending=False).head(1)
print(f'Maximum CO2 emission:\n{max_co2_emmission}\n')

# e. How many countries produce more than 1000 Kg CO2/person/year for at least one food type?
more_1000_emission = df[df.co2_emmission > 1000]['co2_emmission'].nunique()
print(f'There are {more_1000_emission} countries that produce more than 1000 kg CO2/person/year for at least one food type.\n')

# f. Which country consumes the least amount of beef per person per year?
least_beef = df[df.food_category == 'Beef'].sort_values(by='consumption', ascending=False).tail(1)
print(f'Country which consumes least beef:\n{least_beef}\n')

# g. Which country consumes the most soybeans per person per year?
most_soybeans = df[df.food_category == 'Soybeans'].sort_values(by='consumption', ascending=False).head(1)
print(f'Country which consumes most soybeans:\n{most_soybeans}\n')

# h. What is the total emissions of all the meat products (Pork, Poultry, Fish, Lamb & Goat, Beef) in the dataset combined?
meat = ['Pork', 'Poultry', 'Fish', 'Lamb & Goat', 'Beef']
tot_meat_emission = df[df.food_category.isin(meat)]['co2_emmission'].sum()
print(f'Total emission due to meat products is: {tot_meat_emission} co2/person/year\n')

# i. What is the total emissions of all other (non-meat) products in the dataset combined?
tot_non_meat_emission = df[~df.food_category.isin(meat)]['co2_emmission'].sum()
print(f'Total emission due to non meat products is: {tot_non_meat_emission} co2/person/year')

# j. What country consumes the most food per person per year (across all food categories)?
country_most_consumption = df.groupby(by='country')['consumption'].sum().sort_values(ascending=False).head(1)
print(f'Country with highest food consumption:\n{country_most_consumption}\n')

# k. What food category is consumed the least across all countries?
less_consumed_cat = df.groupby(by='food_category')['consumption'].sum().sort_values().head(1)
print(f'Food category less consumed:\n{less_consumed_cat}\n')

# l. What country produces the most kg C02 per person per year?
country_max_co2 = df.groupby("country").sum().reset_index().sort_values(by="co2_emmission").iloc[0]["country"]
print(f'Country with highest CO2 emission:\n{country_max_co2}\n')

# m. Which food category is the biggest contributor to the above country’s C02 emissions?
biggest_contributor = df[df.country == country_max_co2].sort_values('co2_emmission').tail(1)
print(f'Biggest contributor to {country_max_co2} CO2 emission:\n{biggest_contributor}\n')

# n. What food category produces the most C02 per person per year across all countries? 
most_emissive_fc = df.groupby('food_category').sum().sort_values('co2_emmission').tail(1)
print(f'Food category producing the most co2 emission:\n{most_emissive_fc}\n')

# o. What food category is consumed the most across all countries per person per year?
most_consumed_cat = df.groupby('food_category').sum().sort_values('consumption', ascending=False).reset_index().iloc[0]['food_category']
print(f'The most consumed food category:\n{most_consumed_cat}\n')

# p. What food category is consumed the least across all countries?
least_consumed_cat = df.groupby('food_category').sum().sort_values('consumption').reset_index().iloc[0]['food_category']
print(f'The least consumed food category is: {least_consumed_cat}\n')

# q. Make the dataset wide by pivoting on the food_category column. You’ll end up with a “multi-index” dataframe, with multiple levels of columns.
p_df = df.pivot(index='food_category', columns='country')
print(p_df)

## EXTRA
# What country produces the most kg C02 per person per year? (same as 
# previous question l. the way we answer the same data analysis 
# question changes depending on the format of the data (wide vs long))

print(p_df['co2_emmission'].sum().sort_values().tail(1))