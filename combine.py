import glob
import os

def read_indexes(path: str, filetype = 'pnml') -> list[str]:
    return glob.glob(path + '/**/*.' + filetype, recursive=True)

'''def read_file(path: str) -> list[str]:
    with open(path, 'r') as file:
        return file.readlines()'''

def write_file(path: str, data: list[str]) -> None:
    with open(path, 'w+') as file:
        file.writelines(data)

def main():
    if os.name == 'nt':
        indexes = read_indexes('src\stations')
    else:
        indexes = read_indexes('src/stations')
    # output_data = read_file('wins.pnml')
    output_data = []
    for index in indexes:
        output_data.append(f'#include "{index}"\n')
    write_file('indexes.pnml', output_data)
    print('Indexes generated')

if __name__ == '__main__':
    main()