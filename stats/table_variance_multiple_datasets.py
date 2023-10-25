import pandas as pd
import statsmodels.api as sm
from scripts.basic_functions import convert_list_to_rows, convert_math_to_text


def table_variance_multiple_datasets(
    data_file: str = ".../data/clean.csv",
    output_file: str = None,
    dependent_variable: str = "accuracy",
    independent_variables: list = None,
):
    # Initialize
    df = pd.read_csv(data_file)

    if independent_variables is None:
        rows: list = [
            "p_e + p_m",
            "E",
            "I_e",
            "E + I_e",
            "p_e + p_m + E",
            "p_e + p_m + I_e",
            "p_e + p_m + E + I_e",
        ]
    else:
        rows: list = convert_list_to_rows(independent_variables)
    table = pd.DataFrame(index=rows)

    # Setting variable range for subdata
    subdata_vars: dict = {
        "low": [0.55, 0.60],
        "med": [0.60, 0.65],
        "high": [0.65, 0.70],
    }

    # Analysis
    for subdata_key in subdata_vars.keys():
        competence_range = subdata_vars[subdata_key]
        df_sub = df.loc[
            (df["minority_competence"] > min(competence_range))
            & (df["minority_competence"] < max(competence_range))
            & (df["majority_competence"] > min(competence_range))
            & (df["majority_competence"] < max(competence_range))
        ]
        for row in rows:
            variables = convert_math_to_text(row, "list")
            Y = df_sub[dependent_variable]
            X = df_sub[variables]
            X = sm.add_constant(X)
            model = sm.OLS(Y, X).fit()
            table.loc[row, subdata_key] = round(model.rsquared, 3)

    if not output_file:
        return table
    else:
        table.to_csv(f"{output_file}.csv")


if __name__ == "__main__":
    table_variance_multiple_datasets(
        data_file="../data/clean.csv",
        output_file="../stats/table_multi",
        # dependent_variable="mean",
    )
