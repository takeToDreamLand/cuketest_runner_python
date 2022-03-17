# -*- coding: UTF-8 -*-
import json
import os
from distutils.spawn import find_executable

def run(path, args=[], env={}):
    """Run cuketest project
    
    You can directly runing by pass the project path. Also running by specific arguments and enviroment.
    the avaliable arguments can be found in http://cuketest.com/zh-cn/execution/cli.html.
    
    Args: 
        path: String. Project path.
        args: Array<String>. Arguments for cuketest running. Like ["--format", "json", "--overwrite"].
        env: Dict<String, String>. A dictory that need to append to ENV.
    
    Returns: 
        The exitcode.
    """
    return _run(path, args, env, True)

def runDetach(path, args=[], env={}):
    return _run(path, args, env, False);

def _run(path, args, env, isWait=True):
    os.system('chcp 65001')
    run_env = _handle_run_env(env)
    run_args = _handle_run_args(args);
    flag = os.P_WAIT if isWait else os.P_NOWAIT
    child_info = 0;
    old_cwd = os.getcwd();
    os.chdir(path)  
    child_info = os.spawnve(flag, _get_cuke_excutable(), run_args, run_env)
    os.chdir(old_cwd)
    return child_info

def _get_cuke_excutable():
    return find_executable('cuke')

def _merge_two_dict(dict1, dict2):
    """Given two dicts, merge them into a new dict as a shallow copy."""
    dict_merged = dict1.copy()
    if(dict2):
        dict_merged.update(dict2)
    return dict_merged

def _handle_run_env(env):
    run_env = _merge_two_dict(os.environ, env)
    return run_env

def _handle_run_args(args):
    run_args = ['cuke', "--run"]
    for arg in args:
        run_args.append(json.dumps(arg))
    return run_args