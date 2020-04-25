from os.path import isdir
from os import rename
import os
import json
from time import time

version = '0.01'

static_path = 'src/app/static'
templates_path = 'src/app/templates'

versioned_files = {}
changed_html_files = []

version_vendor = False
verbose = True
dry_run = False


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[1;34m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[0;31m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def change_files(path):
    if verbose:
        print('Looking in '+ path)

    # get all file names from current path
    file_names = os.listdir(path)
    # print(file_names)

    directories_names = []

    for file_name in file_names:
        # check if the current path is a directory
        if isdir(path + '/' + file_name) and (file_name != 'vendor' or version_vendor):
            directories_names.append(file_name)
            continue

        versioned_file_name = None
        if '.css' in file_name:
            versioned_file_name = file_name[:file_name.find('.css')] + '_v_' + version + '.css'
        elif '.js' in file_name:
            versioned_file_name = file_name[:file_name.find('.js')] + '_v_' + version + '.js'

        if versioned_file_name:
            if verbose:
                print('\tChanging '+ file_name+ ' to '+ versioned_file_name)
            if not dry_run:
                rename(path + '/' + file_name, path + '/' + versioned_file_name)
            versioned_files[file_name] = versioned_file_name

    if not directories_names:
        return
    else:
        for directory_name in directories_names:
            change_files(path + '/' + directory_name)


def change_html(path):
    if verbose:
        print('Looking in '+ path)

    # get all file names from current path
    file_names = os.listdir(path)

    directories_names = []
    for file_name in file_names:
        file_path = path + '/' + file_name
        # check if the current path is a directory
        if isdir(file_path):
            directories_names.append(file_name)
            continue

        if '.html' in file_name:
            if verbose:
                print("\tProcessing HTML file:" + bcolors.OKBLUE +  file_name + bcolors.ENDC)
            changed = False

            with open(file_path, 'r') as file:
                file_data = file.read()

            if file_data:
                for unversioned_file, versioned_file in versioned_files.items():
                    changed_data = file_data.replace(unversioned_file, versioned_file)
                    if changed_data != file_data:
                        if verbose:
                            print('\t\tReplacing data in current file: ' + unversioned_file + ' -> ' + versioned_file)
                        changed = True

                    file_data = changed_data
            else:
                print('No file data')
                exit()

            if changed:
                if not dry_run:
                    with open(file_path, 'w') as file:
                        file.write(file_data)
                changed_html_files.append(file_path)
            else:
                if verbose:
                    print('\t\tNo changes made')

    if not directories_names:
        return
    else:
        for directory_name in directories_names:
            change_html(path + '/' + directory_name)


if __name__ == '__main__':

    start_time = time()

    if os.name != 'posix':
        print("Incompatible OS")
        exit()


    try:
        os.listdir(static_path)
    except FileNotFoundError:
        print('Cannot find static files path')
        quit()
    except:
        print('Undefined error for static files path')
        quit()

    try:
        os.listdir(templates_path)
    except FileNotFoundError:
        print('Cannot find template files path')
        quit()
    except:
        print('Undefined error for template files path')
        quit()

    now = time()
    print("Changing CSS and JS...")
    change_files(static_path)
    if verbose:
        print('CSS and JS files changed: ')
        print(json.dumps(versioned_files, indent=4, sort_keys=True))
    print("Changed {} CSS and JS files in ".format(len(versioned_files)) + bcolors.HEADER + str(round(time() - now, 3)) +
          bcolors.ENDC + ' seconds\n')

    now = time()
    print("Changing HTML content...")
    change_html(templates_path)
    if verbose:
        print('HTML files changed: ')
        print(json.dumps(changed_html_files, indent=4, sort_keys=True))
    print("Changed {} HTML files in ".format(len(changed_html_files)) + bcolors.HEADER + str(round(time() - now, 3)) +
          bcolors.ENDC + ' seconds\n')

    print("Executed in " + bcolors.HEADER + str(round(time() - start_time, 2)) + bcolors.ENDC + ' seconds\n')