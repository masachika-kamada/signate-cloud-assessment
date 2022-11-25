import pandas as pd

df = pd.read_csv("ダイエット意識調査結果_201806.csv", encoding="cp932")
print(df.head())

# 『列「Q1」が男性である』という条件に該当するデータのみを抽出した新たな表を作成
df_man = df[df["Q1"] == "男"]
print(df_man.head())
# df_manの行数
print(df_man.shape[0])

# 『列「Q2」が40以上である』という条件に該当するデータのみを抽出
df_40 = df[df["Q2"] >= 40]
print(df_40.head())
# df_40の行数
print(df_40.shape[0])

# 『列「Q1」が女』かつ『列「Q2」が30未満である』という条件に該当するデータのみを抽出
df_wman_30 = df[(df["Q1"] == "女") & (df["Q2"] < 30)]
print(df_wman_30.head())
# df_wman_30の行数
print(df_wman_30.shape[0])

# 列「Q4」の値が欠損値でない行のみを抽出
df_notnull = df[df["Q4"].notnull()]
print(df_notnull.head())
# df_notnullの行数
print(df_notnull.shape[0])

# 重複行を取り除いた表を新たに生成
df_nodup = df.drop_duplicates()
print(df_nodup.head())
# df_nodupの行数
print(df_nodup.shape[0])
