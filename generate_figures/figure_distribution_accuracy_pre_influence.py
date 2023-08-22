import numpy as np
import pandas as pd

from generate_figures.figure_basics import histogram_plot


def figure_distribution_accuracy_pre_influence(
    filename: str = None, data_file: str = "data/clean.csv"
):
    """Plots the distribution of the collective accuracy prior to social influence and
    the cumulative line plot.

    Parameters
    ----------

    Returns
    -------
        Plot of the distribution of the collective accuracy prior to social
        influence and the cumulative line plot."""
    df = pd.read_csv(data_file)

    # Histogram
    histogram_plot(
        filename=filename,
        dataframe=df,
        y="collective_accuracy_pre_influence",
        title="Distribution of collective accuracy prior to influence",
        ylabel_left="number of occurrences",
        xlabel="collective accuracy",
        xlim=(0, 1),
        xticks=0.1 * np.arange(0, 11, 1, dtype=int),
        ylabel_right="cumulative probability",
        ylim=(0, 1),
    )


if __name__ == "__main__":
    figure_distribution_accuracy_pre_influence(data_file="../data/test.csv")
