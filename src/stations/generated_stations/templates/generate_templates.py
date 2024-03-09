import glob
import subprocess
import os

# Change the current working directory to the script's directory
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
os.chdir(script_dir)

def GetFileList(path, type, prefix = '', suffix = ''):
    '''
    receives: path string, type string, prefix string, suffix string
    returns: list of files in path with the given type, prefix and suffix
    '''
    files = glob.glob(f'{path}/{prefix}*{suffix}.{type}')
    return files if files else []

def main():
    files = GetFileList('.', 'template', '_index')
    for file in files:
        subprocess.run(['gcc', '-E', '-x', 'c', '-o', file.replace('_index_',''), file])
    print('Templates generated')

if __name__ == '__main__':
    main()