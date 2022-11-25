import pandas as pd

df = pd.read_csv("顧客別集計結果.csv", encoding="cp932")
print(df.head())

# 「合計購入額」を列「合計注文数」で割ることで得られる列「注文単価」を作成
df["注文単価"] = df["合計購入額"] / df["合計注文数"]
print(df.head())

# 列「注文単価」の平均値
print(df["注文単価"].mean())

# 列「合計注文数」の値の大きさで順位付け
df["注文数順位"] = df["合計注文数"].rank(ascending=False)
print(df.head())

print(df["平均購入間隔日"].max())

# 列「平均購入間隔日」の値を3つのカテゴリ『4日未満』『4日以上6日未満』『6日以上』 にビニング
df["購入間隔"] = pd.cut(df["平均購入間隔日"], bins=[0, 4, 6, 100], labels=["4日未満", "4日以上6日未満", "6日以上"])
print(df.head())
# 購入間隔ごとの列「合計注文数」の平均値
print(df.groupby("購入間隔")["合計注文数"].mean())

# 10000以下を除いたデータの「合計購入額」の最小値を求める
purchase_min = df[df["合計購入額"] > 10000]["合計購入額"].min()
# 10000000以上を除いたデータの「合計購入額」の最大値を求める
purchase_max = df[df["合計購入額"] < 10000000]["合計購入額"].max()

# 列「合計購入額」が10000以下の値をpurchase_minに置換する
df["合計購入額"] = df["合計購入額"].replace(df[df["合計購入額"] <= 10000]["合計購入額"], purchase_min)
# 列「合計購入額」が10000000以上の値をpurchase_maxに置換する
df["合計購入額"] = df["合計購入額"].replace(df[df["合計購入額"] >= 10000000]["合計購入額"], purchase_max)
# 列「合計購入額」の平均値
print(df["合計購入額"].mean())
