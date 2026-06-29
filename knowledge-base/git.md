更新文件流程

1.git add . 		#添加所有文件
2.git commit -m "添加学生管理系统脚本"  	#提交改动日志
3.git push 		#上传已添加的文件到库中

#### GitHub绑定全流程

1.创建文件夹,进入命令行

2.git init 		初始化Git库

3.在github上新建一个库,复制库的地址 git remote add origin "http....."

然后 git remote 检查绑定成功

4.git add . 	 将文件夹所有文件加到git暂存区

5.git commit -m "......." 第一次提交,生成快照版本 (已经提交过后会正常提交新变化)

6.git push -u origin main上传代码

7.git branch -m master main 更改分支名称