#### 1.查看当前有哪些环境(包括base)

```python
conda env list
# 查看列出当前所有环境,防止重名环境误用
# 不要在修改base包保持纯净
```

#### 2.创建新环境

```python
conda create --name name1
# 调用conda的create 命令 创建环境
# --name 给环境命名为name1
# --开头长选项 --name
# -开头短选项  -n
# 也可写为
conda create -n name1
# 则创建了一个空环境 名称为name1

conda remove --name my-env --all   
# 删除整个环境

conda craet -n my-env python=3.11
# 指定Python版本
#让conda在这个名为 my-env的环境里安装指定版本的python
#变体: python>=3.10 (至少为3.10) python^3.11(3.11.x但不升级到3.12)
#conda search python 产看可用版本

conda create --name my-env python=3.11 numpy pandas
#创建新环境时安装numpy 和 pandas 两个包
#可添加channel即为 -c conda-forge 指定从conda-forge下载包
#可在代码最后添加 -y 自动为所有回答yes

#可激活环境后安装包
conda install numpy pandas matplotlib
```

#### 3.激活环境

```python
conda activate my -env
# 激活环境,即可在环境选择中选择此环境
conda list
# 显示当前激活环境的包列表
```

#### 4.环境使用

```python
# 激活环境后即可使用
python
# 进入这个环境的python交互模式,可以直接写代码测试
python my_script.py
# 可以运行.py文件
# 关闭conda后环境取消激活状态但环境状态仍然存在

# 一般使用方法
# 打开vscode
# ctrl + shift + P
# 输入并选择：Python: Select Interpreter 找到并选择环境
# 选择后即可使用该环境不需要保持环境激活

```

#### 5.实例

```python
# 创建专门用于算法学习的干净环境（Python 3.9 + 常用库）
conda create -n algo_learning python=3.9 numpy pandas matplotlib jupyter
```

