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
            file_data = file_data.replace('%name', names_to_replace)
            file_data = file_data.replace('$name', names_to_replace.upper())
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



def main():
    '''
    this is the main function, the codes are modified, for the original source code, please check ChinaSet: Platforms and Stations
    '''
    # delete the old files
    DeleteFiles('src/stations/generated_stations', 'pnml')
    DeleteFiles('src/stations/generated_stations', 'lng')

    files = GetFileList('src/stations/generated_stations/gfx', 'png')
    files_original_name = [file.split('\\')[-1].split('.')[0] for file in files]
    files_original_name_capitalized = [f'STN_{file.upper():<36}:{(" ".join(file.split("_")[1:])).capitalize()}' for file in files_original_name]

    for file in files_original_name:
        # create the new files
        file_data = ProcessPnmlFile(f'src/stations/generated_stations/templates/{file.split("_")[0]}.pnml.template', file)
        WriteFile(f'src/stations/generated_stations/{file}.pnml', file_data)

    WriteFile('src/stations/generated_stations/stations.lng', files_original_name_capitalized)

if __name__ == "__main__":
    main()
