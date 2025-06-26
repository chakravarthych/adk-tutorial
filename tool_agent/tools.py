import polars as pl
from typing import Dict


def get_user_details(staff_id: str) -> Dict[str, str]:
    """
    Given a staff_id, returns a dictionary with the full name and role of the user.

    Parameters
    ----------
    staff_id : str
        The staff_id to search for

    Returns
    -------
    dict
        A dictionary with the keys "full_name", "role", and "status". If the user is found, the status is "success",
        otherwise it is "error" and an "error_message" key is included.
    """
    staff_df = (
        pl.scan_csv("../data/HealthCare_Gold_datasets/Hospital info/Staff.csv")
        .filter(pl.col("staff_id") == staff_id)
        .with_columns(full_name=pl.col("first_name") + " " + pl.col("last_name"))
        .collect()
    )
    if staff_df.shape[0] != 0:
        out_dict = {
            "full_name": staff_df["full_name"][0],
            "role": staff_df["role"][0],
            "status": "success",
        }
    else:
        out_dict = {"status": "error", "full_name": "not found", "role": "not found"}
    return out_dict
