import pandas as pd

df = pd.read_csv("売上履歴_202101.csv", encoding="cp932")
print(df.head())

# 受注金額の合計値
print("受注金額の合計値", df["受注金額"].sum())

# 受注金額の平均値
print("受注金額の平均値", df["受注金額"].mean())

# 受注金額の最大値
print("受注金額の最大値", df["受注金額"].max())

# 受注金額の中央値
print("受注金額の中央値", df["受注金額"].median())

# 受注金額の標準偏差(標本分散の平方根)
print("受注金額の標準偏差", df["受注金額"].std())

# 列「商品ID」のユニークな値の個数
print("商品IDのユニークな値の個数", df["商品ID"].nunique())

# 列「受注金額」と列「担当所要工数」の相関係数
print("受注金額と担当所要工数の相関係数", df["受注金額"].corr(df["担当所要工数"]))

# df2 = pd.read_csv("担当社員別_売上集計.csv", encoding="cp932")
# # df2をutf-8で書き出し
# df2.to_csv("担当社員別_売上集計_utf8.csv", encoding="utf-8")

# 社員IDが10194の担当件数
print("社員IDが10194の担当件数", df[df["社員ID"] == 10194].shape[0])

# 社員IDが10349の平均所要工数
print("社員IDが10349の平均所要工数", df[df["社員ID"] == 10349]["担当所要工数"].mean())

# 社員IDが10458の合計受注金額
print("社員IDが10458の合計受注金額", df[df["社員ID"] == 10458]["受注金額"].sum())
