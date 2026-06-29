import pandas as pd

df = pd.read_csv(
    r"C:\Users\gurka\OneDrive\Masaüstü\veri bilimi projesi\data\processed\iett_temiz.csv",
    usecols=["line_name", "number_of_passenger", "town"]
)

bk = df[df["town"].astype(str).str.upper().str.startswith("BAKIRKOY")]
result = (bk.groupby("line_name")["number_of_passenger"]
            .sum()
            .sort_values(ascending=False)
            .head(20))

print(f"Toplam BAKIRKOY kayit: {len(bk):,}")
print(f"Toplam BAKIRKOY yolcu: {bk['number_of_passenger'].sum():,}\n")
print(f"{'Sira':<5} {'Hat':<12} {'Toplam Yolcu':>15}  {'Kumulatif %':>12}")
print("-" * 52)
kum = 0
for i, (hat, val) in enumerate(result.items(), 1):
    kum += val
    print(f"{i:<5} {hat:<12} {val:>15,}  {kum/result.sum()*100:>11.1f}%")
