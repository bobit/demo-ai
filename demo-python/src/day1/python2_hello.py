# 开发环境 python3.0 + idea

# Missing parentheses in call to 'print'
# Python2.X和Python3.X不兼容。安装的是Python3.X，但是试图运行如下Python2.X 的代码，会报如上错误。

# print "你好世界"; # Python3.X 源码文件默认使用utf-8编码，所以可以正常解析中文，无需指定 UTF-8 编码。
# print "hello word"; # python3.0版本,需要将print后面的语句加括号
# raw_input("按下 enter 键退出，其他任意键显示...\n") # python3.0版本,用input替换了raw_input