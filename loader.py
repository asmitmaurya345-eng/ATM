import json
with open ("database.json","w") as database:
        full_info={"123456":{"name":"Asmit Maurya","pin":1234,"balance":1000,"history":{"2026-04-26":1000}}}
        json.dump(full_info,database,indent=4)
        print("Your account have been created sucessfully>")
        database.close()