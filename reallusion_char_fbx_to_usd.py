# USE IN OV


import os, shutil
from glob import glob
from pxr import Usd

import carb
import omni
import asyncio


async def convert_asset_to_usd(input_obj: str, output_usd: str):
    import omni.kit.asset_converter

    def progress_callback(progress, total_steps):
        pass

    converter_context = omni.kit.asset_converter.AssetConverterContext()
    # setup converter and flags
    # converter_context.ignore_material = False
    # converter_context.ignore_animation = False
    # converter_context.ignore_cameras = True
    # converter_context.single_mesh = True
    # converter_context.smooth_normals = True
    # converter_context.preview_surface = False
    # converter_context.support_point_instancer = False
    # converter_context.embed_mdl_in_usd = False
    # converter_context.use_meter_as_world_unit = True
    # converter_context.create_world_as_default_root_prim = False
    instance = omni.kit.asset_converter.get_instance()
    task = instance.create_converter_task(input_obj, output_usd, progress_callback, converter_context)
    success = await task.wait_until_finished()
    if not success:
        carb.log_error(task.get_status(), task.get_detailed_error())
    print("converting done")
    if os.path.isfile(output_usd):
        stage= Usd.Stage.Open(output_usd)
        print(f'{output_usd} exists. removing /World/Looks')
        stage.RemovePrim('/World/Looks')
        stage.Save()
        print(f'usda cleanup complete')
    else:
        print(f'{output_usd} DNE!')
    texture_path = f"{'/'.join(output_usd.split('/')[:-1])}/textures"
    print(texture_path)
    if os.path.exists(texture_path):
        shutil.rmtree(texture_path)
        print('textures removed')
    else:
        print('textures not found')
    print(f'{input_obj} COMPLETE')


path = "N:/working/characters/assets/char/ethnicPackExport/age10/"

char_paths = [x.replace(os.sep, '/') for x in glob(path+"*.fbx") if len(x.split('_')) == 5]
# char_paths = [x.replace(os.sep, '/') for x in glob(path+"*")]
# print(char_paths)
for char in char_paths:
    char_name = char.rstrip(".Fbx").split("/")[-1]
    print(char_name)
    usd_name = f'{path}{char_name}/{char_name}.usd'
    print(usd_name)
    usda_name = f'{path}{char_name}/asset/{char_name}.usda'
    print(usda_name)
    # print(path, char, name)
    asyncio.ensure_future(
        convert_asset_to_usd(
            char,
            usda_name,
        )
    )
print('export complete')



# # print(char_paths)