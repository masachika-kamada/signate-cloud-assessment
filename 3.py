import pandas as pd

df1 = pd.read_csv("来店履歴_1月.csv", encoding="cp932")
# df2 = pd.read_csv("来店履歴_2月.csv", encoding="cp932").T

# # df2を書き出し
# df2.to_csv("来店履歴_2月_T.csv", encoding="cp932", header=False, index=False)

df2 = pd.read_csv("来店履歴_2月_T.csv", encoding="cp932")

# df1とdf2を縦方向に連結
df = pd.concat([df1, df2], axis=0)
print(df.head())

# 列「お支払い額」の平均値
print("お支払い額の平均値", df["お支払い額"].mean())

df_new_customer = pd.read_csv("新規顧客.csv", encoding="cp932")
df_record = pd.read_csv("顧客別売上集計.csv", encoding="cp932")
print(df_new_customer.head())
print(df_record.head())

# df_new_customerとdf_recordを列「顧客ID」をキーとして内部結合
df_merge_inner = pd.merge(df_new_customer, df_record, on="顧客ID", how="inner")
print(df_merge_inner.head())
# 列「年間お支払い額」の平均値
print("年間お支払い額の平均値", df_merge_inner["年間お支払い額"].mean())

# df_new_customerとdf_recordを列「顧客ID」をキーとして左外部結合
df_merge_left = pd.merge(df_new_customer, df_record, on="顧客ID", how="left")
# 「年間お支払い額」の列が空欄(欠損値)となった箇所を、0で補間
df_merge_left["年間お支払い額"] = df_merge_left["年間お支払い額"].fillna(0)
# 列「年間お支払い額」の平均値
print("年間お支払い額の平均値", df_merge_left["年間お支払い額"].mean())

# df_recordを年間来店回数が多い順番に行を並び替え
df_record_sorted = df_record.sort_values("年間来店回数", ascending=False)
print(df_record_sorted.head())
# 先頭10行における列「年間来店回数」の平均値
print("年間来店回数の平均値", df_record_sorted["年間来店回数"].head(10).mean())
