# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2017/12/29  19:52
# @abstract    :

# 作者：知乎用户
# 链接：https://www.zhihu.com/question/38766472/answer/77988707
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class GenFunc:
    func_set = set([])
    def __init__(self, list_func):
        self.func_set = set(list_func)

    def method_missing(self, attr, *args, **kwargs):
        print (attr)

    def __getattr__(self, attr):
        if not (attr in self.func_set):
            raise Exception("no such method")
        def callable(*args, **kwargs):
            return self.method_missing(attr, *args, **kwargs)
        return callable


test = GenFunc(["funca", "funcb", "funcc"])
test.funca()
test.funcb()
test.funcc()
test.funcd()