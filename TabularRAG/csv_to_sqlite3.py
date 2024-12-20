import os
import sqlite3
import pandas as pd

# 定義資料夾路徑
tables_folder = "cpic_data\\tables"
views_folder = "cpic_data\\views"

# SQLite 資料庫檔案名稱
db_name = "drug.db"

# 建立資料庫連線
conn = sqlite3.connect(db_name)

def import_csv_to_sqlite(folder, conn):
    for file in os.listdir(folder):
        if file.endswith(".csv"):
            file_path = os.path.join(folder, file)
            table_name = os.path.splitext(file)[0]  # 使用檔名作為表名
            print(f"正在導入 {file_path} 至表 {table_name}")
            
            # 將 CSV 讀取為 DataFrame
            df = pd.read_csv(file_path)
            
            # 將 DataFrame 寫入 SQLite 資料庫
            df.to_sql(table_name, conn, if_exists="replace", index=False)

# 將 tables 資料夾的 CSV 文件導入
print("導入 tables 資料夾中的 CSV 文件...")
import_csv_to_sqlite(tables_folder, conn)

# 關閉資料庫連線
conn.close()
print("所有 CSV 文件已成功導入 SQLite 資料庫。")
