## FigureMVC快速使用说明

---

### 前言

基于matplotlib及其他相关画图第三方库（如seaborn）作简单的包装，旨在借鉴MVC的部分设计思路整合常用的作图方法， 将作图过程抽象为，定制画板(Figure)和画笔(Axes)，操作画笔作草图，应用定制化模板(
Template)到草图，后续处理(图像的展示与保存)。

使用前，根据requirements.txt，安装所需全部库函数。

使用时，导入service下的FigureService类

```python
from service.FigureService import FigureService
```

作图时，创建好FigureService实例，准备作图数据，调用对应作图函数生成草图，配置对应模板成图，最后输出和保存图像。

### 一、定制画板(Figure)和画笔(Axes)

```python
from service.FigureService import FigureService

# 创建FigureService实例，FigureService会自动调用initFigure()，完成画板(Figure)和画笔(Axes)的初始化
figureService = FigureService(num=1, figsize=(10, 8))  # num为图编号，默认为1；figsize为画布大小

```

### 二、操作画笔作草图

```python
import numpy as np

# 数据预处理
x = np.linspace(-10, 10, 50)
y = 2 * x + 1

# 绘制图形
figureService.drawLine(x=x, y=y)
```

### 三、应用定制化模板(Template)到草图

```python
import numpy as np

# 使用模板
figureService.commonTemplate(xlim=(-1, 2),
                             ylim=(-2, 3),
                             xlabel="I am x",
                             ylabel="I am y",
                             xticks=np.linspace(-1, 2, 5),
                             yticks=[-2, -1.8, -1, 1.22, 3],
                             ytick_labels=[
                                 r'$really\ bad$', r'$bad$', r'$normal$',
                                 r'$good$', r'$really\ good$'
                             ],
                             tickFont=14,
                             showLegend=False)
```

### 四、后续处理(图像的展示与保存)

```python
from resources.configuration import PATH  # PATH为配置的工程目录下的默认文件保存路径

# 输出与保存(PDF)
figureService.figureShow()
figureService.figureSave(savePath=PATH.get("out/pdf"), saveName="simpleLine")
```


目前FigureService支持绘制线图、散点图、柱状图、箱线图、分布图和热力图等常用图像。
若想要拓展其他图像或者复杂的组合图像，仅需在service.FigureService中的Axes类中，编写自定义的方法即可，如：

```python
@classmethod
def function(cls, *args, **kwargs):
    try:
        drawing = """自定义方法主题"""
        cls.handles.append(drawing)
        return drawing
    except Exception as errMsg:
        raise BusinessException(EmBusinessError.MATPLOTLIB_AXES_FAIL, errMsg)

```



