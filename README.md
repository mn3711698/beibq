# beibq

https://youapi.janedao.cn/  这是我部署好的，服务器是1C2G1M的云，
系统是freebsd,http服务器是nginx+apache24(python3.6+postgresql10)
国内下载代码请到码云 https://gitee.com/mn3711698/beibq
基于flask开发类似gitbook的知识管理网站。



因为很多博客系统都是以文章的形式为主；如果记录的文章变多了，还需要进行分类，
而且查找以前写过的某篇文章会比较麻烦。

beibq是用写书的方式来写博客，因为书籍本身就具有分类功能，
就算记录的内容变多了也不觉得乱，而且在阅读时通过点击书籍目录很方便的切换到其他章节。

beibq的编辑器支持Markdown，Markdown是一个标记语言，
只需要几个简单的标记符号就能转化成丰富的HTML格式，特别适合写博客。
关于Markdown的具体介绍：[Markdown 语法说明](https://www.appinn.com/markdown/)
beibq的编辑器界面简洁、操作简单，能够通过工具栏或快捷键方式输入Markdown标记符号，
有效的提高写作效率；编辑器的目录区支持章节拖拉，可以调整章节顺序。

更多信息请参考原作者的开源地址
原作者地址：码云地址：https://gitee.com/beibq/beibq 
            github地址：https://github.com/chaijunit/beibq


因为我平时用的是python3和postgresql，所以我将原项目改造成了我想要的。感谢原作者
因为我没有mysql数据的环境，所以第一步就修改数据库支持postgrsql.
然后再修改python2为python3

## 安装使用
![](https://github.com/mn3711698/beibq/blob/master/doc/image/start.png)
#### 1. 安装postgresql及依赖包
安装postgtesql数据库  https://www.postgresql.org/download/   
可以在这个链接下载安装及找到安装的说明文档
```
pip3 install -r requirements.txt
```

#### 2. 启动程序
```
python3 manage.py
```

#### 3. 配置站点
在浏览器中输入http://127.0.0.1:5000
第一次访问会跳转到配置界面，根据指示配置站点信息后就能使用beibq



## 建议反馈
如果您有任何建议和问题，可以通过邮箱方式和我联系

- 邮箱： 173782910@qq.com





