"""
Pandas I - DataFrame internals, Indexing, GroupBy Project
=========================================================
Dự án học tập về:
1. DataFrame internals - hiểu DataFrame là dict của Series
2. Indexing - loc/iloc/at/iat
3. Data Cleaning - đổi tên cột, xử lý NaN, ép kiểu, categorical
4. GroupBy - agg vs transform
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# ============================================================================
# PHẦN 1: TẠO DỮ LIỆU MẪU
# ============================================================================
print("=" * 80)
print("PHẦN 1: TẠO DỮ LIỆU MẪU")
print("=" * 80)

# Tạo dữ liệu mẫu về bán hàng của cửa hàng
np.random.seed(42)
dates = [datetime(2024, 1, 1) + timedelta(days=x) for x in range(30)]

data = {
    'sale_date': dates * 4,  # Lặp lại 4 lần cho 4 cửa hàng
    'store_name': ['Store A', 'Store B', 'Store C', 'Store D'] * 30,
    'product_category': np.random.choice(['Electronics', 'Clothing', 'Food', 'Books'], 120),
    'quantity_sold': np.random.randint(1, 20, 120),
    'price_per_unit': np.random.uniform(10, 500, 120),
    'customer_age': np.random.randint(18, 80, 120),
    'satisfaction_score': np.random.choice([np.nan, 1, 2, 3, 4, 5], 120),  # Có NaN
}

df = pd.DataFrame(data)
# Thêm một vài NaN vào các cột khác
df.loc[np.random.choice(df.index, 5), 'quantity_sold'] = np.nan

print("\nDữ liệu gốc:")
print(df.head(10))
print(f"\nShape: {df.shape}")
print(f"\nCác cột: {df.columns.tolist()}")

# ============================================================================
# PHẦN 2: HIỂU DATAFRAME LÀ DICT CỦA SERIES
# ============================================================================
print("\n" + "=" * 80)
print("PHẦN 2: HIỂU DATAFRAME LÀ DICT CỦA SERIES")
print("=" * 80)

print("\n1. Mỗi cột là một Series:")
print(f"Type của df['store_name']: {type(df['store_name'])}")
print(f"Series này có {len(df['store_name'])} phần tử")

print("\n2. Truy cập từng cột:")
print("df['quantity_sold']:")
print(df['quantity_sold'].head())

print("\n3. Cấu trúc nội bộ - columns:")
print(f"df.columns: {df.columns.tolist()}")
print(f"df.index: {df.index.tolist()[:5]}... (truncated)")

print("\n4. Thông tin dtype của từng cột:")
print(df.dtypes)

# ============================================================================
# PHẦN 3: INDEXING - loc, iloc, at, iat
# ============================================================================
print("\n" + "=" * 80)
print("PHẦN 3: INDEXING - loc, iloc, at, iat")
print("=" * 80)

print("\n--- A. iloc (Index-based, sử dụng vị trí số) ---")
print("iloc[0, 0] - hàng thứ 0, cột thứ 0:")
print(df.iloc[0, 0])

print("\niloc[0:3, 0:3] - 3 hàng đầu, 3 cột đầu:")
print(df.iloc[0:3, 0:3])

print("\niloc[:, 1] - tất cả hàng, cột thứ 1:")
print(df.iloc[:5, 1])

print("\n--- B. loc (Label-based, sử dụng tên cột/index) ---")
print("loc[0, 'store_name'] - hàng 0, cột 'store_name':")
print(df.loc[0, 'store_name'])

print("\nloc[0:2, ['store_name', 'product_category']] - hàng 0-2, 2 cột cụ thể:")
print(df.loc[0:2, ['store_name', 'product_category']])

print("\nloc với điều kiện - bán hàng > 15 chiếc:")
print(df.loc[df['quantity_sold'] > 15, ['store_name', 'quantity_sold']].head())

print("\n--- C. at (Truy cập nhanh 1 phần tử, label-based) ---")
print("at[5, 'store_name']:")
print(df.at[5, 'store_name'])

print("\n--- D. iat (Truy cập nhanh 1 phần tử, index-based) ---")
print("iat[5, 2] - hàng 5, cột 2:")
print(df.iat[5, 2])

print("\n--- So sánh tốc độ ---")
print("at/iat nhanh hơn loc/iloc vì chỉ trả về 1 giá trị")
print("loc/iloc linh hoạt hơn cho việc lấy nhiều giá trị")

# ============================================================================
# PHẦN 4: DATA CLEANING
# ============================================================================
print("\n" + "=" * 80)
print("PHẦN 4: DATA CLEANING")
print("=" * 80)

df_clean = df.copy()

# 4.1 Đổi tên cột
print("\n--- 4.1 Đổi tên cột ---")
print("Tên cột ban đầu:", df_clean.columns.tolist())

df_clean = df_clean.rename(columns={
    'sale_date': 'date',
    'store_name': 'store',
    'product_category': 'category',
    'quantity_sold': 'quantity',
    'price_per_unit': 'price',
    'customer_age': 'age',
    'satisfaction_score': 'satisfaction'
})
print("Tên cột sau rename:", df_clean.columns.tolist())

# 4.2 Xử lý NaN
print("\n--- 4.2 Xử lý NaN ---")
print("Số NaN trong từng cột:")
print(df_clean.isnull().sum())

print("\nXử lý NaN:")
print("- quantity: fill với median")
df_clean['quantity'] = df_clean['quantity'].fillna(df_clean['quantity'].median())

print("- satisfaction: fill với mode (mode=5 là phổ biến nhất)")
mode_val = df_clean['satisfaction'].mode()[0]
df_clean['satisfaction'] = df_clean['satisfaction'].fillna(mode_val)

print("\nSau khi xử lý NaN:")
print(df_clean.isnull().sum())

# 4.3 Ép kiểu
print("\n--- 4.3 Ép kiểu ---")
print("Dtype trước khi convert:")
print(f"  satisfaction: {df_clean['satisfaction'].dtype}")
print(f"  age: {df_clean['age'].dtype}")

df_clean['satisfaction'] = df_clean['satisfaction'].astype('int8')
df_clean['age'] = df_clean['age'].astype('int8')
df_clean['quantity'] = df_clean['quantity'].astype('int16')
df_clean['price'] = df_clean['price'].astype('float32')

print("\nDtype sau khi convert:")
print(f"  satisfaction: {df_clean['satisfaction'].dtype}")
print(f"  age: {df_clean['age'].dtype}")
print(f"  quantity: {df_clean['quantity'].dtype}")
print(f"  price: {df_clean['price'].dtype}")

# 4.4 Categorical
print("\n--- 4.4 Categorical ---")
print("Trước khi convert categorical:")
print(f"  store dtype: {df_clean['store'].dtype}")
print(f"  store unique: {df_clean['store'].nunique()}")
print(f"  Memory usage: {df_clean['store'].memory_usage()}")

df_clean['store'] = df_clean['store'].astype('category')
df_clean['category'] = df_clean['category'].astype('category')

print("\nSau khi convert categorical:")
print(f"  store dtype: {df_clean['store'].dtype}")
print(f"  store unique: {df_clean['store'].nunique()}")
print(f"  Memory usage: {df_clean['store'].memory_usage()}")

print("\nCategories của 'store':", df_clean['store'].cat.categories.tolist())
print("Categories của 'category':", df_clean['category'].cat.categories.tolist())

# ============================================================================
# PHẦN 5: GROUPBY - agg vs transform
# ============================================================================
print("\n" + "=" * 80)
print("PHẦN 5: GROUPBY - agg vs transform")
print("=" * 80)

# 5.1 GroupBy cơ bản
print("\n--- 5.1 GroupBy cơ bản ---")
grouped = df_clean.groupby('store')
print("Các nhóm Store:")
for name, group in grouped:
    print(f"  {name}: {len(group)} rows")

# 5.2 agg - tổng hợp dữ liệu
print("\n--- 5.2 agg (Aggregation - tập hợp dữ liệu) ---")
print("Dùng khi muốn GIẢM số lượng hàng")

# Tổng hợp đơn giản
agg_simple = df_clean.groupby('store')['quantity'].sum()
print("\nTổng số lượng bán theo store:")
print(agg_simple)

# Tổng hợp với nhiều hàm
agg_multi = df_clean.groupby('store')[['quantity', 'price', 'satisfaction']].agg({
    'quantity': ['sum', 'mean', 'max'],
    'price': ['min', 'max', 'mean'],
    'satisfaction': ['mean', 'count']
})
print("\nTổng hợp đa chiều:")
print(agg_multi)

# Tổng hợp theo nhiều cột
agg_multi_group = df_clean.groupby(['store', 'category'])['quantity'].agg(['sum', 'mean', 'count'])
print("\nTổng hợp theo store và category:")
print(agg_multi_group.head(10))

# 5.3 transform - thêm cột mới
print("\n--- 5.3 transform (Transformation - thêm cột) ---")
print("Dùng khi muốn GIỮ số lượng hàng, thêm cột mới")

# Thêm cột với số lượng trung bình của cửa hàng
df_clean['store_avg_quantity'] = df_clean.groupby('store')['quantity'].transform('mean')

# Thêm cột với tỷ phần trăm so với tổng của store
df_clean['quantity_pct_of_store'] = df_clean.groupby('store')['quantity'].transform(lambda x: x / x.sum() * 100)

# Thêm cột rank trong từng store
df_clean['quantity_rank_in_store'] = df_clean.groupby('store')['quantity'].transform('rank')

print("\nSau transform, df_clean có thêm 3 cột mới:")
print(df_clean[['store', 'quantity', 'store_avg_quantity', 'quantity_pct_of_store', 'quantity_rank_in_store']].head(10))

# 5.4 So sánh agg vs transform
print("\n--- 5.4 So sánh agg vs transform ---")
print("agg: Giảm dữ liệu từ 120 rows thành 4 rows (một cho mỗi store)")
print(f"  Result shape: {df_clean.groupby('store')['quantity'].agg('sum').shape}")

print("\ntransform: Giữ 120 rows, thêm cột mới")
print(f"  Input shape: {df_clean.shape}")
print(f"  Output shape (có thêm cột): {df_clean.shape}")

# 5.5 Use case thực tế
print("\n--- 5.5 Use case thực tế ---")
# Tính z-score (lệch chuẩn so với trung bình của store)
df_clean['quantity_zscore'] = df_clean.groupby('store')['quantity'].transform(
    lambda x: (x - x.mean()) / x.std()
)

print("Z-score số lượng bán (so với trung bình của store):")
print(df_clean[['store', 'quantity', 'quantity_zscore']].head(8))

# ============================================================================
# PHẦN 6: THỐNG KÊ VÀ INSIGHTS
# ============================================================================
print("\n" + "=" * 80)
print("PHẦN 6: THỐNG KÊ VÀ INSIGHTS")
print("=" * 80)

print("\nThống kê cơ bản:")
print(df_clean.describe())

print("\nThực hành combined: Tìm top 3 sản phẩm bán chạy nhất theo từng store")
top_products = df_clean.groupby(['store', 'category']).agg({
    'quantity': 'sum',
    'price': 'mean',
    'satisfaction': 'mean'
}).reset_index()
top_products = top_products.sort_values(['store', 'quantity'], ascending=[True, False])
print(top_products.head(12))

# ============================================================================
# PHẦN 7: LƯỚI TRỊ VÀ PIVOT
# ============================================================================
print("\n" + "=" * 80)
print("PHẦN 7: PIVOT - Tạo bảng tổng hợp")
print("=" * 80)

# Pivot table - bán hàng theo store và category
pivot = df_clean.pivot_table(
    values='quantity',
    index='store',
    columns='category',
    aggfunc='sum',
    fill_value=0
)
print("\nPivot table - Số lượng bán theo Store và Category:")
print(pivot)

print("\n" + "=" * 80)
print("KẾT THÚC DỰ ÁN")
print("=" * 80)
