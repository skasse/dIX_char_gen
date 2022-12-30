"""
compares local and network character directors for mismatched counts or missing folders
"""



import os, filecmp, time
from glob import glob
import shutil

start = time.time()
export_container_path = "N:/working/characters/assets/char/ethnicPackExport/age10/waiting for export/"
local_poc_path = "N:/working/characters/POC/TASKS/MODEL/char/"
# avatar_poc_path = "O:/Devs/SDG/POC/TASKS/MODEL/backup/char_2212161254/"
avatar_poc_path = "O:/Devs/SDG/POC/TASKS/MODEL/char/"
avatar_task_path = "O:/Devs/SDG/TASK/CHARACTERS/SPECIFICS/"
avatar_publish_path = "O:/Devs/SDG/PUBLISH/CHARACTERS/SPECIFICS/"

# avatar_poc_char_list = [x.replace(os.sep, '/')[:-1].split('/')[-1] for x in glob(f'{avatar_poc_path}*/')]
# avatar_task_char_list = [x.replace(os.sep, '/')[:-1].split('/')[-1] for x in glob(f'{avatar_task_path}*/')]

export_container_path_count = len(glob(f"{export_container_path}*/"))
local_poc_path_count = len(glob(f"{local_poc_path}*/"))
avatar_poc_path_count = len(glob(f"{avatar_poc_path}*/"))
avatar_task_path_count = len(glob(f"{avatar_task_path}*/"))
avatar_publish_path_count = len(glob(f"{avatar_publish_path}*/"))

print(f'there are {export_container_path_count:5} chars waiting to be exported')
print(f'there are {local_poc_path_count:5} chars in local_poc_path')
print(f'there are {avatar_poc_path_count:5} chars in avatar_poc_path')
print(f'there are {avatar_task_path_count:5} chars in avatar_task_path')
print(f'there are {avatar_publish_path_count:5} chars in avatar_publish_path')

result = filecmp.dircmp(export_container_path, local_poc_path)
print(f'{len(result.left_only)} character exports not yet in poc directory: ', result.left_only)

result = filecmp.dircmp(local_poc_path, avatar_task_path)
print(f'{len(result.left_only)} local characters not yet on server: ', result.left_only)

result = filecmp.dircmp(avatar_task_path, avatar_publish_path)
print(f'{len(result.left_only)} characters in TASK not yet published to mongoDB: ', result.left_only)
# print(result.left_only, len(result.left_only))
# print(result.right_only, len(result.right_only))

def dir_transfer(dirs:list, source_path, dest_path):
    if len(dirs) == 0:
        print('nothing to do')
    else:
        for count, dir in enumerate(dirs, 1):
            print(f'moving {count} of {len(dirs)}')
            print(f'copying {source_path+dir}/ to  {dest_path+dir}/')
            shutil.copytree(source_path+dir, dest_path+dir)
        print('complete')

# # transfer from TASK to POC
# dir_transfer(result.left_only, export_container_path, avatar_task_path)

end = time.time()
print(f'Seconds: {end-start}')