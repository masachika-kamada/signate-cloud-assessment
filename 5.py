import pandas as pd

df = pd.read_csv("社員名簿.csv", encoding="cp932")
print(df.head())

# 2つの列「姓」と「名」を連結した新たな列「氏名」を作成
df["氏名"] = df["姓"] + df["名"]

# 「氏名」におけるユニークな値の個数
print(df["氏名"].nunique())

# # 列「セイ」に含まれるすべての文字列を全角に統一
# df["セイ"] = df["セイ"].str.zenwidth()
# # 列「セイ」に含まれるユニークな値の個数
# print(df["セイ"].nunique())

# 列「first_name」の文字列をすべて小文字に
df["first_name"] = df["first_name"].str.lower()
# 列「first_name」に含まれるユニークな値の個数
print(df["first_name"].nunique())

# 列「名」のの丸括弧及び丸括弧に囲まれた文字列を全て取り除く
df["名"] = df["名"].str.replace(r"\(.*\)", "")
# 列「名」に含まれるユニークな値の個数
print(df["名"].nunique())

# 列「本社所在地」から郵便番号の先頭3桁のみを抽出した新たな列
df["郵便番号"] = df["住所"].str.extract(r"(\d{3})")
# 列「郵便番号」に含まれるユニークな値の個数
print(df["郵便番号"].nunique())