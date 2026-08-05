import sys
import pandas as pd


def calculate_metrics(df, sufix, filter_instances=[]):
    if filter_instances:
        df = df[df["Instância"].isin(filter_instances)]

    df["Instance"] = df["Instância"].apply(lambda x: x.split("/")[-1])

    df_grouped = df[["Instance", "Melhor_Bound"]].groupby("Instance").min().reset_index()

    df_grouped.columns = ["Instance", f"B. Bound {sufix}"]

    df_grouped["T (s)"] = "Max"

    df_grouped["B. Int."] = "-"

    df_grouped["S. Int."] = "-"

    df_grouped = df_grouped[["Instance", "B. Int.", "S. Int.", "T (s)", f"B. Bound {sufix}"]]

    return df_grouped

def bold_best_results(df1, sufix):
    df1["B. Bound SEDC"] = df1[["B. Bound SEDC", f"B. Bound {sufix}"]].apply(lambda x: "\\textbf{" + str(x["B. Bound SEDC"]) + "}" if x["B. Bound SEDC"] >= x[f"B. Bound {sufix}"] else x["B. Bound SEDC"], axis=1)
    df1[f"B. Bound {sufix}"] = df1[["B. Bound SEDC", f"B. Bound {sufix}"]].apply(lambda x: "\\textbf{" + str(x[f"B. Bound {sufix}"]) + "}" if x["B. Bound SEDC"] < x[f"B. Bound {sufix}"] else x[f"B. Bound {sufix}"], axis=1)

    return df1


def main():
    raw_result_v1 = "/mnt/d/doutorado/cutset/results/no_ub/modelo_sedc_pattern_v1_harder_set_no_ub.txt"
    raw_result_v2 = "/mnt/d/doutorado/cutset/results/no_ub/modelo_sedc_pattern_v2_harder_set_ub.txt"
    raw_result_sedc = "/mnt/d/doutorado/cutset/results/outputs_seed_3600s/sem_suspeita_otimo_modelo_sedc_sem_heuristica_3600s.txt"

    dfv1 = pd.read_csv(raw_result_v1, sep=" ")
    dfv2 = pd.read_csv(raw_result_v2, sep=" ")
    dfsedc = pd.read_csv(raw_result_sedc, sep=" ")

    v1_results = calculate_metrics(dfv1, "V1")
    v2_results = calculate_metrics(dfv2, "V2")
    sedc_results = calculate_metrics(dfsedc, "SEDC")


    df_sedc_vs_v1 = sedc_results.merge(v1_results, on="Instance")

    df_sedc_vs_v2 = sedc_results.merge(v2_results, on="Instance")

    df_sedc_vs_v1 = bold_best_results(df_sedc_vs_v1, "V1")
    df_sedc_vs_v2 = bold_best_results(df_sedc_vs_v2, "V2")

    df_sedc_vs_v1.to_excel("/mnt/d/doutorado/cutset/results/no_ub/modelo_sedc_pattern_v1_harder_set.xlsx")
    df_sedc_vs_v2.to_excel("/mnt/d/doutorado/cutset/results/no_ub/modelo_sedc_pattern_v2_harder_set.xlsx")


if __name__ == "__main__":
    main()
