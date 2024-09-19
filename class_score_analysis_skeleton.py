def read_data(filename):
    data = []
    with open(filename, "r") as fi:
        for index, line in enumerate(fi.readlines()):
            if index == 0 and line[0] == "#":
                continue

            data.append(list(map(int, line.split(","))))
    return data


def calc_weighted_average(data_2d, weight):
    average = []
    for data in data_2d:
        average.append(sum(data[i] * weight[i] for i in range(2)))
    return average


def analyze_data(data_1d):
    sorted_data = sorted(data_1d)
    mean = sum(data_1d) / len(data_1d)
    var = sum((data - mean) ** 2 for data in data_1d) / len(data_1d)
    median = (
        sorted_data[(len(sorted_data) - 1) // 2]
        if len(sorted_data) % 2 == 1
        else (
            sorted_data[len(sorted_data) / 2] + sorted_data[(len(sorted_data) / 2) + 1]
        )
        / 2  # also using code | sorted_data[len(sorted_data) // 2]
    )
    return mean, var, median, min(data_1d), max(data_1d)


if __name__ == "__main__":
    data = read_data(
        "data/class_score_en.csv"
    )  # You can change data/class_score_kr.csv
    if data and len(data[0]) == 2:  # Check 'data' is valid
        average = calc_weighted_average(data, [40 / 125, 60 / 100])

        with open("class_score_analysis.md", "w") as report:
            report.write("### Individual Score\n\n")
            report.write("| Midterm | Final | Average |\n")
            report.write("| ------- | ----- | ----- |\n")
            for (m_score, f_score), a_score in zip(data, average):
                report.write(f"| {m_score} | {f_score} | {a_score:.3f} |\n")
            report.write("\n\n\n")

            report.write("### Examination Analysis\n")
            data_columns = {
                "Midterm": [m_score for m_score, _ in data],
                "Final": [f_score for _, f_score in data],
                "Average": average,
            }
            for name, column in data_columns.items():
                mean, var, median, min_, max_ = analyze_data(column)
                report.write(f"* {name}\n")
                report.write(f"  * Mean: **{mean:.3f}**\n")
                report.write(f"  * Variance: {var:.3f}\n")
                report.write(f"  * Median: **{median:.3f}**\n")
                report.write(f"  * Min/Max: ({min_:.3f}, {max_:.3f})\n")
