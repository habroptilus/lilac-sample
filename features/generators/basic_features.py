from lilac.features.features_base import FeaturesBase


class BasicFeatures(FeaturesBase):
    """train_dataのみから作れる基本的な特徴量セット."""

    def __init__(self, features_dir=None):
        super().__init__(features_dir)

    def _transform(self, df):
        df["strike2_fouls"] = df["totalPitchingCount"] - (df["B"]+df["S"]+1)
        df["SminusB"] = df["S"]-df["B"]
        df["S_B"] = df["S"].astype("str") + "_" + df["B"].astype("str")
        df["S_B_O"] = df["S"].astype(
            "str") + "_" + df["B"].astype("str") + "_"+df["O"].astype("str")
        df["runners"] = df["b1"].astype(
            "str") + "_" + df["b2"].astype("str") + "_"+df["b3"].astype("str")
        df["pit_bat_hand"] = df["pitcherHand"].astype(
            "str") + "_" + df["batterHand"].astype("str")
        df["inning_num"] = df["inning"].apply(lambda x: int(x[0]))
        df["top_bottom"] = df["inning"].apply(lambda x: x[-1])
        df["exist_runners"] = df["b1"] | df["b2"] | df["b3"]
        df["in_scoring_pos"] = df["b2"] | df["b3"]
        return_cols = ["strike2_fouls", "SminusB", "S_B", "S_B_O", "runners",
                       "pit_bat_hand", "inning_num", "top_bottom", "exist_runners", "in_scoring_pos"]
        return df[return_cols]
