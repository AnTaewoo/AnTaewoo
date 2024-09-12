import pandas as pd
from tabulate import tabulate


def normalize_data(n_cases, n_people, scale):
    norm_cases = []
    for idx, n in enumerate(n_cases):
        ratio = (n * scale) / n_people[idx]
        norm_cases.append(ratio)
    return norm_cases


regions = [
    "Seoul",
    "Gyeongi",
    "Busan",
    "Gyeongnam",
    "Incheon",
    "Gyeongbuk",
    "Daegu",
    "Chungnam",
    "Jeonnam",
    "Jeonbuk",
    "Chungbuk",
    "Gangwon",
    "Daejeon",
    "Gwangju",
    "Ulsan",
    "Jeju",
    "Sejong",
]
n_people = [
    9550227,
    13530519,
    3359527,
    3322373,
    2938429,
    2630254,
    2393626,
    2118183,
    1838353,
    1792476,
    1597179,
    1536270,
    1454679,
    1441970,
    1124459,
    675883,
    365309,
]  # 2021-08
n_covid = [
    644,
    529,
    38,
    29,
    148,
    28,
    41,
    62,
    23,
    27,
    27,
    33,
    16,
    40,
    20,
    5,
    4,
]  # 2021-09-21

sum_people = sum(n_people)
sum_covid = sum(n_covid)
norm_covid = normalize_data(
    n_covid, n_people, 1000000
)  # The new cases per 1 million people

# Print population by region
print("### Korean Population by Region")
print("* Total population:", sum_people)
print()  # Print an empty line
print("| Region | Population | Ratio (%) |")
print("| ------ | ---------- | --------- |")
for idx, pop in enumerate(n_people):
    ratio = norm_covid[idx]
    print("| %s | %d | %.1f |" % (regions[idx], pop, ratio))
print()

data = {
    "Region": regions,
    "Population": n_people,
    "Ratio (%, ppm)": norm_covid,
}
intro_p = f"""### Korean Population by Region

- Total population: {sum_people}

"""
info_table = f"""

> < covid19_statistics > table
"""

df = pd.DataFrame(data)
df["Ratio (%, ppm)"] = df["Ratio (%, ppm)"].round(1)

# 데이터프레임을 markdown 테이블로 변환하여 출력
md_table = tabulate(df, headers="keys", tablefmt="pipe")

with open("covid19_statistics.md", "w", encoding="utf-8") as f:
    f.write(intro_p)
    f.write(md_table)
    f.write(info_table)

print("Complete to Save covid19_statistics.md")
