import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 

warnings.filterwarnings("ignore")

df=pd.read_csv("ML/EDA/insurance.csv")

# EDA

print(df.shape)
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum()) 

# visualization 

numeric_columns=['age', 'bmi', 'children', 'charges']
# for col in numeric_columns:
#     plt.figure(figsize=(8,4))
#     sns.histplot(df[col], kde=True,bins=20)
#     plt.title(f"Distribution of {col}")
#     plt.show()

# sns.countplot(x=df['children'])
# plt.title("Distribution of Children")
# plt.xlabel("Number of Children")
# plt.ylabel("Count")
# plt.show()

# sns.countplot(x=df['smoker'])
# plt.title("Distribution of Smoker")
# plt.xlabel("Smoker")
# plt.ylabel("Count")
# plt.show()

# for col in numeric_columns:
#     plt.figure(figsize=(8,4))
#     sns.boxplot(x=df[col])
#     plt.title(f"Boxplot of {col}")
#     plt.show()

# plt.figure(figsize=(8,6))
# sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', linewidths=0.5)
# plt.title("Correlation Heatmap")
# plt.show()


#DATA CLEANING AND PREPROCESSING
df_cleaned=df.copy()
df_cleaned.drop_duplicates(inplace=True)
print(df_cleaned.shape)

print(df_cleaned.dtypes)
print(df_cleaned['sex'].value_counts())
df_cleaned['sex']=df_cleaned['sex'].map({"male" : 0, "female" : 1}) #label encoding

print(df_cleaned['smoker'].value_counts())
df_cleaned['smoker']=df_cleaned['smoker'].map({"no" : 0, "yes" : 1})

df_cleaned.rename(columns={'sex': 'is_female', 'smoker': 'is_smoker'}, inplace=True)

print(df_cleaned['region'].value_counts())
df_cleaned=pd.get_dummies(df_cleaned, columns=['region'], drop_first=False) #one hot encoding

df_cleaned=df_cleaned.astype(int)
print(df_cleaned.head())

#FEATURE ENGINEERING 
sns.histplot(df['bmi'])
plt.show()

df_cleaned['bmi_category']=pd.cut(
    df_cleaned['bmi'],
    bins=[0, 18.5, 24.9, 29.9, float('inf')],
    labels=['Underweight', 'Normal', 'Overweight', 'Obese']
)#pd.cut split continuous data into intervals (bins)
print(df_cleaned.head())
df_cleaned=pd.get_dummies(df_cleaned, columns=['bmi_category'], drop_first=False)
df_cleaned=df_cleaned.astype(int)
print(df_cleaned.head())

#FEATURE SCALING
from sklearn.preprocessing import StandardScaler
cols=['age', 'bmi', 'children']
scaler=StandardScaler()
df_cleaned[cols]=scaler.fit_transform(df_cleaned[cols])
print(df_cleaned.head()) #don't touch charges bcz its output

#FEATURE EXTRACTION
import numpy as np
import pandas as pd
from sklearn.feature_selection import chi2
from sklearn.preprocessing import KBinsDiscretizer #converts continuous target into categories

selected_features=[
    'age', 'bmi', 'children', 'is_female', 'is_smoker',
    'region_northeast', 'region_northwest', 'region_southeast', 'region_southwest',
    'bmi_category_Underweight', 'bmi_category_Normal', 'bmi_category_Overweight', 'bmi_category_Obese' 
]

correlations = {
    feature: np.corrcoef(df_cleaned[feature], df_cleaned['charges'])[0, 1]
    for feature in selected_features
} #it creates 2*2 matrix then take row 0, column 1

correlation_df = pd.DataFrame(
    list(correlations.items()),
    columns=['Features', 'Pearson Correlation']
).sort_values(by='Pearson Correlation', ascending=False)

print(correlation_df)

cat_features=[
    'is_female', 'is_smoker',
    'region_northeast', 'region_northwest', 'region_southeast', 'region_southwest',
    'bmi_category_Underweight', 'bmi_category_Normal', 'bmi_category_Overweight', 'bmi_category_Obese'
]
X_cat = df_cleaned[cat_features]

kb = KBinsDiscretizer(n_bins=4, encode='ordinal', strategy='quantile') #encode=ordinal instead of labels like low,medium we will get 0,1,2,3
y_binned = kb.fit_transform(df_cleaned[['charges']]).ravel() #chi square requires categorical target variable
#chi square expects 1D target array so we use ravel
chi2_values, p_values = chi2(X_cat, y_binned)

chi2_df = pd.DataFrame({
    'Feature': X_cat.columns,
    'chi2_statistic': chi2_values,
    'p_value': p_values
})
#High chi2 → strong dependency
#Low p-value → important feature
chi2_df['Decision'] = np.where(
    chi2_df['p_value'] < 0.05,
    'Reject Null (Keep Feature)',
    'Accept Null (Drop Feature)'
)
# np.where function automatically assigns the alternative label

chi2_df = chi2_df.sort_values(by='p_value')

print(chi2_df)

final_df = df_cleaned[
    ['age', 'bmi', 'is_smoker', 'charges',
     'region_southeast', 'bmi_category_Obese']
]

print(final_df)