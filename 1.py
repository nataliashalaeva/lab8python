#Вариант 14. Найти количество магазинов, не являющихся супермаркетами. Указать их тип
import xmltodict
import re


def check_tags(check, dct_c):
    tag_shops = {}
    for ch in dct_c['osm'][check]:
        if 'tag' in ch:
            tags = ch['tag']
            if isinstance(tags, list):
                shop_type = None
                for tag in tags:
                    if tag['@k'] == 'shop':
                        shop_type = tag['@v']
                        break

                if shop_type and shop_type != 'supermarket':
                    for tagname in tags:
                        if tagname['@k'] == 'name':
                            if not tag_shops.get(shop_type):
                                tag_shops[shop_type] = 1
                            else:
                                tag_shops[shop_type] += 1
    return tag_shops


file = open(r'14 - 2.osm', 'r', encoding='utf-8')
text = file.read()
file.close()

dct = xmltodict.parse(text)
dct_shops1 = check_tags('way', dct)
dct_shops2 = check_tags('node', dct)
for k, v in dct_shops1.items():
    if k in dct_shops2:
        dct_shops2[k] += v
    else:
        dct_shops2[k] = v

print("Количество магазинов, не являющихся супермаркетами, и их типы:")
for shop_type, count in dct_shops2.items():
    print(f"{shop_type}: {count}")
