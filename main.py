import numpy as np
from service.FigureService import FigureService
from resources.configuration import PATH

if __name__ == "__main__":
    # ----------------------------------------测试绘制直线-------------------------------------------

    def simpleLine():
        # 创建FigureService实例
        figureService = FigureService(num=1, figsize=(10, 8))

        # # 数据预处理
        x = np.linspace(-10, 10, 50)
        y = 2 * x + 1

        # 绘制图形
        figureService.drawLine(x=x, y=y)

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

        # 输出与保存(PDF)
        figureService.figureShow()
        figureService.figureSave(savePath=PATH.get("out/pdf"), saveName="simpleLine")


    simpleLine()


    # ----------------------------------------测试绘制散点图-------------------------------------------
    def simpleScatter():
        # 创建FigureService实例
        figureService = FigureService()

        # 数据预处理
        n = 1024  # data size
        x = np.random.normal(0, 1, n)
        y = np.random.normal(0, 1, n)
        T = np.arctan2(y, x)  # for color later on

        # 绘制图形
        figureService.drawScatter(x=x, y=y, s=75, c=T, alpha=0.5)

        # 使用模板
        figureService.commonTemplate(
            xlim=(-1.5, 1.5),
            ylim=(-1.5, 1.5),
            xticks=[],
            yticks=[],
            tickFont=14
        )

        # 输出与保存(PDF)
        figureService.figureShow()
        figureService.figureSave(savePath=PATH.get("out/pdf"), saveName="simpleScatter")


    simpleScatter()


    # ----------------------------------------测试绘制柱状图-------------------------------------------
    def simpleBar():
        # 创建FigureService实例
        figureService = FigureService()

        # 数据预处理
        n = 12
        x = np.arange(n)
        y1 = (1 - x / float(n)) * np.random.uniform(0.5, 1.0, n)
        y2 = (1 - x / float(n)) * np.random.uniform(0.5, 1.0, n)

        # 绘制图形
        figureService.drawBar(
            x=x,
            y=y1,
            ybias=0.05,
            facecolor='#9999ff',
            edgecolor='white',
        )
        figureService.drawBar(x=x,
                              y=-y2,
                              ybias=-0.05,
                              facecolor='#ff9999',
                              edgecolor='white',
                              va="top")

        # 使用模板
        figureService.commonTemplate(
            xlim=(-.5, 12),
            ylim=(-1.25, 1.25),
            xticks=[],
            yticks=[],
            tickFont=14
        )

        # 输出与保存(PDF)
        figureService.figureShow()
        figureService.figureSave(savePath=PATH.get("out/pdf"), saveName="simpleBar")


    simpleBar()


    # ----------------------------------------测试绘制箱线图-------------------------------------------
    def simpleBoxplot():
        # 创建FigureService实例
        figureService = FigureService()

        # 数据预处理
        np.random.seed(19680801)
        data = np.random.lognormal(size=(37, 4), mean=1.5, sigma=1.75)
        labels = list('ABCD')

        # 绘制图形
        figureService.drawBoxplot(x=data,
                                  labels=labels,
                                  showmeans=True,
                                  meanline=True,
                                  notch=True,
                                  bootstrap=10000,
                                  showfliers=False)

        # 使用模板
        figureService.commonTemplate(title="simple_boxplot", tickFont=14)

        # 输出与保存(PDF)
        figureService.figureShow()
        figureService.figureSave(savePath=PATH.get("out/pdf"), saveName="simpleBoxplot")


    simpleBoxplot()


    # ----------------------------------------测试绘制分布图-------------------------------------------
    def simpleHist():
        # 创建FigureService实例
        figureService = FigureService()

        # 数据预处理
        np.random.seed(19680801)
        mu = 100  # mean of distribution
        sigma = 15  # standard deviation of distribution
        x = mu + sigma * np.random.randn(437)
        num_bins = 50

        # 绘制图形
        figureService.drawHist(x=x, bins=num_bins)

        # 使用模板
        figureService.commonTemplate(
            xlabel="Smarts",
            ylabel="Probability density",
            title=r'Histogram of IQ: $\mu=100$, $\sigma=15$',
            tickFont=14
        )

        # 输出与保存(PDF)
        figureService.figureShow()
        figureService.figureSave(savePath=PATH.get("out/pdf"), saveName="simpleHist")


    simpleHist()


    # ----------------------------------------测试绘制热力图-------------------------------------------
    def simpleHeatmap():
        # 创建FigureService实例
        figureService = FigureService()

        # 数据预处理
        x = np.random.rand(16).reshape(4, 4)
        import pandas as pd
        attr = ['a', 'b', 'c', 'd']
        x = pd.DataFrame(x, columns=attr, index=attr)

        # 绘制图形, 使用模板
        figureService.drawHeatmap(x, vmin=0, vmax=1, center=0)

        # import seaborn as sns
        # sns.heatmap(x, vmin=0, vmax=1, center=0)

        # 输出与保存(PDF)
        figureService.figureShow()
        figureService.figureSave(savePath=PATH.get("out/pdf"), saveName="simpleHeatmap")


    simpleHeatmap()
    pass
