# 用批处理脚本批量新建文件夹，文件夹名带序号

想在本地批量新建一些带有规律命名的文件夹，手动创建后一个个重命名好麻烦。看看有什么快捷的办法偷懒。  

预期的文件名：`文字+数字序号`的形式。而序号前面需要**补零**。像这样：

![0](https://user-images.githubusercontent.com/45864744/147043892-ff60b390-29e7-4408-828e-f5408756e954.png)


## 批处理脚本：

create.bat
```
@echo off
setlocal EnableDelayedExpansion

for /L %%i in (1, 1, 20) do (
     set "zeropad=000%%i"
     md 文件夹!zeropad:~-2!
)
```
