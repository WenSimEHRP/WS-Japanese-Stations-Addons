import glob
import subprocess
import os

# Change the current working directory to the script's directory
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
os.chdir(script_dir)

def DeleteFiles(path, type, prefix = '', suffix = ''):
    '''
    receives: path string, type string, prefix string, suffix string
    returns: None, deletes files from path with the given type, prefix and suffix
    '''
    for file in glob.glob(f'{path}/{prefix}*{suffix}.{type}'):
        os.remove(file)

def GetFileList(path, type, prefix = '', suffix = ''):
    '''
    receives: path string, type string, prefix string, suffix string
    returns: list of files in path with the given type, prefix and suffix
    '''
    files = glob.glob(f'{path}/{prefix}*{suffix}.{type}')
    return files if files else []

def main():
    DeleteFiles('.', 'pnml.template')
    files = GetFileList('.', 'index')
    for file in files:
        subprocess.run(['gcc', '-E', '-x', 'c', '-o', file.replace('.index',''), file])
    print('Templates generated')

if __name__ == '__main__':
    main()