"""
@author: wanghongliang
@file: 01_study_lxml_字符串.py
@time: 2020/5/11 9:08 
"""
from lxml import etree


text = """<body>
		<b>加粗文本</b><br /><br />
		<i>斜体文本</i><br /><br />
		<code>电脑自动输出</code><br /><br />
		这是<sub>下标</sub>和<sup>上标</sup>
		
		
		<code>计算机输出</code>
		<br />
		<kbd>键盘输入</kbd>
		<br />
		<tt>打字机文本</tt>
		<br />
		<samp>计算机代码样本</samp>
		<br />
		<var>计算机变量</var>
		<br />
		
		<p>
		<b>注释：</b>这些标签常用于显示计算机/编程代码。
		</p>

	</body>
"""

html = etree.HTML(text)
result = etree.tostring(html,encoding='utf-8')  # 解析对象输出代码

print(type(html))

print(type(result))

print(result.decode('utf-8'))

