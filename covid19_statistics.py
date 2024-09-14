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
    ratio = (pop * 100) / sum_people
    print("| %s | %d | %.1f |" % (regions[idx], pop, ratio))
print()


# Regions
data1 = {
    "Region": regions,
    "Population": n_people,
    "Ratio (%)": n_people,
}
intro_p1 = f"""### Korean Population by Region

- Total population: {sum_people}

"""
info_table1 = f"""

> table 1-1



"""

df1 = pd.DataFrame(data1)
df1["Ratio (%)"] = (df1["Ratio (%)"] * 100 / sum_people).map("{:.1f}".format)

# Regions by Covid
data2 = {
    "Region": regions,
    "New Cases": n_covid,
    "Ratio (%)": n_covid,
    "New Cases / 1M": norm_covid,
}
intro_p2 = f"""### Korean COVID-19 New Cases by Region

- Total new cases: {sum_covid}

"""
info_table2 = f"""

> table 1-2
"""

df2 = pd.DataFrame(data2)
df2["Ratio (%)"] = (df2["Ratio (%)"] * 100 / sum_covid).map("{:.1f}".format)
df2["New Cases / 1M"] = df2["New Cases / 1M"].map("{:.1f}".format)

# 데이터프레임을 markdown 테이블로 변환하여 출력
md_table1 = tabulate(df1, headers="keys", tablefmt="pipe")
md_table2 = tabulate(df2, headers="keys", tablefmt="pipe")

with open("covid19_statistics.md", "w", encoding="utf-8") as f:
    f.write(intro_p1)
    f.write(md_table1)
    f.write(info_table1)
    f.write(intro_p2)
    f.write(md_table2)
    f.write(info_table2)

print("Complete to Save covid19_statistics.md")
