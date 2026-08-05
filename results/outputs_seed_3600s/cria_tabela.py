import pandas as pd


def main():
    strategy_group = [
        [
            "./sem_suspeita_otimo_modelo_sedc_sem_heuristica_5400s.txt",
            # "./com_suspeita_otimo_modelo_sedc_sem_heuristica_3600s.txt",
            # "./sem_suspeita_otimo_modelo_sedc_sem_heuristica_3600s.txt"
        ],
        [
            "./sem_suspeita_otimo_modelo_sedc_pattern_v1_sem_heuristica_seed_v2_5400s.txt",
            # "./com_suspeita_otimo_modelo_sedc_pattern_v1_sem_heuristica_seed_v2_3600s.txt"
        ],
        # [
            # "./sem_suspeita_otimo_modelo_sedc_pattern_v2_sem_heuristica_seed_v2_5400s.txt",
            # "./com_suspeita_otimo_modelo_sedc_pattern_v2_sem_heuristica_seed_v2_3600s.txt"
        # ]
    ]



    strategy_prefix = [
        "SEDC + UB",
        "V1",
    ]

    group_all = True

    df_final = None
    for strategy, prefix in zip(strategy_group, strategy_prefix):
        columns_to_use = [
            f"Instance",
            f"Best Integer {prefix}",
            f"Solver Avg. Time {prefix}",
            f"Best Bound {prefix}",
        ]
        df_strategy = pd.DataFrame()
        for path in strategy:
            easy_instances = [
                "i080-044_sft",
                "i080-111_sft",
                "i080-143_sft",
                "i080-212_sft",
                "i080-213_sft",
                "i080-214_sft",
                "i080-215_sft",
                "i080-235_sft",
                "i080-241_sft",
                "i080-243_sft",
                "i080-244_sft",
                "i080-245_sft",
                "i080-312_sft",
                "i080-314_sft",
                "i080-315_sft",
                "i080-331_sft",
                "i080-342_sft",
                "i080-343_sft",
                "i080-344_sft",
                "i080-345_sft",
                "i160-033_sft",
                "i160-043_sft",
                "i160-045_sft",
                "i160-112_sft",
                "i160-115_sft",
                "i160-142_sft",
                "i160-144_sft",
                "i160-201_sft",
                "i160-211_sft",
                "i160-212_sft",
                "i160-213_sft",
                "i160-214_sft",
                "i160-215_sft",
                "i160-241_sft",
                "i160-242_sft",
                "i160-243_sft",
                "i160-244_sft",
                "i160-245_sft",
                "i160-305_sft",
                "i160-311_sft",
                "i160-312_sft",
                "i160-313_sft",
                "i160-314_sft",
                "i160-315_sft",
                "i160-322_sft",
                "i160-324_sft",
                "i160-325_sft",
                "i160-341_sft",
                "i160-342_sft",
                "i160-343_sft",
                "i160-344_sft",
                "i160-345_sft",
                "i320-011_sft",
                "i320-014_sft",
                "i320-015_sft",
                "i320-031_sft",
                "i320-032_sft",
                "i320-043_sft",
                "i320-111_sft",
                "i320-112_sft",
                "i320-113_sft",
                "i320-114_sft",
                "i320-115_sft",
                "i320-135_sft",
                "i320-141_sft",
                "i320-145_sft",
                "i320-211_sft",
                "i320-212_sft",
                "i320-213_sft",
                "i320-214_sft",
                "i320-215_sft",
                "i320-221_sft",
                "i320-222_sft",
                "i320-223_sft",
                "i320-224_sft",
                "i320-225_sft",
                "i320-241_sft",
                "i320-242_sft",
                "i320-243_sft",
                "i320-244_sft",
                "i320-245_sft",
                "i320-321_sft",
                "i320-322_sft",
                "i320-323_sft",
                "i320-324_sft",
                "i320-325_sft",
                "i320-341_sft",
                "i320-342_sft",
                "i320-343_sft",
                "i320-344_sft",
                "i320-345_sft",
                "i640-015_sft",
                "i640-022_sft",
                "i640-024_sft",
                "i640-042_sft",
                "i640-043_sft",
                "i640-044_sft",
                "i640-105_sft",
                "i640-111_sft",
                "i640-112_sft",
                "i640-113_sft",
                "i640-114_sft",
                "i640-115_sft",
                "i640-121_sft",
                "i640-122_sft",
                "i640-123_sft",
                "i640-124_sft",
                "i640-125_sft",
                "i640-132_sft",
                "i640-141_sft",
                "i640-142_sft",
                "i640-143_sft",
                "i640-144_sft",
                "i640-145_sft",
                "i640-211_sft",
                "i640-212_sft",
                "i640-213_sft",
                "i640-215_sft",
                "i640-221_sft",
                "i640-222_sft",
                "i640-223_sft",
                "i640-224_sft",
                "i640-225_sft",
                "i640-241_sft",
                "i640-242_sft",
                "i640-243_sft",
                "i640-244_sft",
                "i640-245_sft",
                "i640-321_sft",
                "i640-322_sft",
                "i640-323_sft",
                "i640-324_sft",
                "i640-325_sft",
                "i640-341_sft",
                "i640-342_sft",
                "i640-343_sft",
                "i640-344_sft",
                "i640-345_sft"
            ]

            df = pd.read_csv(path, sep=" ")

            df["solution_found"] = df["Best_Integer"].apply(lambda x: 1 if x < 1000000000 else 0)

            agg_dict = {
                "Best_Integer": ["min", "mean"],
                "solution_found": "sum",
                "Tempo_Solver": "mean",
                "#Nós": "mean",
                "LP": "mean",
                "Melhor_Bound": ["max", "mean"],
                "#Cortes": "mean"
            }
            df_grouped = df.groupby("Instância").agg(agg_dict).reset_index()
            column_names = [
                "Instance",
                f"Best Integer {prefix}",
                f"Avg. Integer {prefix}",
                f"Integer Found {prefix}",
                f"Solver Avg. Time {prefix}",
                f"Avg Opened Nodes {prefix}",
                f"LP {prefix}",
                f"Best Bound {prefix}",
                f"Avg Bound {prefix}",
                f"Avg Cuts {prefix}"
            ]

            df_grouped.columns = column_names

            df_grouped["Instance"] = df_grouped["Instance"].apply(lambda x: x.split("/")[-1])

            df_grouped = df_grouped[columns_to_use]
            # df_final = df_grouped[df_grouped.easy_instance == 0]

            # df_grouped["Best Integer"] = df_grouped["Best Integer"].apply(lambda x: x if x < 100000 else "-")

            if not group_all:
                df_final = df_grouped
                pure_path = path.replace(".txt", "")
                df_final.to_csv(f"{pure_path}.csv")

            if df_strategy.empty:
                df_strategy = df_grouped
            else:
                df_strategy = pd.concat([df_strategy, df_grouped])

        if df_final is None:
            df_final = df_strategy
        else:
            df_final = df_final.merge(df_strategy, on="Instance")


    if group_all:
        df_final.sort_values("Instance").to_latex("sedc_ub_vs_v1_5400s.tex", float_format="%.2f")
    print(df_final.head())


if __name__ == "__main__":
    main()
