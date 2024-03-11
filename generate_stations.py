import glob
import os

def GetFileList(path, type, prefix = '', suffix = ''):
    '''
    receives: path string, type string, prefix string, suffix string
    returns: list of files in path with the given type, prefix and suffix
    '''
    files = glob.glob(f'{path}/{prefix}*{suffix}.{type}')
    return files if files else []

def DeleteFiles(path, type, prefix = '', suffix = ''):
    '''
    receives: path string, type string, prefix string, suffix string
    returns: None, deletes files from path with the given type, prefix and suffix
    '''
    for file in glob.glob(f'{path}/{prefix}*{suffix}.{type}'):
        os.remove(file)


def ProcessPnmlFile(template_path: str, names_to_replace: str|list) -> str:
    '''
    receives: template_path string, names_to_replace string or list
    returns: string, replaces %name and $name in the template file with the given names_to_replace
    '''
    if isinstance(names_to_replace, str):
        with open(template_path, 'r') as file:
            file_data = file.read()
            file_data = file_data.replace('%name0', names_to_replace)
            file_data = file_data.replace('$name0', names_to_replace.upper())
    elif isinstance(names_to_replace, list):
        with open(template_path, 'r') as file:
            file_data = file.read()
            for index,name in enumerate(names_to_replace):
                file_data = file_data.replace(f'%name{index}', name)
                file_data = file_data.replace(f'$name{index}', name.upper())
    else:
        raise ValueError('names_to_replace must be a string or a list')
    return file_data


def WriteFile(path, content):
    '''
    receives: path string, content string or list
    returns: None, writes the content to the file in the given path
    '''
    with open(path, 'w+') as file:
        if isinstance(content, list):
            content = '\n'.join(content) if '\n' not in content[0] else '\n'.join(content)
        file.write(content)


def ReadFile(path, type = 'list'):
    '''
    receives: path string, type string
    returns: string or list, reads the file in the given path
    '''
    with open(path, 'r') as file:
        content = file.read()
    return content if type == 'string' else content.splitlines()

# def GenerateCombinedStations(template_path: str, output_path: str, ind_list_0: list, ind_list_1: list) -> list:
#     '''
#     Receives:
#     template_path (str): The path to the template file.
#     output_path (str): The path where the output files will be written.
#     combine_list_1 (list): The first list of items to be combined.
#     combine_list_2 (list): The second list of items to be combined.
# 
#     Returns:
#     list: A list of strings, each string is a combination of an item from combine_list_1 and an item from combine_list_2.
# 
#     The function generates combined stations from the template file and the given lists and writes them to the output path.
#     '''
#     combine_list_0 = []
#     combine_list_1 = []
#     for item in ind_list_0:
#         combine_list_0.extend(GetFileList('src/stations/generated_stations/gfx', 'png', item))
#     for item in ind_list_1:
#         combine_list_1.extend(GetFileList('src/stations/generated_stations/gfx', 'png', item))
#     lang_list = []
#     #combine_list_0_original_name = [file.split('\\')[-1].split('.')[0] for file in combine_list_0 if 'snow' not in file.lower()]
#     #combine_list_1_original_name = [file.split('\\')[-1].split('.')[0] for file in combine_list_1 if 'snow' not in file.lower()]
#     combine_list_0_original_name = [file.split('\\')[-1].split('.')[0] for file in combine_list_0]
#     combine_list_1_original_name = [file.split('\\')[-1].split('.')[0] for file in combine_list_1]
#     for item0 in combine_list_0_original_name:
#         for item1 in combine_list_1_original_name:
#             WriteFile(f'{output_path}/{item0}_{item1}.pnml', ProcessPnmlFile(f'{template_path}/{item0.split("_")[0]}_{item1.split("_")[0]}.pnml.template', [item0, item1]))
#             item_combined_upper = f'STN_{item0.upper()}_{item1.upper()}'
#             item_combined_capitalized = f'{(" ".join(item0.split("_")[1:])+ " with " + " ".join(item1.split("_")[1:])).capitalize()}'
#             lang_list.append(f'{item_combined_upper:<64}:{item_combined_capitalized}')
#     return lang_list

def main():
    '''
    this is the main function, the codes are modified, for the original source code, please check ChinaSet: Platforms and Stations
    '''
    # delete the old files
    DeleteFiles('src/stations/generated_stations', 'pnml')
    DeleteFiles('src/stations/generated_stations', 'lng')

    files = GetFileList('src/stations/generated_stations/gfx', 'png')
    #files_original_name = [file.split('\\')[-1].split('.')[0] for file in files if 'snow' not in file.lower()]
    if os.name == 'nt': # why would windows do that???
        files_original_name = [file.split('\\')[-1].split('.')[0] for file in files]
    else:
        files_original_name = [file.split('/')[-1].split('.')[0] for file in files]
    for file in files_original_name:
        # create the new files
        file_data = ProcessPnmlFile(f'src/stations/generated_stations/templates/{file.split("_")[0]}.pnml.template', [file, file.split('_')[0]])
        WriteFile(f'src/stations/generated_stations/{file}.pnml', file_data)

    files_original_name_capitalized = [f'STN_{file.upper():<60}:{(" ".join(file.split("_")[1:])).capitalize()}' for file in files_original_name]
    # files_original_name_capitalized.extend(GenerateCombinedStations('src/stations/generated_stations/templates',
    #                                                     'src/stations/generated_stations',
    #                                                     ['st1'], ['dc1']))
    WriteFile('src/stations/generated_stations/stations.lng', files_original_name_capitalized)
    print('Stations generated')

if __name__ == "__main__":
    main()
