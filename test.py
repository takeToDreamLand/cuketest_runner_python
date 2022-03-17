# -*- coding: UTF-8 -*-
from os.path import dirname,join
from cuketest_runner import run

# 假设默认参数如下
project_dir = join(dirname(__file__),'./test/math') # 目标项目路径
run(project_dir) # 指定项目可以直接运行，但不会生成报告，需要配置--format选项，如下

args = ["--format", "html"] # 运行配置，可以通过CukeTest运行配置快速生成
env = {"TEST_VERSION":"debug"} # 环境变量，为字典类型
run(project_dir, args, env)

# 可以追加运行配置
# 追加下面的配置使报告另外生成json格式的副本
args.extend(['--format', "json"])
run(project_dir, args, env)

# 追加下面的配置使得带`fail`标签的场景或步骤不执行
args.extend(['--tags', "not @fail"])
run(project_dir, args, env)

# 追加下面的配置录制运行过程
args.extend(['--video'])
run(project_dir, args, env)