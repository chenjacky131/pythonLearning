"""
第三方库Pyinstaller可以在Windows操作系统中将Python
源文件打包成.exe的可执行文件。还可以在Linux和Mac OS
操作系统中对源文件进行打包操作。

注意事项：
在进行文件打包时，需要打包的文件尽量不要有中文，而且需要
打包的文件路径也尽量不要有中文，路径中包含中文有可能会导
致打包失败。
"""
# pyinstaller -F 模块路径 (-F在dist文件夹中只生成.exe可执行文件)
# 要打包的文件最后加一句input()防止程序执行完自动退出窗口(回车完才会退出)
# 会在当前目录下生成build和dist文件夹，可执行文件.exe位于dist文件夹中
