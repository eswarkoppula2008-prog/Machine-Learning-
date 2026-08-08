import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_dataset():

    df = pd.read_csv("placement_predict_50k Dataset.csv")

    head = df.head().to_html(classes="table table-bordered")

    describe = df.describe().to_html(classes="table table-bordered")

    missing = df.isna().sum().to_frame("Missing Values").to_html(classes="table table-bordered")

    dtypes = df.dtypes.to_frame("Data Types").to_html(classes="table table-bordered")

    df['CGPA_Category'] = pd.cut(
        df['CGPA'],
        bins=[0,6,8,10],
        labels=['Low','Medium','High'],
        ordered=True
    )

    cgpa_category = df[['CGPA','CGPA_Category']].head().to_html(classes="table table-bordered")

    os.makedirs("static/graphs", exist_ok=True)

    plt.figure(figsize=(6,4))
    sns.histplot(df['CGPA'], kde=True)
    plt.title("CGPA Histogram")
    plt.savefig("static/graphs/histogram.png")
    plt.close()

    plt.figure(figsize=(6,4))
    sns.boxplot(x=df['CGPA'])
    plt.title("CGPA Boxplot")
    plt.savefig("static/graphs/boxplot.png")
    plt.close()

    plt.figure(figsize=(6,4))
    sns.scatterplot(
        x='CGPA',
        y='PlacementStatus',
        data=df
    )
    plt.title("CGPA vs Placement")
    plt.savefig("static/graphs/scatter.png")
    plt.close()

    plt.figure(figsize=(10,8))
    sns.heatmap(
        df.corr(numeric_only=True),
        annot=True
    )
    plt.title("Correlation Heatmap")
    plt.savefig("static/graphs/heatmap.png")
    plt.close()

    return {
        "head": head,
        "describe": describe,
        "missing": missing,
        "dtypes": dtypes,
        "cgpa": cgpa_category
    }