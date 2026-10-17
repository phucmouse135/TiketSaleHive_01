"""
Bài Tập Thực Hành Pandas
======================

Hãy hoàn thành các bài tập sau sử dụng dữ liệu từ pandas_project.py
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# ============================================================================
# SETUP: Tạo dữ liệu mẫu (sử dụng code từ pandas_project.py)
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

# Data cleaning
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
# BÀI TẬP
# ============================================================================

print("=" * 80)
print("BÀI TẬP THỰC HÀNH PANDAS")
print("=" * 80)

# ---------------------------------------------------------------------------
# BÀI 1: INDEXING - Sử dụng loc, iloc, at, iat
# ---------------------------------------------------------------------------
print("\n" + "=" * 80)
print("BÀI 1: INDEXING")
print("=" * 80)

print("\n--- Bài 1.1: Sử dụng iloc ---")
print("TODO: In ra 5 hàng đầu tiên và 3 cột đầu tiên")
# Viết code ở đây
# answer_1_1 = df.iloc[0:5, 0:3]
# print(answer_1_1)

print("\n--- Bài 1.2: Sử dụng loc ---")
print("TODO: In ra dữ liệu của Store A với 3 cột: store, category, quantity")
# Viết code ở đây
# answer_1_2 = df.loc[df['store'] == 'Store A', ['store', 'category', 'quantity']]
# print(answer_1_2.head())

print("\n--- Bài 1.3: Sử dụng at/iat ---")
print("TODO: Lấy giá trị satisfaction của hàng thứ 10")
print("  - Dùng at: df.at[10, 'satisfaction']")
print("  - Dùng iat: df.iat[10, 6]")
# Viết code ở đây

print("\n--- Bài 1.4: Boolean indexing ---")
print("TODO: Tìm tất cả các giao dịch có quantity > 15 và satisfaction >= 4")
# Viết code ở đây

# ---------------------------------------------------------------------------
# BÀI 2: DATAFRAME INTERNALS - Hiểu DataFrame là dict của Series
# ---------------------------------------------------------------------------
print("\n" + "=" * 80)
print("BÀI 2: DATAFRAME INTERNALS")
print("=" * 80)

print("\n--- Bài 2.1: Truy cập columns ---")
print("TODO: In ra:")
print("  1. Danh sách tất cả tên cột")
print("  2. Số lượng cột")
print("  3. Dtype của từng cột")
# Viết code ở đây

print("\n--- Bài 2.2: Truy cập Series ---")
print("TODO: Lấy column 'quantity' và in ra:")
print("  1. Type của nó")
print("  2. Mean, median, std")
print("  3. 5 giá trị đầu tiên")
# Viết code ở đây

print("\n--- Bài 2.3: Tạo Series mới ---")
print("TODO: Tạo một Series mới tên là 'revenue' = quantity * price")
print("      Sau đó thêm vào DataFrame (df['revenue'] = ...)")
# Viết code ở đây

# ---------------------------------------------------------------------------
# BÀI 3: DATA CLEANING - Đổi tên, xử lý NaN, ép kiểu, categorical
# ---------------------------------------------------------------------------
print("\n" + "=" * 80)
print("BÀI 3: DATA CLEANING")
print("=" * 80)

print("\n--- Bài 3.1: Đổi tên cột ---")
print("TODO: Đổi tên cột 'satisfaction' thành 'rating'")
# Viết code ở đây
# df_temp = df.rename(columns={'satisfaction': 'rating'})

print("\n--- Bài 3.2: Kiểm tra và xử lý NaN ---")
print("TODO:")
print("  1. Kiểm tra số lượng NaN trong từng cột")
print("  2. In ra các hàng có NaN")
print("  3. Xóa các hàng có NaN")
# Viết code ở đây

print("\n--- Bài 3.3: Ép kiểu ---")
print("TODO: Chuyển đổi dtype:")
print("  - 'age' thành int8 (tiết kiệm bộ nhớ)")
print("  - 'price' thành float32 (không cần độ chính xác cao)")
# Viết code ở đây

print("\n--- Bài 3.4: Categorical ---")
print("TODO:")
print("  1. Chuyển 'category' thành categorical")
print("  2. In ra các categories")
print("  3. So sánh memory usage trước và sau")
# Viết code ở đây

# ---------------------------------------------------------------------------
# BÀI 4: GROUPBY - agg (Aggregation)
# ---------------------------------------------------------------------------
print("\n" + "=" * 80)
print("BÀI 4: GROUPBY - AGG")
print("=" * 80)

print("\n--- Bài 4.1: agg cơ bản ---")
print("TODO: Tính tổng quantity bán theo store")
# Viết code ở đây
# answer_4_1 = df.groupby('store')['quantity'].sum()
# print(answer_4_1)

print("\n--- Bài 4.2: agg với nhiều hàm ---")
print("TODO: Tính theo store:")
print("  - quantity: sum, mean, max, min")
print("  - price: mean")
print("  - satisfaction: mean")
# Viết code ở đây

print("\n--- Bài 4.3: agg theo nhiều cột ---")
print("TODO: Tính agg theo [store, category]:")
print("  - quantity: sum")
print("  - price: mean")
print("  - satisfaction: mean")
# Viết code ở đây

print("\n--- Bài 4.4: agg với custom function ---")
print("TODO: Tính range (max - min) của quantity theo store")
# Viết code ở đây
# answer_4_4 = df.groupby('store')['quantity'].agg(lambda x: x.max() - x.min())
# print(answer_4_4)

# ---------------------------------------------------------------------------
# BÀI 5: GROUPBY - transform
# ---------------------------------------------------------------------------
print("\n" + "=" * 80)
print("BÀI 5: GROUPBY - TRANSFORM")
print("=" * 80)

print("\n--- Bài 5.1: transform cơ bản ---")
print("TODO: Thêm cột 'store_avg_quantity' = trung bình quantity của store")
print("      Kiểm tra shape của df trước và sau")
# Viết code ở đây

print("\n--- Bài 5.2: transform với tỷ phần trăm ---")
print("TODO: Thêm cột 'quantity_pct' = quantity / tổng quantity của store * 100")
# Viết code ở đây

print("\n--- Bài 5.3: transform với rank ---")
print("TODO: Thêm cột 'rank_in_store' = rank của quantity trong store")
print("      (Quantity cao nhất = rank 1)")
# Viết code ở đây

print("\n--- Bài 5.4: transform để tính outlier ---")
print("TODO: Tính z-score của quantity trong từng store")
print("      Formula: (x - mean) / std")
print("      Thêm cột 'quantity_zscore'")
# Viết code ở đây

# ---------------------------------------------------------------------------
# BÀI 6: agg vs transform
# ---------------------------------------------------------------------------
print("\n" + "=" * 80)
print("BÀI 6: AGG VS TRANSFORM")
print("=" * 80)

print("\n--- Bài 6.1: So sánh shape ---")
print("TODO:")
print("  1. Shape của df gốc")
print("  2. Shape sau df.groupby('store')[['quantity']].agg('sum')")
print("  3. Shape sau df.groupby('store')['quantity'].transform('sum')")
print("  4. Giải thích tại sao shape khác nhau")
# Viết code ở đây

print("\n--- Bài 6.2: Chọn agg hay transform ---")
print("TODO: Quyết định nên dùng agg hay transform cho mỗi case:")
print("  1. Muốn tính tổng doanh thu theo store → ?")
print("  2. Muốn thêm cột % doanh thu trong store → ?")
print("  3. Muốn tìm store nào bán nhiều nhất → ?")
print("  4. Muốn đánh dấu các giao dịch có qty lớn bất thường → ?")
# Viết code ở đây

# ---------------------------------------------------------------------------
# BÀI 7: THỰC HÀNH COMBINED
# ---------------------------------------------------------------------------
print("\n" + "=" * 80)
print("BÀI 7: THỰC HÀNH COMBINED")
print("=" * 80)

print("\n--- Bài 7.1: Pipeline data cleaning ---")
print("TODO: Thực hiện pipeline sau:")
print("  1. Lọc dữ liệu của store A và B")
print("  2. Lọc satisfaction >= 3")
print("  3. Thêm cột revenue = quantity * price")
print("  4. In ra top 5 giao dịch có revenue cao nhất")
# Viết code ở đây

print("\n--- Bài 7.2: Phân tích theo category ---")
print("TODO:")
print("  1. Tính tổng quantity bán theo category và store")
print("  2. Tạo pivot table")
print("  3. Tìm category nào bán nhiều nhất ở mỗi store")
# Viết code ở đây

print("\n--- Bài 7.3: Phân tích customer age ---")
print("TODO:")
print("  1. Chia age thành 3 nhóm: young (18-40), middle (41-60), senior (60+)")
print("  2. Tính average satisfaction theo age group và store")
print("  3. Vẽ bảng tóm tắt (tùy chọn)")
# Viết code ở đây

# ---------------------------------------------------------------------------
# HƯỚNG DẪN GIẢI
# ---------------------------------------------------------------------------
print("\n" + "=" * 80)
print("HƯỚNG DẪN GIẢI (Uncomment để xem)")
print("=" * 80)

print("\n# Hướng dẫn chung:")
print("# 1. Đọc kỹ yêu cầu của từng bài")
print("# 2. Tư duy về loại dữ liệu cần: 1 giá trị, Series, DataFrame?")
print("# 3. Chọn phương pháp: iloc/loc, agg, transform, pivot?")
print("# 4. Viết code từng bước, test từng bước")
print("# 5. So sánh kết quả với hướng dẫn")

