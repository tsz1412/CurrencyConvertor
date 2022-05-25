def get_key(val, target_dict):
    for key, value in target_dict.items():
        if val == value:
            return key
    return False
