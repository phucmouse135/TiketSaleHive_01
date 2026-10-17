"""
Giải Pháp Tham Khảo - Pandas Exercises
====================================

File này chứa các giải pháp cho bài tập trong pandas_exercises.py
Hãy cố gắng giải quyết bài tập trước khi xem giải pháp!
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# ============================================================================
# SETUP: Tạo dữ liệu mẫu
# ============================================================================
np.random.seed(42)
dates = [datetime(2024, 1, 1) + timedelta(days=x) for x in range(30)]

data = {
    'sale_date': dates * 4,
    'store_name': ['Store A', 'Store B', 'Store C', 'Store D'] * 30,
    'product_category': np.random.choice(['Electronics', 'Clothing', 'Food', 'Books'], 120),
    'quantity_sold': np.random.randint(1, 20, 120),
    'price_per_unit': np.random.uniform(10, 500, 120),
    'customer_age': np.random.randint(18, 80, 120),
    'satisfaction_score': np.random.choice([np.nan, 1, 2, 3, 4, 5], 120),
}

df = pd.DataFrame(data)
df.loc[np.random.choice(df.index, 5), 'quantity_sold'] = np.nan

df = df.rename(columns={
    'sale_date': 'date',
    'store_name': 'store',
    'product_category': 'category',
    'quantity_sold': 'quantity',
    'price_per_unit': 'price',
    'customer_age': 'age',
    'satisfaction_score': 'satisfaction'
})

df['quantity'] = df['quantity'].fillna(df['quantity'].median())
mode_val = df['satisfaction'].mode()[0]
df['satisfaction'] = df['satisfaction'].fillna(mode_val)

df['satisfaction'] = df['satisfaction'].astype('int8')
df['quantity'] = df['quantity'].astype('int16')
df['store'] = df['store'].astype('category')
df['category'] = df['category'].astype('category')

# ============================================================================
# GIẢI PHÁP
# ============================================================================

print("=" * 80)
print("GIẢI PHÁP THAM KHẢO")
print("=" * 80)

# ---------------------------------------------------------------------------
# BÀI 1: INDEXING
# ---------------------------------------------------------------------------
print("\n" + "=" * 80)
print("BÀI 1: INDEXING - GIẢI PHÁP")
print("=" * 80)

print("\n--- Bài 1.1: iloc ---")
answer_1_1 = df.iloc[0:5, 0:3]
print("5 hàng đầu, 3 cột đầu:")
print(answer_1_1)

print("\n--- Bài 1.2: loc ---")
answer_1_2 = df.loc[df['store'] == 'Store A', ['store', 'category', 'quantity']]
print("Dữ liệu Store A:")
print(answer_1_2.head())

print("\n--- Bài 1.3: at/iat ---")
answer_1_3_at = df.at[10, 'satisfaction']
answer_1_3_iat = df.iat[10, 6]
print(f"at[10, 'satisfaction']: {answer_1_3_at}")
print(f"iat[10, 6]: {answer_1_3_iat}")

print("\n--- Bài 1.4: Boolean indexing ---")
answer_1_4 = df[(df['quantity'] > 15) & (df['satisfaction'] >= 4)]
print(f"Số giao dịch có quantity > 15 và satisfaction >= 4: {len(answer_1_4)}")
print(answer_1_4.head())

# ---------------------------------------------------------------------------
# BÀI 2: DATAFRAME INTERNALS
# ---------------------------------------------------------------------------
print("\n" + "=" * 80)
print("BÀI 2: DATAFRAME INTERNALS - GIẢI PHÁP")
print("=" * 80)

print("\n--- Bài 2.1: Truy cập columns ---")
print(f"Tên cột: {df.columns.tolist()}")
print(f"Số cột: {len(df.columns)}")
print("\nDtype của từng cột:")
print(df.dtypes)

print("\n--- Bài 2.2: Truy cập Series ---")
quantity_series = df['quantity']
print(f"Type: {type(quantity_series)}")
print(f"\nStatistics:")
print(f"  Mean: {quantity_series.mean():.2f}")
print(f"  Median: {quantity_series.median():.2f}")
print(f"  Std: {quantity_series.std():.2f}")
print(f"\n5 giá trị đầu:\n{quantity_series.head()}")

print("\n--- Bài 2.3: Tạo Series mới ---")
df['revenue'] = df['quantity'] * df['price']
print("Cột 'revenue' đã được thêm:")
print(df[['quantity', 'price', 'revenue']].head())

# ---------------------------------------------------------------------------
# BÀI 3: DATA CLEANING
# ---------------------------------------------------------------------------
print("\n" + "=" * 80)
print("BÀI 3: DATA CLEANING - GIẢI PHÁP")
print("=" * 80)

print("\n--- Bài 3.1: Đổi tên cột ---")
df_renamed = df.rename(columns={'satisfaction': 'rating'})
print(f"Cột cũ: 'satisfaction'")
print(f"Cột mới: 'rating' in {df_renamed.columns.tolist()}")

print("\n--- Bài 3.2: NaN handling ---")
print("Số NaN trong từng cột:")
print(df.isnull().sum())
print("\nCác hàng có NaN (nếu có):")
print(df[df.isnull().any(axis=1)])
print("\nSau khi dropna (giả sử có NaN):")
df_no_nan = df.dropna()
print(f"Shape trước: {df.shape}, Shape sau: {df_no_nan.shape}")

print("\n--- Bài 3.3: Ép kiểu ---")
df_temp = df.copy()
print("Trước khi convert:")
print(f"  age: {df_temp['age'].dtype}")
print(f"  price: {df_temp['price'].dtype}")

df_temp['age'] = df_temp['age'].astype('int8')
df_temp['price'] = df_temp['price'].astype('float32')
print("\nSau khi convert:")
print(f"  age: {df_temp['age'].dtype}")
print(f"  price: {df_temp['price'].dtype}")

print("\n--- Bài 3.4: Categorical ---")
print("Trước (memory):", df['category'].memory_usage())
df_cat = df.copy()
df_cat['category'] = df_cat['category'].astype('category')
print("Sau (memory):", df_cat['category'].memory_usage())
print(f"\nCategories: {df_cat['category'].cat.categories.tolist()}")

# ---------------------------------------------------------------------------
# BÀI 4: GROUPBY - AGG
# ---------------------------------------------------------------------------
print("\n" + "=" * 80)
print("BÀI 4: GROUPBY - AGG - GIẢI PHÁP")
print("=" * 80)

print("\n--- Bài 4.1: agg cơ bản ---")
answer_4_1 = df.groupby('store')['quantity'].sum()
print("Tổng quantity theo store:")
print(answer_4_1)

print("\n--- Bài 4.2: agg với nhiều hàm ---")
answer_4_2 = df.groupby('store')[['quantity', 'price', 'satisfaction']].agg({
    'quantity': ['sum', 'mean', 'max', 'min'],
    'price': 'mean',
    'satisfaction': 'mean'
})
print("Tổng hợp đa chiều:")
print(answer_4_2)

print("\n--- Bài 4.3: agg theo nhiều cột ---")
answer_4_3 = df.groupby(['store', 'category']).agg({
    'quantity': 'sum',
    'price': 'mean',
    'satisfaction': 'mean'
})
print("Tổng hợp theo store và category:")
print(answer_4_3.head(8))

print("\n--- Bài 4.4: agg với custom function ---")
answer_4_4 = df.groupby('store')['quantity'].agg(lambda x: x.max() - x.min())
print("Range (max - min) của quantity theo store:")
print(answer_4_4)

# ---------------------------------------------------------------------------
# BÀI 5: GROUPBY - TRANSFORM
# ---------------------------------------------------------------------------
print("\n" + "=" * 80)
print("BÀI 5: GROUPBY - TRANSFORM - GIẢI PHÁP")
print("=" * 80)

print("\n--- Bài 5.1: transform cơ bản ---")
df_5 = df.copy()
print(f"Shape trước: {df_5.shape}")
df_5['store_avg_quantity'] = df_5.groupby('store')['quantity'].transform('mean')
print(f"Shape sau: {df_5.shape}")
print("\nData sau transform:")
print(df_5[['store', 'quantity', 'store_avg_quantity']].head(8))

print("\n--- Bài 5.2: transform với tỷ phần trăm ---")
df_5['quantity_pct'] = df_5.groupby('store')['quantity'].transform(
    lambda x: x / x.sum() * 100
)
print("Tỷ phần trăm quantity trong store:")
print(df_5[['store', 'quantity', 'quantity_pct']].head(8))

print("\n--- Bài 5.3: transform với rank ---")
df_5['rank_in_store'] = df_5.groupby('store')['quantity'].transform('rank', ascending=False)
print("Rank quantity (cao nhất = 1):")
print(df_5[['store', 'quantity', 'rank_in_store']].head(8))

print("\n--- Bài 5.4: transform để tính outlier ---")
df_5['quantity_zscore'] = df_5.groupby('store')['quantity'].transform(
    lambda x: (x - x.mean()) / x.std()
)
print("Z-score của quantity:")
print(df_5[['store', 'quantity', 'quantity_zscore']].head(8))

# ---------------------------------------------------------------------------
# BÀI 6: AGG VS TRANSFORM
# ---------------------------------------------------------------------------
print("\n" + "=" * 80)
print("BÀI 6: AGG VS TRANSFORM - GIẢI PHÁP")
print("=" * 80)

print("\n--- Bài 6.1: So sánh shape ---")
shape_original = df.shape
shape_agg = df.groupby('store')[['quantity']].agg('sum').shape
shape_transform = df.groupby('store')['quantity'].transform('sum').shape

print(f"Shape gốc: {shape_original}")
print(f"Shape sau agg: {shape_agg} (giảm hàng)")
print(f"Shape sau transform: {shape_transform} (giữ hàng)")
print("\nGiải thích:")
print("- agg: giảm từ 120 rows → 4 rows (1 hàng per store)")
print("- transform: giữ 120 rows, thêm cột mới")

print("\n--- Bài 6.2: Chọn agg hay transform ---")
print("1. Muốn tính tổng doanh thu theo store → AGG")
print("2. Muốn thêm cột % doanh thu trong store → TRANSFORM")
print("3. Muốn tìm store nào bán nhiều nhất → AGG")
print("4. Muốn đánh dấu các giao dịch có qty lớn bất thường → TRANSFORM")

# ---------------------------------------------------------------------------
# BÀI 7: THỰC HÀNH COMBINED
# ---------------------------------------------------------------------------
print("\n" + "=" * 80)
print("BÀI 7: THỰC HÀNH COMBINED - GIẢI PHÁP")
print("=" * 80)

print("\n--- Bài 7.1: Pipeline data cleaning ---")
df_7_1 = df[df['store'].isin(['Store A', 'Store B'])].copy()
df_7_1 = df_7_1[df_7_1['satisfaction'] >= 3]
df_7_1['revenue'] = df_7_1['quantity'] * df_7_1['price']
top_5 = df_7_1.nlargest(5, 'revenue')
print("Top 5 giao dịch có revenue cao nhất (Store A, B + satisfaction >= 3):")
print(top_5[['store', 'category', 'quantity', 'price', 'revenue']])

print("\n--- Bài 7.2: Phân tích theo category ---")
pivot_data = df.groupby(['store', 'category'])['quantity'].sum().unstack(fill_value=0)
print("Pivot table - Số lượng theo store và category:")
print(pivot_data)
print("\nCategory bán nhiều nhất ở mỗi store:")
for store in pivot_data.index:
    best_cat = pivot_data.loc[store].idxmax()
    best_qty = pivot_data.loc[store].max()
    print(f"  {store}: {best_cat} ({best_qty} units)")

print("\n--- Bài 7.3: Phân tích customer age ---")
df_7_3 = df.copy()
# Chia age thành nhóm
df_7_3['age_group'] = pd.cut(
    df_7_3['age'],
    bins=[0, 40, 60, 100],
    labels=['Young (18-40)', 'Middle (41-60)', 'Senior (60+)']
)
satisfaction_by_age = df_7_3.groupby(['age_group', 'store'])['satisfaction'].mean().unstack()
print("Average satisfaction theo age group và store:")
print(satisfaction_by_age.round(2))

print("\n" + "=" * 80)
print("KẾT THÚC GIẢI PHÁP")
print("=" * 80)
