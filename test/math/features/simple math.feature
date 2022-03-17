# language: zh-CN
@math
功能: 数学计算
加法测试，剧本用法演示样例

  场景: 简单数学计算
    假如初始值设为1
    当现在再加1
    那么结果为2
  @fail
  场景: 错误数学计算
    假如初始值设为1
    当现在再加2
    那么结果为2

  @complex @math
  场景大纲: 混合场景
    假如初始值设为<var>
    当现在再加<increment>
    那么结果为<result>
    例子: 
      | var | increment | result |
      | 100 | 5         | 105    |
      | 102 | 3         | 105    |