import sys
import os
import pandas as pd
import requests

UPLOAD_DIR = "local_uploads"

T_LEFT_MOST = "left_most"
T_NON_NUM = "left_most_non-numeric"

# The below two functions are copied from oeg-upm/ttla


def get_numerics_from_list(nums_str_list):
    """
    :param nums_str_list: list of string or numbers or a mix
    :return: list of numbers or None if less than 50% are numbers
    """
    nums = []
    for c in nums_str_list:
        n = get_num(c)
        if n is not None:
            nums.append(n)
    if len(nums) < len(nums_str_list)/2:
        return None
    return nums


def get_num(num_or_str):
    """
    :param num_or_str:
    :return: number or None if it is not a number
    """
    if pd.isna(num_or_str):
        return None
    elif isinstance(num_or_str, (int, float)):
        return num_or_str
    elif isinstance(num_or_str, basestring):
        if '.' in num_or_str or ',' in num_or_str or num_or_str.isdigit():
            try:
                return float(num_or_str.replace(',', ''))
            except Exception as e:
                return None
    return None


def spot_subject_column(fname, technique):
    fdir = os.path.join(UPLOAD_DIR, fname)
    col_id = -2
    if technique == T_LEFT_MOST:
        col_id = left_most(fdir)
    elif technique == T_NON_NUM:
        col_id = left_most_non_numeric(fdir)
    os.remove(fdir)
    return col_id


def left_most(fdir):
    return 0


def left_most_non_numeric(fdir):
    df = pd.read_csv(fdir)
    headers = df.columns.values
    # print("headers: ")
    # print(headers)
    for idx, col_name in enumerate(headers):
        # col = df.columns.values[col_name]
        col = df[col_name]
        col_list = col.tolist()
        nums = get_numerics_from_list(col_list)
        if nums is None:
            return idx
    return -1


if __name__ == "__main__":
    print(len(sys.argv))
    if len(sys.argv) == 4:
        _, fname, technique, callback_url = sys.argv
        col_id = spot_subject_column(fname=fname, technique=technique)
        reply = {
            "subject_col_id": col_id
        }
        r = requests.post(callback_url, data=reply)
        print("callback: %s, status: %d" % (callback_url, r.status_code))
