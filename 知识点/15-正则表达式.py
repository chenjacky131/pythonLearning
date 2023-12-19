"""
元字符  具有特殊意义的专用字符，例如^和$分别表示匹配的开始和结束
元字符  描述说明                   举例              结果
.      匹配任意字符（除\n）         'p\nytho\tn'     p、y、t、h、o、\t、n
\w     匹配字母、数字、下划线        'python\n123'    p、y、t、h、o、n、1、2、3
\W     匹配非字母、数字、下划线      'python\n123'    \n
\s     匹配任意空白字符            'python\t123'     \t
\S     匹配任意非空字符            'python\t123'     p、y、t、h、o、n、1、2、3
\d     匹配任意十进制数            'python\t123'     1、2、3

限定字符  描述说明                   举例            结果
?       匹配前面的字符0次或1次        'colou?r'      可以匹配color或colour
+       匹配前面的字符1次或多次       'colou+r'      可以匹配colour或colouu...r
*       匹配前面的字符0次或多次       'colou*r'      可以匹配color或colouu...r
{n}     匹配前面的字符n次            'colou{2}r     可以匹配colouur
{n,}    匹配前面的字符至少n次         'colou{2,}r    可以匹配colouur或colouu...r
{n,m}   匹配前面的字符至少n次，至多m次 'colou{2,4}r   可以匹配colouur或colouuur或colouuuur

其它字符          描述说明                           举例             结果
区间字符[]        匹配[]中所指定的字符                 [.?!]、[0-9]    匹配标点符号逗号、问号、感叹号，匹配数字0、1、2、3、4、5、6、7、8、9
排除字符^         匹配不存在[]中指定的字符              [^0-9]         匹配除0、1、2、3、4、5、6、7、8、9的字符
选择字符|         用于匹配|左右的任意字符               \d{18}|\d{15}  匹配15位数字或18位数字
转义字符          同python中的转义字符                \.             将.作为普通字符使用
[\u4e00-\u9fa5] 匹配任意一个汉字
分组()           改变限定符的作用                     six|fourth     匹配six或fourth
                                                  (six|four)th   匹配sixth或fourth
"""