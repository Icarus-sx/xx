#coding=utf-8
import re
print("#1、匹配一行文字中的所有开头的字母内容")
s="i love you not because of who you are,but because of who when i am with you"
content = re.findall(r"\b\w",s)
print(content)
#======================================================================================
print("#2、匹配一行文字中的所有开头的数字内容")
s = "i love you not because 12sd 34er 56df e4 54434"
content = re.findall(r"\b\d",s)
print(content)
#======================================================================================
print("#3、匹配一行文字的所有开头的数字内容或数字内容")
print(re.match(r"\w+","123sdf").group())
#======================================================================================
print("#4、只匹配包含字母和数字的行")
s="i love you not because\n12sd 34er 56\ndf e4 54434"
content = re.findall(r"\w+",s,re.M)
print(content)
#======================================================================================
print("#5、写一个正则表达式，使其能同时识别下面所有的字符串：'bat', 'bit', 'but', 'hat', 'hit', 'hut‘")
s="'bat','bit','but','hat','hit','hut'"
content= re.findall(r"..t",s)
print(content)
#======================================================================================
print("#6、匹配所有合法的python标识符")
s="awoeur awier !@# @#4_-asdf3$^&()+?><dfg$\n$"
content= re.findall(r".*",s,re.DOTALL)
print(s)
print(content)
#======================================================================================
print("#7、提取每行中完整的年月日和时间字段(注意格式）")
s= """se234 1987-02-09 07:30:00 
    1987-02-10 07:25:00"""
content=re.findall(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",s,re.M)
print(s)
print(content)
#======================================================================================
print("#8、将每行中的电子邮件地址替换为你自己的电子邮件地址")
s="""693152032@qq.com, werksdf@163.com, sdf@sina.com
    sfjsdf@139.com, soifsdfj@134.com
    pwoeir423@123.com"""
content=re.sub(r"\w+@\w+.com","xiaxiaoxu1987@163.com",s)
print(s)
print ("_______________________________________")
print(content)
#======================================================================================
print("#9、匹配\home关键字：")
re.findall(r"\\home","skjdfoijower \home \homewer")
print(re.findall(r"\\home","skjdfoijower \home \homewer"))
print("#1、使用正则提取出字符串中的单词")
s="""i love you not because of who 234 you are,234 but 3234ser because if who i am when i am with you"""
content=re.findall(r"\b[a-zA-Z]+\b",s)
print(content)
print("#2、使用正则表达式匹配合法的邮件地址：")
s = """xiasd@163.com, sdlfkj@.com sdflkj@180.com solodfdsf@123.com sdlfjxiaori@139.com saldkfj.com oisdfo@.sodf.com.com"""
content=re.findall(r"\w+@\w+.com",s)
print(content)

