import time
import argparse
import os
from cpro import handlefilesystemevents
from watchdog.observers import Observer


def run_watch_dog():
    my_event_handler = handlefilesystemevents.HandleFilesystemEvent()
    path = "."
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)
    my_observer.start()
    while True:
        time.sleep(1)


def create_cmakelist_file(project_name :str):
    f = open("CMakeLists.txt","w")
    f.write('cmake_minimum_required(VERSION 3.11)\n')
    f.write('project('+project_name+')\n')
    f.write('include(CMAKE_FILES.txt)\n')
    f.write('add_executable('+project_name + ' $<TARGET_OBJECTS:PROJECT_FILES> )\n')
    f.close()
    f = open('src/cpro.cpp',"w")
    f.write('int cpro(int argc,char **argv){\n\treturn 0;\n}')
    f.close()
    f = open('CMAKE_FILES.txt','w')
    f.write('add_library(PROJECT_FILES OBJECT src/cpro.cpp)')
    f.close()
def create_project(project_name : str):
    os.mkdir('./src')
    os.mkdir('./header')
    os.mkdir('./test')
    create_cmakelist_file(project_name)

def handle_args(args):
    if args.project_name != 'cpro_empty':
        create_project(args.project_name)
    if args.watch == True:
        run_watch_dog()


def parse_command_line():
    parser = argparse.ArgumentParser(description='Create new C/C++ CMake project')
    parser.add_argument('--name', action='store', dest='project_name',default='cpro_empty')
    parser.add_argument('--watch', action='store_true', dest='watch', default='false')
    return parser.parse_args()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    handle_args(parse_command_line())

def run():
    handle_args(parse_command_line())