# handling missing values

# import pandas as pd 
# data={
#     'name':['pavan','kapil','lalit','ishan','om'],
#     'age':[23,None,25,26,None],
#     'salary':[10000,20000,30000,None,None]
# }

# df=pd.DataFrame(data)
# print(df)

# print(df.isnull().sum())
# df_drop=df.dropna()
# print(df_drop)

# df['age'].fillna(df['age'].mean(),inplace=True)
# df['salary'].fillna(df['salary'].mean(),inplace=True)
# print(df)

# # encoding categorical values
# # 1. label encoding  2. one-hot encoding

# from sklearn.preprocessing import LabelEncoder,OneHotEncoder
# import pandas as pd

# df=pd.read_csv('aiml\data.csv')

# # label encoding
# df_label=df.copy()
# le=LabelEncoder()
# df_label['gender_encoded']=le.fit_transform(df_label['Gender'])   # fit_transform means fir means learn and transform means convert the data into encoded form
# df_label['passed_encoded']=le.fit_transform(df_label['Passed'])

# print("\nLabel Encoded DataFrame")
# print(df_label[['Name','Gender','gender_encoded','Passed','passed_encoded']])

# df_encoded=pd.get_dummies(df,columns=['City']) 
# #coverting into boolean value
# df_encoded = df_encoded.astype({col: int for col in df_encoded.select_dtypes(include='bool').columns})
# print("\nOne-Hot Encoded DataFrame")
# print(df_encoded)

# # feature scaling 
# # 1. standard scaler -it bring values with mean =0 and standard deviation=1
# from sklearn.preprocessing import StandardScaler
# scaler=StandardScaler()
# x_scaled=scaler.fit_transform()

# # 2. min-max scaler- it bring values between 0 and 1
# from sklearn.preprocessing import MinMaxScaler
# scaler=MinMaxScaler()
# x_scaled=scaler.fit_transform()

# splitting data into training and testing sets

import pandas as pd
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.model_selection import train_test_split

data={
    'studyhours':[1,2,3,4,5],
    'testscore':[40,50,60,70,80]
}

df=pd.DataFrame(data)

# standard scaler
standard_scaler=StandardScaler()
standard_scaled=standard_scaler.fit_transform(df)  # fir will learn mean and standard deviation and transform will convert the data into scaled form using formula (x-mean)/std
print("standard scaler output")
print(pd.DataFrame(standard_scaled,columns=['studyhours','testscore']))

# min-max scaler
minmax_scaler=MinMaxScaler()
minmax_scaled=minmax_scaler.fit_transform(df)  # using the formula (x-min)/(max-min)
print("\nmin-max scaler output")
print(pd.DataFrame(minmax_scaled,columns=['studyhours','testscore']))

#train-test split
x=df[['studyhours']]
y=df[['testscore']]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
print("\nTraining data")
print(x_train)

print("testing data")
print(x_test)

print("\nTraining data")
print(y_train)

print("testing data")
print(y_test)
