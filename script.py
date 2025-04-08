from frappe.geo.country_info import get_country_info


def get_country_phone_code(country='Egypt'):
    country_info = get_country_info(country)
    print(country_info)
    return country_info['isd']


print(get_country_phone_code('Egypt'))