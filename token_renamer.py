import os, filecmp
from glob import glob
import shutil

poc_path = "O:/Devs/SDG/POC/TASKS/MODEL/char/"
task_path = "O:/Devs/SDG/TASK/CHARACTERS/SPECIFICS/"
publish_path = "O:/Devs/SDG/PUBLISH/CHARACTERS/SPECIFICS/"
local_path = "N:/working/characters/POC/TASKS/MODEL/char/"


local_char_list = [x.replace(os.sep, '/')[:-1].split('/')[-1] for x in glob(f'{local_path}*/')]
poc_char_list = [x.replace(os.sep, '/')[:-1].split('/')[-1] for x in glob(f'{poc_path}*/')]
task_char_list = [x.replace(os.sep, '/')[:-1].split('/')[-1] for x in glob(f'{task_path}*/')]
# print(task_char_list)

ethnicity_set = set()
input = poc_char_list
input = task_char_list
input = local_char_list

for char in input:
    ethnicity = char.split('_')[1]
    ethnicity_set.add(ethnicity)
# print(ethnicity_set)


def token_rename(input, old, new, index, path):
    token = input.split('_')[index]
    if token == old:
        print(f'renaming {input} to {input.replace(token, new)}')
        os.rename(path+input, path+input.replace(token, new))
    else:
        print('nothing to do')

task_path = local_path
input_list = local_char_list
for char in input_list:
    token_rename(char, 'ca', 'cau', 1, task_path)
    token_rename(char, 'am', 'ame', 1, task_path)
    token_rename(char, 'af', 'afr', 1, task_path)
    token_rename(char, 'ai', 'ein', 1, task_path)
    token_rename(char, 'ei', 'ein', 1, task_path)
    token_rename(char, 'hi', 'ame', 1, task_path)
    token_rename(char, 'aa', 'aus', 1, task_path)
    token_rename(char, 'eu', 'cau', 1, task_path)
    token_rename(char, 'as', 'nea', 1, task_path)

    # token_rename(char, 'sch', 'sea', 1, task_path)

# for char in task_char_list:
#     token_rename(char, 'cau', 'ca', 1, task_path)
#     # token_rename(char, 'ame', 'am', 1, task_path)
#     token_rename(char, 'afr', 'af', 1, task_path)
#     # token_rename(char, 'ein', 'ai', 1, task_path)
#     token_rename(char, 'ein', 'ei', 1, task_path)
#     token_rename(char, 'ame', 'hi', 1, task_path)
#     token_rename(char, 'aus', 'aa', 1, task_path)
#     token_rename(char, 'cau', 'eu', 1, task_path)
#     token_rename(char, 'nea', 'as', 1, task_path)
#     token_rename(char, 'sch', 'pi', 1)