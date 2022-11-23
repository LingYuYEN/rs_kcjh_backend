import json
from pydantic import BaseModel
import os


class MemberModel(BaseModel):
    id: int
    account: str
    password: str
    priority: int


data = {
    "name": "Louis",
    "phone": "0988888888"
}


def write_jsonfile(json_str):
    ret = json.dumps(json_str)
    with open('jsonfile.json', 'w') as fp:
        fp.write(ret)


def load_jsonfile():
    with open('jsonfile.json', 'r') as fp:
        dict_data = json.load(fp)
        print(dict_data)
        print(type(dict_data))
        return dict_data


def delete_jsonfile():
    if os.path.exists('jsonfile.json'):
        os.remove('jsonfile.json')
    else:
        print('The file does not exist.')


write_jsonfile(data)
load_jsonfile()
delete_jsonfile()
# user_a = MemberModel(id=1, account='aaps', password='aaps', priority=1)
# # user_b = MemberModel(2, 'bbps', 'bbps', 1)
# # user_c = MemberModel(3, 'ccps', 'ccps', 1)
# # user_d = MemberModel(4, 'ddps', 'ddps', 1)
#
# # user_a = {'id': 1, 'account': 'aaps', 'password': 'aaps', 'priority': 1}
# user_array = [user_a]
#
# print(user_array)
