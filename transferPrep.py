import os
from glob import glob
import shutil
import time

source_path = "N:/working/characters/POC/TASKS/MODEL/char/**/asset/model.usda"
dest_path = "N:/working/characters/POC/TASKS/MODEL/unprocessed/"

models = [x.replace(os.sep, '/') for x in glob(source_path)]
models.sort(key=os.path.getmtime)
# for model in models: #[-7:]:
#     mtime = time.ctime(os.path.getmtime(model))
#     if mtime > time.time():
#         print(mtime)



# if not os.path.exists(dest_path):
#     os.mkdir(dest_path)
#     print("created dir:", dest_path)
# else:
#     print("dir exists")

models = models[-7:]
for model in models:
    newpath = dest_path+"/".join(model.split('/')[-3:-1])+"/"
    print("moving {0} to {1}".format(model, newpath))
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        print("created dir:", newpath)
    shutil.copy(model, newpath+"model.usda")
