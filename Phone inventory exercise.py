"""Phone inventory."""


def list_of_phones(all_phones: str) -> list:
    """
    Return list of phones.

    The input string contains of phone brands and models, separated by comma.
    Both the brand and the model do not contain spaces (both are one word).

    "Google Pixel,Honor Magic5,Google Pixel" => ["Google Pixel', 'Honor Magic5', 'Google Pixel"]
    """
    all_phones.split(",")
    if len(all_phones) == 0:
        return []
    else:
        return all_phones.split(",")

def phone_brands(all_phones: str) -> list:
    """
    Return list of unique phone brands.

    The order of the elements should be the same as in the input string (first appearance).

    "Google Pixel,Honor Magic5,Google Pixel" => ["Google", "Honor"]
    """
    found_companies = []
    companies = ["IPhone", "Google", "Honor", "Samsung", "HTC"]
    all_phones_list = all_phones.split(",")
    for i in all_phones_list:
        test = i.split(" ")
        if test[0] in companies:
            if test[0] not in found_companies:
                found_companies.append(test[0])
    if len(found_companies) == 0:
        return []
    else:
        return found_companies


def phone_models(all_phones: str) -> list:
    """
    Return list of unique phone models.

    The order of the elements should be the same as in the input string (first appearance).

    "Honor Magic5,Google Pixel,Honor Magic4" => ['Magic5', 'Pixel', 'Magic4']
    """
    found_models = []
    phone_models = all_phones.split(",")
    for i in phone_models:
        models_split = i.split(" ", 1)
        if models_split[-1] not in found_models:
            found_models.append(models_split[-1])
    return found_models


def search_by_brand(all_phones, brand) -> list:
    """Return list of all same brand phones."""
    list_of_same_brand_phones = []
    split_list = all_phones.split(",")
    for i in split_list:
        if brand.lower() in i.lower():
            list_of_same_brand_phones.append(i)
    return list_of_same_brand_phones


def search_by_model(all_phones, model) -> list:
    """Return list of all same model phones"""
    list_of_same_model_phones = []
    split_list = all_phones.split(",")
    for i in split_list:
        if (f" {model}").lower() in i.lower():
            list_of_same_model_phones.append(i)
    return list_of_same_model_phones



if __name__ == '__main__':
    print(list_of_phones("Google Pixel,Honor Magic5,Google Pixel"))  # ["Google Pixel', 'Honor Magic5', 'Google Pixel"]
    print(phone_brands("Google Pixel,Honor Magic5,Google Pix,Honor Magic6,IPhone 12,Samsung S10,Honor Magic,IPhone 11"))  # ['Google', 'Honor', 'IPhone', 'Samsung']
    print(phone_brands("Google Pixel,Google Pixel,Google Pixel,Google Pixel"))  # ['Google']
    print(phone_brands(""))  # []
    print(phone_models("IPhone 14,Google Pixel,Honor Magic5,IPhone 14"))  # ['14', 'Pixel', 'Magic5']
    print(phone_models("IPhone 14 A,Google Pixel B,Honor Magic5,IPhone 14"))  # ['14 A', 'Pixel B', 'Magic5', '14']

    # second part
    print(search_by_brand("IPhone X,IPhone 12 Pro,IPhone 14 pro Max", "iphone"))  # ['IPhone X', 'IPhone 12 Pro', 'IPhone 14 pro Max']
    print(search_by_model("IPhone proX,IPhone 12 Pro,IPhone 14 pro Max", "pro"))  # ['IPhone 12 Pro', 'IPhone 14 pro Max']
    print(search_by_model("IPhone proX,IPhone 12 Pro,IPhone 14 pro Max", "1"))  # []
    print(search_by_model("IPhone proX,IPhone 12 Pro,IPhone 14 pro Max", "IPhone"))  # []
    print(search_by_model("IPhone proX,IPhone 12 Pro,IPhone 14 pro Max", "12 Pro"))  # []