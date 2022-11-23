import os


# jsonfile_name = "/root/fast_api_demo/jsonfile.json"
jsonfile_name = "./jsonfile.json"


def creat_jsonfile():
    if os.path.exists(jsonfile_name):
        return
    else:
        with open(jsonfile_name, 'w') as jsonfile:
            jsonfile.write("{}")
            jsonfile.close()


creat_jsonfile()
