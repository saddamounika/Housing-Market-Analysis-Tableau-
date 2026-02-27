import pandas as pd

# File name check cheskondi (path correct ga ivvandi)
df = pd.read_csv('C:\Users\91630\OneDrive\Desktop\Mouni\projects')

# 1. House Age: 2026 - yr_built
df['house_age'] = 2026 - df['yr_built']

# 2. Years Since Renovation: 
# If yr_renovated is 0, then years since renovation = house_age.
# Else current_year - yr_renovated.
df['years_since_renov'] = df.apply(
    lambda x: 2026 - x['yr_renovated'] if x['yr_renovated'] > 0 else (2026 - x['yr_built']), 
    axis=1
)

# 3. Renovation Status for Pie Chart
df['renov_status'] = df['yr_renovated'].apply(lambda x: 'Renovated' if x > 0 else 'Original')

# Cleaned data save cheyandi
df.to_csv('cleaned_housing_data.csv', index=False)
print("Data ready! Tableau ki upload cheyadaniki 'cleaned_housing_data.csv' ready ga undi.")