
from utils import finding_ides, getting_json_from_web, key_in_list

link = "https://www.jsonkeeper.com/b/FGAS"

file = getting_json_from_web(link)
list_of_id = finding_ides(link)
for idefic in list_of_id:
    """находим инфо по каждому id"""
    for item in file:
        if len(item) != 0 and item['id'] == idefic:
            time_data = item['date'].split('T')
            date_ = time_data[0].split('-')
            normal_date = f"{date_[2]}.{date_[1]}.{date_[0]}"
            disc = item['description']
            abs_from = key_in_list('from', item)
            to = item['to'].split(' ')
            num_of_trans = to[1]
            summ = item["operationAmount"]["amount"]
            cur = item["operationAmount"]["currency"]["name"]
            """собираем оставшуюся необходимую информацию и делаем вывод транзакции"""
            print(f"""{normal_date} {disc}\n{abs_from}"""
                  f"""{to[0]} **{num_of_trans[-4:]}\n{summ} {cur}\n""")