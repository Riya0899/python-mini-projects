# discount,final price,ordersize,payment method

import pandas as pd 

data = {
    "Order_ID": [101, 102, 103, 104, 105],
    "Customer": ["Aman", "Riya", "Karan", "Neha", "Arjun"],
    "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Grocery"],
    "Amount": [12000, 2500, 8000, 1500, 600],
    "payment_mode": ["upi", "cod", "card", "upi", "cod"]
}

df=pd.DataFrame(data)

def calculate_discount(amount):
    if amount>10000:
        return amount*0.1
    elif amount>5000:
        return amount*0.05
    else:
        return 0
    
df['discount']=df['Amount'].map(calculate_discount)

def calculate_final_price(row):
    return row['Amount']-row['discount']

df['final price']=df.apply(calculate_final_price, axis=1)

def order_size(amount):
    if amount>10000:
        return 'large'
    elif amount>5000:
        return 'medium'
    else:
        return 'small'

df['size']=df['Amount'].map(order_size)

def payment_method(payment_mode):
    if payment_mode=='upi':
        return 'digital'
    elif payment_mode=='cod':
        return 'cash'
    else:
        return 'card'

df['payment method']=df['payment_mode'].map(payment_method)
print(df)

print("\nTOTAL DISCOUNT GIVEN:",df['discount'].sum())
print("AVERAGE FINAL PRICE:",df['final price'].mean())
print("NUMBER OF LARGE ORDERS:",len(df[df['size']=='large']))
print("PAYMENT METHOD DISTRIBUTION:")
print(df['payment method'].value_counts())
print("TOP CUSTOMER:",df.loc[df['final price'].idxmax()])
print("TOTAL SALES BY CATEGORY:")
print(df.groupby('Category')['final price'].sum())
print("AVERAGE DISCOUNT BY PAYMENT METHOD:")
print(df.groupby('payment method')['discount'].mean())

