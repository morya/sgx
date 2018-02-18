# 安装

1. install phantomjs

不同的平台，需要安装不同的包，如果是mac系统，则选mac对应的包。
下面的指令是给linux64系统使用。

```
wget https://npm.taobao.org/mirrors/phantomjs/phantomjs-2.1.1-linux-x86_64.tar.bz2 ~/bin/
tar jxf ~/bin/phantomjs-2.1.1-linux-x86_64.tar.bz2
mv ~/bin/phantomjs-2.1.1-linux-x86_64/bin/phantomjs ~/bin/
export PATH=$HOME/bin:$PATH
```

确认，执行下面指令确认phantomjs正常工作。

```
phantomjs --version
```

# 测试 phantomjs

这一步比较耗时，我在macpro机器执行大约耗时2分钟才有结果。

```
phantomjs --load-images=no job.js
```

# 测试python脚本

待完成

```
python crawler.py -h
```

# 原理介绍

phantomjs 是一个无头浏览器模拟器，通过模拟访问网页，然后加载自行设定的js来解析出页面原先用javascript渲染出的元素。

通过 `job.js` 执行后，会把解析出的内容写入 `data.txt` 文件，再通过python脚本读取此文件，完成最终文件下载。

后续则需要改进 `crawler.py` 来调用 `phantomjs --load-images=no job.js` 并读取 data.txt ，下载文件。

## 注意事项

如果，单独执行 job.js 无反应，可以更改 `jquery.js` 使用其它cdn代替确认非baidu cdn读取失败。
