import pandas as pd

df = pd.read_csv("temper.csv", encoding="utf8")
df = df.rename(columns={'평균기온(°C)':'중간기온(°C)'})
df['중간기온(°C)'] = (df['최저기온(°C)'] + df['최고기온(°C)']) / 2
df.to_csv("temper-m.csv", index=False, encoding="utf8")
