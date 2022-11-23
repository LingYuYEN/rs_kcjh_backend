
import json
import os
# from send_email import test_send_mail

# dict_list = []
# repair_record_dict_list = []
jsonfile_name = "./jsonfile.json"
members_jsonfile = "./members.json"

# if the exe just in current dir
# print("abspath.: ", os.path.abspath("."))
# print("abspath..: ", os.path.abspath(".."))
# print("abspath./: ", os.path.abspath("./"))
# print("abspath../: ", os.path.abspath("../"))
# print(jsonfile_name, os.path.abspath(jsonfile_name))


def write_members_jsonfile(member_model_list):
    with open(members_jsonfile, 'w') as jsonfile:  # 如果沒有 json 檔案，就新增
        json_dic_list = []
        for member_model in member_model_list:
            json_dic_list.append(member_model.dict())

        json_object_list = json.dumps(json_dic_list, indent=4)
        jsonfile.write(json_object_list)
        return json_dic_list


def write_repair_info_jsonfile(repair_info_model_list):
    with open(jsonfile_name, 'w') as jsonfile:  # 如果沒有 json 檔案，就新增
        json_dic_list = []
        for repair_info_model in repair_info_model_list:
            json_dic_list.append(repair_info_model.dict())

        json_object_list = json.dumps(json_dic_list, indent=4)
        jsonfile.write(json_object_list)
        return json_dic_list


def load_members_jsonfile():
    if os.path.exists(members_jsonfile):
        with open(members_jsonfile, 'r') as jsonfile_list:
            dict_data_list = json.load(jsonfile_list)  # 轉換成 dic_list
            jsonfile_list.close()
            return dict_data_list
    else:
        return


def put_members_jsonfile(index, new_password):
    with open(members_jsonfile, 'r') as jsonfile_list:
        member_dict_list = json.load(jsonfile_list)  # 轉換成 dic_list
        member_dict_list[index - 1]["password"] = new_password

    with open(members_jsonfile, 'w') as jsonfile:  # 如果沒有 json 檔案，就新增
        json_object_list = json.dumps(member_dict_list, indent=4)
        jsonfile.seek(0)
        jsonfile.write(json_object_list)
        jsonfile.close()
        return member_dict_list[index - 1]

    #     jsonfile_list.seek(0)
    #     json_obj_list = json.dumps(member_dict_list, indent=4)  # 再將 dic_list 轉成 json
    #     jsonfile_list.write(json_obj_list)
    #     jsonfile_list.close()
    #     return member_dict_list[index - 1]


def write_jsonfile(dic):
    # global dict_list
    dict_list = []
    if os.path.exists(jsonfile_name):
        with open(jsonfile_name, 'r+') as jsonfile_list:  # 如果 json 檔案存在，就載入
            dict_list = json.load(jsonfile_list)  # 並轉換成 dic_list
            dict_list.append(dic)  # 將 dic append 到 dic_list
            jsonfile_list.seek(0)  # 指定光標位置，避免將 list 加到原本 jsonfile_list 後
            json_obj_list = json.dumps(dict_list, indent=4)  # 再將 dic_list 轉成 json
            jsonfile_list.write(json_obj_list)
            jsonfile_list.close()
    else:
        with open(jsonfile_name, 'w') as jsonfile:  # 如果沒有 json 檔案，就新增
            dict_list.append(dic)  # 先將 dict 加入陣列
            json_object_list = json.dumps(dict_list, indent=4)  # 再將 dict_list 轉成 json
            jsonfile.write(json_object_list)  # 並寫入
            jsonfile.close()


def load_jsonfile():
    if os.path.exists(jsonfile_name):
        with open(jsonfile_name, 'r') as jsonfile_list:
            dict_data_list = json.load(jsonfile_list)  # 轉換成 dic_list
            jsonfile_list.close()
            return dict_data_list
    else:
        return []


def put_jsonfile(index, dic):
    with open(jsonfile_name, 'r+') as jsonfile:  # 如果 json 檔案存在，就載入
        dict_list = json.load(jsonfile)
        repair_record_dict_list = dict_list[index - 1]['repair_record']

        if repair_record_dict_list is None:
            repair_record_len = 0
            repair_record_dict_list = []
        else:
            repair_record_len = len(repair_record_dict_list)

        dic['id'] = repair_record_len + 1
        repair_record_dict_list.append(dic)

        dict_list[index - 1]['repair_record'] = repair_record_dict_list
        # dict_list[index - 1]['status'] = '處理中'
        jsonfile.seek(0)
        json_obj_list = json.dumps(dict_list, indent=4)
        jsonfile.write(json_obj_list)  # 並寫入
        jsonfile.close()


def put_status_jsonfile(index, string):
    with open(jsonfile_name, 'r+') as jsonfile:
        dict_list = json.load(jsonfile)
        dict_list[index - 1]['status'] = string
        jsonfile.seek(0)
        json_obj_list = json.dumps(dict_list, indent=4)
        jsonfile.write(json_obj_list)  # 並寫入
        jsonfile.close()


def put_end_time_jsonfile(index, time_str):
    with open(jsonfile_name, 'r+') as jsonfile:
        dict_list = json.load(jsonfile)
        dict_list[index - 1]['end_time'] = time_str
        jsonfile.seek(0)
        json_obj_list = json.dumps(dict_list, indent=4)
        jsonfile.write(json_obj_list)  # 並寫入
        jsonfile.close()


def delete_jsonfile():
    if os.path.exists('jsonfile.json'):
        os.remove('jsonfile.json')
    else:
        print('The file does not exist.')

