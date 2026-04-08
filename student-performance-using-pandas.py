import pandas as pd 

data={
    "name":["aman","riya","karan","neha","arjun"],
    "math":[90,80,70,60,50],
    "science":[85,75,65,55,45],
    "english":[88,78,68,58,48]
    
}
df=pd.DataFrame(data)

def calculate_total(row):
    return row['math'] + row['science'] + row['english']

df['total'] = df.apply(calculate_total, axis=1)

def calculate_percentage(total):
    return total/3

df['percentage']=df['total'].map(calculate_percentage)

def assign_grade(percentage):
    if percentage>=90:
        return 'A+'
    elif percentage>=75:
        return 'A'
    elif percentage>=60:
        return 'B'
    else:
        return 'C'

df['grade']=df['percentage'].map(assign_grade)

performance_map={
    'A+':'execellent',
    'A':'very good',
    'B':'good',
    'C':'needs improvement'
}

df['performance']=df['grade'].map(performance_map)
print(df)

print("\nTOP PERFORMER:")
print(df.loc[df['percentage'].idxmax()])

print("\n AVERAGE PERCENTAGE:",df['percentage'].mean())
print("GRADE DISTRIBUTION:")
print(df['grade'].value_counts())
print("PERFORMANCE DISTRIBUTION:")
print(df['performance'].value_counts())

