# 1. get list of all models/lookdevs
# 2. loop thru models and insert into template variantSet
# 3. write full variantSet list to model_variant_template and output. 
# variantSet "characterSets" = {"<model_id>" {over "body" (payload = @../../../TASKS/MODEL/char/<model_id>/asset/model.usda@){}}}
# this should work for all usda variants, not just models or skin. 
# maybe?  the model.usda creates the binding... eek

import os
from glob import glob

rootPath = "N:/working/characters/POC/"
modelPath = rootPath+"TASKS/MODEL/char/**/asset/"
skinpath = rootPath+"TASKS/LOOKDEV/char/skin/"
modelTemplate = rootPath+"templates/model_variants_template.usda"
skinTemplate = rootPath+"templates/skin_variants_template.usda"
model_varTemplate = '"<id>" {over "body" (reference = @../../../TASKS/MODEL/char/<id>/asset/model.usda@){}\n}'
skin_varTemplate = '"<id>" {over "Looks" (reference = @../../../TASKS/LOOKDEV/char/skin/<id>.usda@){}\n}'
destPath = rootPath+"PUBLISH/assets/char/"

models = [x.replace(os.sep, '/').split("/")[-3] for x in glob(modelPath+"/model.usda")]
skin_mtl = [x.replace(os.sep, '/').split("/")[-1].split(".")[0] for x in glob(skinpath+"/**.usda")]

def func(input_list, varToken, usdTemplate, fname):
    varList = []
    for each in input_list:
        varList.append(varToken.replace("<id>", each)+"\n")
    joinVarList = "".join(varList)
    with open(usdTemplate, 'r') as f:
        s = f.read()
    with open(destPath+fname+".usda", 'w') as f:
        s = s.replace("<variantSet>", joinVarList)
        f.write(s)

func(models, model_varTemplate, modelTemplate, "modelVariants_ref")

func(skin_mtl, skin_varTemplate, skinTemplate, "skinVariants_ref")