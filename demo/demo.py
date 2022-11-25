import pandas as pd

df = pd.read_csv("デモ_注文履歴.csv", encoding="cp932")
print(df.head())

# コーヒーの平均単価
df_coffee = df[df["商品カテゴリ"] == "コーヒー"]
print("コーヒーの平均単価", df_coffee["単価"].mean())

# ブレンド茶飲料の平均注文数
df_tea = df[df["商品カテゴリ"] == "ブレンド茶飲料"]
print("ブレンド茶飲料の平均注文数", df_tea["注文数"].mean())

# 栄養ドリンク炭酸飲料の平均購入額
df_soda = df[df["商品カテゴリ"] == "栄養ドリンク炭酸飲料"]
print("栄養ドリンク炭酸飲料の平均購入額", df_soda["購入額"].mean())


def print_av_min_max(df, column):
    print(f"{column}の平均値", df[column].mean())
    print(f"{column}の最小値", df[column].min())
    print(f"{column}の最大値", df[column].max())


# 従業員数、単価、注文数、購入額
for column in ["従業員数", "単価", "注文数", "購入額"]:
    print_av_min_max(df, column)
