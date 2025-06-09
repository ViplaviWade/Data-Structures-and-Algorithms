
def merge_dicts(dict1, dict2):
    # result = dict1.copy()
    # for key in dict2:
    #     if key not in result:
    #         result[key] = dict2[key]
    # return result
    return {**dict1, **{k: v for k, v in dict2.items() if k not in dict1}}
