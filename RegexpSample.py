import re


class RegexpSample:
    originHtml = '<div class="design" id="leftcolumn">' \
                 '<a title="Python3教程" href="/python3/python3-tutorial.html" target="_top">Python3教程</a>' \
                 '<a title="Python3基础语法" href="python3-basic-syntax.html" target="_top">Python3基础语法</a>' \
                 '<a title="Python3基本数据类型" href="python3-data-type.html" target="_top">Python3基本数据类型</a>' \
                 '<a title="Python3解释器" href="/python3/python3-interpreter.html" target="_top">Python3解释器</a>' \
                 '</div>'
    originStr = "aaa,bbb,ccc,ddd,eee"

    def match(self):
        print("match 使用=====================================================")
        print("OriginStr Length:", len(self.originHtml))
        # Match对象是一次匹配的结果，包含了很多关于此次匹配的信息，可以使用Match提供的可读属性或方法来获取这些信息。
        m = re.match(r'.*?(<a.*?>.*?</a>).*?', self.originHtml, re.M | re.I)
        print("m.string:", m.string)
        print("m.re:", m.re)
        print("m.pos:", m.pos)
        print("m.endpos:", m.endpos)
        print("m.lastindex:", m.lastindex)
        print("m.lastgroup:", m.lastgroup)
        print("m.group(0,1):", m.group(0, 1))
        print("m.groups():", m.groups())
        print("m.groupdict():", m.groupdict())
        print("m.start(0):", m.start(0))
        print("m.end(1):", m.end(1))
        print("m.span(0):", m.span(0))
        print(r"m.expand(r'\1'):", m.expand(r'\1'))

    def split(self):
        print("\nsplit 使用：===========================================================")
        print("originStr: ",self.originStr)
        reSplit = re.split(",", self.originStr)
        print(reSplit)
        print("reSplit: ")
        for si in reSplit:
            print(si.strip())

    def findall(self):
        print("\nfindall 使用：===========================================================")
        print("originHtml",self.originHtml)
        reFindAll = re.findall("<a.*?>.*?</a>", self.originHtml, re.M)
        print(reFindAll)
        for fi in reFindAll:
            print(fi)
