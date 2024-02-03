## 环境搭建
### 1. 使用conda隔离环境并安装Cartopy
- `conda create -n env_cwr python=3.8  cartopy -c conda-forge --yes`
  - 注意python版本3.8及以上
### 2. 切换环境
- `conda activate env_cwr`
### 3. 配置镜像
- [参考](https://blog.csdn.net/JackyAce6880/article/details/129018819)
### 4. 安装依赖
- `pip install pycwr==0.3.6`
- `conda install pyqt=5`
### 5. 设置Python解释器
- Pycharm-Setting-Project-Python Interpreter-选择`env_cwr`
### 6. 运行
## 参考资料
1. [PyCWR](https://github.com/YvZheng/pycwr)
2. [PyCWR-文档](https://pycwr.readthedocs.io/en/latest/)
## PyCWR的插值库-RadarInterp
### 目前提供的插值方法
#### barnes
#### cressman

