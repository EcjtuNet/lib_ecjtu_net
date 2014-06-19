日新校图书馆辅助
====
抓取校图书馆数据，重新展示

主要功能：

 - 更友好的搜索
 - 到期提醒
 - 自动续借
 - 借书、欠款等查询

安装
----
	pip install -r `requirement.txt`
另需MySQL

启动
----
	gunicorn -b 0.0.0.0:4000 app:app