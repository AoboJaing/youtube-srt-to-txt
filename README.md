# 按行读取文件（逐行读取） --- 按行写入文件（逐行写入） --- 实战：从字幕文件中提取字幕内容 --- Wait --- 2016年11月15日 星期二


---

使用的开发集成环境：PyCharm 2016.1.4
使用的Python的版本：python 2.7.10

---

## 知识点：Python 按行读取文件 



### 读取整个文件的内容

```python
f = open('filename.txt', 'r')
text = f.read()
f.close()

print text
```

### 读取一行的内容（按行读文件的内容）

参考网站：

Python逐行读取文件内容
http://www.cnblogs.com/sysuoyj/archive/2012/03/14/2395789.html


```python
f = open('filename.txt', 'r')

while 1:
	line = f.readline()
	if not line:
		break
	print text
	pass

f.close()
```

缺点：它依赖于前后文的关系，所以不能获取指定行的内容。

### 读取一行的内容 和 行号

参考网站：

python读取文件同时输出行号和内容
http://outofmemory.cn/code-snippet/3222/python-duqu-file-tongshi-output-xinghao-content

```python
f = open('filename.txt', 'r')
for (num,value) in enumerate(f):
	print "line number", num, "is:", value
f.close()
```

缺点：虽然这段代码可以获取到指定行的内容，但是，使用`enumerate()`函数获取指定行内容的代价是：需要对所有**行**依次进行编号，可想运算量之大。

### 读取指定行的内容

参考网站：

Python 从指定行读取数据 
http://blog.163.com/xiaowei_090513/blog/static/11771835920140251257802

```python
import linecache

num = 20
linecache.getline('filename.txt', num)
```

优点：读取的是缓存内的数据，速度快，并且代码简单。

---

## 知识点：Python 按行写入文件

参考网站：

Python文件读写
http://cxymrzero.github.io/blog/2015/03/19/python-file/
Python读写文件
http://blog.csdn.net/adupt/article/details/4435615

### 写一行（新建文件、替换现有文件）

```python
f = open('namefile.txt', 'w')
f.write('the first line: hello world in the new file.\n')
f.write('the sencond line: ')
f.write('this is also the second line.\n')
f.close()

f = open('namefile.txt', 'r')
text = f.read()
f.close()
print text
```

执行输出：

```
the first line: hello world in the new file.
the sencond line: this is also the second line.

```

`f = open('namefile.txt', 'w')`这段代码的执行：如果有这个`namefile.txt`文件，那就将现有的`namefile.txt`文件里面的内容全部自动清空；如果没有这个`namefile.txt`文件，那就自动新建一个`namefile.txt`文件。


### 写一行（在原有文件后面追加写入）

```python
f = open('namefile.txt', 'w+')
f.write('the last line: hello world in the new file.\n')
f.close()

f = open('namefile.txt', 'r')
text = f.read()
f.close()
print text
```

输出：

```
the first line: hello world in the new file.
the sencond line: this is also the second line.
the last line: hello world in the new file.

```

---

## 实战：从字幕文件中提取字幕内容

github源代码网址：https://github.com/AoboJaing/youtube-srt-to-txt

### 如何获取字幕文件

参考网站：https://www.youtube.com/watch?v=d9ctCc2AXCw

视频网站： https://www.youtube.com/

字幕提取网站：http://mo.dbxdb.com/setting.html

### 设计思路

输入是英文字幕文件和中文字幕文件，输出是英文配中文的txt文件

英文字幕文件

![Alt text](/img/1479414135007.png)

中文字幕文件

![Alt text](/img/1479414161811.png)

输出：英文配中文的txt文件

![Alt text](/img/1479414198952.png)


### 代码

```python
# coding : utf-8

import linecache

file_srt = open('Servos - working principle and homemade types.srt', 'r')
file_txt = open('newfile.txt', 'w')

cout=1
for (num, value) in enumerate(file_srt):
    if cout == 5:
        cout = 1
    if cout == 3:
        file_txt.write(linecache.getline('en-Servos - working principle and homemade types.srt', num+1))
        file_txt.write(value)
    cout += 1

file_srt.close()
file_txt.close()

```

### 运行输出

```
Youtube subtitles download by mo.dbxdb.com 
Youtube subtitles download by mo.dbxdb.com 
In this video I would like to explain the functionality of servos and how to convert conventional DC motors into homebuilt servos.
在这部影片中，我想解释一下舵机以及如何传统的直流电动机转换成自制伺服系统的功能。 
A servo is a device that produces motion accordant to a command signal from a control system.
伺服是，从一个控制系统产生运动一致来的命令信号的装置。 
Usually an electric motor is used to create a mechanical force and the servomechanism rotates at a velocity that approximates the command signal.
一般的电动机被用来创建一个机械力和伺服机构在近似于指令信号的速度旋转。 
...
...
```