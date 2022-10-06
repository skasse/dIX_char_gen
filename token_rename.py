import os
import shutil
from glob import glob


path_source = "N:/working/characters/POC/TASKS/MODEL/char/*"

model_paths = [x.replace(os.sep, '/') for x in glob(path_source, recursive=False)]
# print(model_paths)
model_names = [x.split('/')[-1] for x in model_paths]
# print(model_names)
model_tokens = [x.split('_') for x in model_names]
genetic_tokens = set()
for token in model_tokens:
    genetic_tokens.add(token[1]) # {'eu', 'af', 'hi', 'ei', 'aa', 'ai', 'as'}

# {'eu', 'af', 'hi', 'ei', 'aa', 'ai', 'as'}

genetic_tokens = {'eu':'ca', 'af':'af', 'hi':'am', 'ei':'ca', 'aa':'oc', 'ai':'am', 'as':'as'}
for token in model_tokens:
    if token[1] in genetic_tokens:
        token[1] = genetic_tokens[token[1]]

model_names_mod = ['_'.join(x) for x in model_tokens]

for i in range(0, len(model_names)):
    print("{0} changed to {1}".format(path_source[:-1]+model_names[i], path_source[:-1]+model_names_mod[i]))

# for name in model_names_mod:
#     print(path_source[:-1]+name)