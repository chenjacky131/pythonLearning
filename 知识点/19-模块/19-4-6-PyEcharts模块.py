"""
PyEcharts是百度开源的数据可视化库，它对流行图的
支持度比较高，它给用户提供了30多种图形，如柱形渐变图、
k线周期图等
文档地址    https://pyecharts.org/#/zh-cn/
"""
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker
c = (
    Pie()
    .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本实例"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("pip_base.html")
)
