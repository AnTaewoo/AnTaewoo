import matplotlib.pyplot as plt


def read_data(filename):
    data = []
    with open(filename, "r") as f:
        for line in f.readlines():
            if not line.startswith("#"):  # If 'line' is not a header
                data.append([int(word) for word in line.split(",")])
    return data


if __name__ == "__main__":
    # Load score data
    class_kr = read_data("data/class_score_kr.csv")
    class_en = read_data("data/class_score_en.csv")

    # TODO) Prepare midterm, final, and total scores
    midterm_kr, final_kr = zip(*class_kr)
    total_kr = [40 / 125 * midterm + 60 / 100 * final for (midterm, final) in class_kr]
    midterm_en, final_en = zip(*class_en)
    total_en = [40 / 125 * midterm + 60 / 100 * final for (midterm, final) in class_en]

    # TODO) Plot midterm/final scores as points
    plt.plot(midterm_kr, final_kr, "rs", midterm_en, final_en, "b^")
    plt.xlabel("Midterm", labelpad=10)
    plt.ylabel("Final", labelpad=10)
    plt.legend(["Korean", "English"])
    plt.title("Midterm and Final Exam Visualization using Scatter Plot")
    plt.xlim([0, 125])
    plt.ylim([0, 100])
    plt.grid(True)
    plt.savefig("Midterm_Final_Score_Scatter.png")

    # TODO) Plot total scores as a histogram
    plt.figure()
    plt.hist(total_kr, range=(0, 100), bins=20, alpha=0.5, label="Korean")
    plt.hist(total_en, range=(0, 100), bins=20, alpha=0.5, label="English")
    plt.xlabel("Total Score", labelpad=10)
    plt.ylabel("The number of students", labelpad=10)
    plt.legend(["Korean", "English"])
    plt.title("Midterm and Final Exam Visualization using Histogram")
    plt.xlim([0, 100])
    plt.savefig("Midterm_Final_Score_Histogram.png")
