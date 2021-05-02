import matplotlib.pyplot as plt
import numpy as np
from resources.configuration import PATH

from error.BusinessException import BusinessException
from error.EmBusinessError import EmBusinessError


class Axes:

    @classmethod
    def drawLine(cls, x, y, **kwargs):
        try:
            line, = cls.axes.plot(x,
                                  y,
                                  c=kwargs.get('color'),
                                  marker=kwargs.get('marker'),
                                  markersize=kwargs.get('markersize', 4),
                                  markerfacecolor=kwargs.get('markerfacecolor'),
                                  alpha=kwargs.get('alpha', 1),
                                  linewidth=kwargs.get('linewidth', 2),
                                  linestyle=kwargs.get("linestyle", 'dashed'),
                                  label=kwargs.get('label'),
                                  )
            cls.handles.append(line)
            return line
        except Exception as errMsg:
            raise BusinessException(EmBusinessError.FIGURE_AXES_FAIL, errMsg)

    @classmethod
    def drawScatter(cls, x, y, **kwargs):
        try:
            scatter = cls.axes.scatter(x,
                                       y,
                                       c=kwargs.get("color"),
                                       s=kwargs.get("size"),
                                       alpha=kwargs.get("alpha"),
                                       label=kwargs.get("label"),
                                       marker=kwargs.get('marker'),
                                       )
            cls.handles.append(scatter)
            return scatter
        except Exception as errMsg:
            raise BusinessException(EmBusinessError.FIGURE_AXES_FAIL, errMsg)

    @classmethod
    def drawBar(cls, x, y, **kwargs):
        try:
            bar = cls.axes.bar(x,
                               y,
                               width=kwargs.get("width", 0.8),
                               color=kwargs.get("color"),
                               facecolor=kwargs.get("facecolor"),
                               edgecolor=kwargs.get("edgecolor"),
                               alpha=kwargs.get("alpha", 0.5),
                               label=kwargs.get("label"))
            cls.handles.append(bar)
            return bar
        except Exception as errMsg:
            raise BusinessException(EmBusinessError.FIGURE_AXES_FAIL, errMsg)

    @classmethod
    def drawHist(cls, x, bins, **kwargs):
        try:
            n, bins, patches = cls.axes.hist(
                x=x,
                bins=bins,
                range=kwargs.get("range"),
                density=kwargs.get("density", False),
                histtype=kwargs.get("histtype", "bar"),
                cumulative=kwargs.get("cumulative"),
                label=kwargs.get("label"),
                edgecolor=kwargs.get("edgecolor", "black"),
                color=kwargs.get("color", "blue"),
                alpha=kwargs.get("alpah", 0.4)
            )
            # cls.handles.append((n, bins, patches))
            return n, bins, patches
        except Exception as errMsg:
            raise BusinessException(EmBusinessError.FIGURE_AXES_FAIL, errMsg)

    @classmethod
    def drawBoxplot(cls, x, **kwargs):
        try:
            bp = cls.axes.boxplot(
                x,
                labels=kwargs.get("labels"),
                showmeans=kwargs.get("showmeans"),
                meanline=kwargs.get("meanline"),
                showbox=kwargs.get("showbox", True),
                showcaps=kwargs.get("showcaps", True),
                notch=kwargs.get("notch"),
                bootstrap=kwargs.get("bootstrap"),
                showfliers=kwargs.get("showfliers", True),
                boxprops=kwargs.get("boxprops"),
                flierprops=kwargs.get("flierprops"),
                medianprops=kwargs.get("medianprops"),
                meanprops=kwargs.get("meanpointprops",
                                     kwargs.get("meanlineprops")),
            )
            cls.handles.append(bp)
            return bp
        except Exception as errMsg:
            raise BusinessException(EmBusinessError.FIGURE_AXES_FAIL, errMsg)

    @classmethod
    def drawArrow(cls, start, end, **kwargs):
        """
            箭头起始位置（A[0],A[1]）和向量（B[0],B[1]）
            length_includes_head = True:表示增加的长度包含箭头部分
            head_width:箭头的宽度
            head_length:箭头的长度
            fc:filling color(箭头填充的颜色)
            ec:edge color(边框颜色)
            arrowtype: "simple", "->"
        """
        try:
            from matplotlib.pyplot import gca

            arrowstyle = '{2},head_width={0},head_length={1}'.format(kwargs.get('head_width', 0.75),
                                                                     kwargs.get('head_length', 0.75),
                                                                     kwargs.get("arrow_type", "->"))
            if kwargs.get("tail_width"):
                arrowstyle += ",tail_width={0}".format(kwargs.get("tail_width", 0.4))

            opt = dict(color=kwargs.get('color', 'red'), alpha=kwargs.get("alpha"),
                       arrowstyle=arrowstyle, connectionstyle='arc3,rad=0', fc=kwargs.get("fc"))
            arrow = gca().annotate(kwargs.get("annotate", ""), xy=end, xycoords='data', xytext=start, textcoords='data',
                                   arrowprops=opt, )
            cls.handles.append(arrow)
            return arrow
        except Exception as errMsg:
            raise BusinessException(EmBusinessError.FIGURE_AXES_FAIL, errMsg)

    @staticmethod
    def drawHeatmap(df, **kwargs):
        try:
            import seaborn as sns
            heatmap = sns.heatmap(df,
                                  annot=kwargs.get('annot', True),
                                  annot_kws={'family': 'Times New Roman', 'weight': 'normal',
                                             'size': kwargs.get('annot_size', 12)},
                                  vmin=kwargs.get("vmin"),
                                  vmax=kwargs.get("vmax"),
                                  square=kwargs.get("square", True),
                                  linewidths=kwargs.get("linewidths", 0.05),
                                  cmap=kwargs.get('cmap', 'YlGnBu'),
                                  xticklabels=kwargs.get("xticklabels", True),
                                  cbar=kwargs.get('cbar', False),
                                  fmt='.{0}g'.format(kwargs.get("annotDigit", 3)),
                                  )

            if not kwargs.get('cbar', False):
                cb = heatmap.figure.colorbar(heatmap.collections[0])  # 显示colorbar
                cb.ax.tick_params(labelsize=kwargs.get("labelsize", 12))  # 设置colorbar刻度字体大小。
                if kwargs.get("cbar_label"):
                    font = {'family': 'Times New Roman',
                            'weight': 'normal',
                            'size': kwargs.get("cbar_label_font", 16),
                            }
                    cb.set_label(kwargs.get("cbar_label"), fontdict=font)
        except Exception as errMsg:
            raise BusinessException(EmBusinessError.FIGURE_AXES_FAIL, errMsg)


class Template:
    labelFont = {'family': 'Times New Roman', 'weight': 'normal', 'size': 16}
    titleFont = {'family': 'Times New Roman', 'weight': 'normal', 'size': 18}
    legendFont = {'family': 'Times New Roman', 'weight': 'normal', 'size': 12}
    tickFont = {'family': 'Times New Roman', 'weight': 'normal', 'size': 12}
    tickLabelFont = {'family': 'Times New Roman', 'weight': 'normal', 'size': 14}
    subplotCodeFont = {'family': 'Times New Roman', 'weight': 'normal', 'size': 16}

    @classmethod
    def setLabelFont(cls, labelFont):
        cls.labelFont = labelFont

    @classmethod
    def setTitleFont(cls, titleFont):
        cls.titleFont = titleFont

    @classmethod
    def setLegendFont(cls, legendFont):
        cls.legendFont = legendFont

    @classmethod
    def setSubplotCodeFont(cls, subplotCodeFont):
        cls.subplotCodeFont = subplotCodeFont

    @classmethod
    def setLim(cls, **kwargs):
        # 设置图像有效范围(lim)
        try:
            if kwargs.get("xlim"):
                cls.axes.set_xlim(kwargs.get("xlim"))
            if kwargs.get("ylim"):
                cls.axes.set_ylim(kwargs.get("ylim"))
            if kwargs.get("zlim"):
                cls.axes.set_zlim(kwargs.get("zlim"))
        except Exception as errMsg:
            raise BusinessException(EmBusinessError.NETWORK_CUSTOM_METRIC_ERROR, errMsg)

    @classmethod
    def setLabel(cls, **kwargs):
        # 设置坐标轴名称(label)
        if kwargs.get("xlabel"):
            cls.axes.set_xlabel(kwargs.get("xlabel"), cls.labelFont)
        if kwargs.get("ylabel"):
            cls.axes.set_ylabel(kwargs.get("ylabel"), cls.labelFont)
        if kwargs.get("zlabel"):
            cls.axes.set_zlabel(kwargs.get("zlabel"), cls.labelFont)

    @classmethod
    def setTitle(cls, **kwargs):
        # 设置标题名称(title)
        if kwargs.get("title"):
            cls.axes.set_title(kwargs.get("title"), cls.titleFont)

    @classmethod
    def setSubplotCode(cls, **kwargs):
        # 设置分图编号
        if kwargs.get("subplotCode"):
            locX, locY = kwargs.get("subplotCodeLoc", (0.02, 0.94))
            cls.axes.text(locX, locY, kwargs.get("subplotCode"), transform=cls.axes.transAxes,
                          fontdict=cls.subplotCodeFont)

    @classmethod
    def setLogAxes(cls, **kwargs):
        # 对数坐标
        if kwargs.get("xlog"):
            cls.axes.set_xscale('log')
        if kwargs.get("ylog"):
            cls.axes.set_yscale('log')
        if kwargs.get("zlog"):
            cls.axes.set_zscale('log')

    @classmethod
    def setLegend(cls, **kwargs):
        # 设置图例(legend)
        """legend( handles=(line1, line2, line3),
                            labels=('label1', 'label2', 'label3'),
                            'upper right')
                        The *loc* location codes are::

                            'best' : 0,          (currently not supported for figure legends)
                            'upper right'  : 1,
                            'upper left'   : 2,
                            'lower left'   : 3,
                            'lower right'  : 4,
                            'right'        : 5,
                            'center left'  : 6,
                            'center right' : 7,
                            'lower center' : 8,
                            'upper center' : 9,
                            'center'       : 10,
        """
        if kwargs.get("showLegend"):
            plt.legend(handles=cls.handles,
                       labels=kwargs.get("labels"),
                       loc=kwargs.get("loc", "best"),
                       prop=cls.legendFont)
            # plt.legend(labels=kwargs.get("labels"), loc=kwargs.get("loc", "best"),
            #            prop=cls.legendFont)
            # plt.legend(loc=kwargs.get("loc", "best"), prop=cls.legendFont)

        if kwargs.get("legendOutlier"):
            plt.legend(prop={'family': 'Times New Roman', 'weight': 'normal', 'size': kwargs.get('legend_font', 12)},
                       bbox_to_anchor=kwargs.get('bbox_to_anchor', (0.98, 0)), loc=3, borderaxespad=0, frameon=True)

    @classmethod
    def setTick(cls, **kwargs):
        # 设置坐标轴刻度(tick)
        # if isinstance(kwargs.get("xtick"), int):
        #     cls.tickFont['size'] = kwargs.get("xtick")
        # elif isinstance(kwargs.get("ytick"), int):
        #     cls.tickFont['size'] = kwargs.get("ytick")
        # elif isinstance(kwargs.get("ztick"), int):
        #     cls.tickFont['size'] = kwargs.get("ztick")
        if kwargs.get("xtick"):
            cls.axes.set_xticks(kwargs.get("xtick"), cls.tickFont)
        if kwargs.get("ytick"):
            cls.axes.set_yticks(kwargs.get("ytick"), cls.tickFont)
        if kwargs.get("ztick"):
            cls.axes.set_zticks(kwargs.get("ztick"), cls.tickFont)

    @classmethod
    def setTickLabel(cls, **kwargs):
        # 设置坐标轴刻度标签(tickLabel)
        if kwargs.get("xtickLabel"):
            cls.axes.set_xticklabels(kwargs.get("xtickLabel"), cls.tickLabelFont)

        if kwargs.get("ytickLabel"):
            cls.axes.set_yticklabels(kwargs.get("ytickLabel"), cls.tickLabelFont)

        if kwargs.get("ztickLabel"):
            cls.axes.set_zticklabels(kwargs.get("ztickLabel"), cls.tickLabelFont)

    @classmethod
    def setTickRotation(cls, **kwargs):
        # 设置坐标轴刻度标签(tickLabel)
        if kwargs.get("xrotation"):
            plt.xticks(rotation=kwargs.get("xrotation"))
        if kwargs.get("yrotation"):
            plt.yticks(rotation=kwargs.get("yrotation"))
        if kwargs.get("zrotation"):
            plt.zticks(rotation=kwargs.get("zrotation"))

    @classmethod
    def setGridOn(cls, **kwargs):
        # 开启网格
        if kwargs.get("gridOn"):
            plt.grid(True)

    @classmethod
    def setColorBar(cls, **kwargs):
        # 设置色标(colorbar)
        if kwargs.get("colorbar"):
            plt.colorbar(shrink=kwargs.get("shrink", .92))

    @classmethod
    def setTickFont(cls, **kwargs):
        # 设置tickFont
        if kwargs.get('tickFont'):
            plt.tick_params(labelsize=kwargs.get('tickFont', cls.tickFont))
            labels = cls.axes.get_xticklabels() + cls.axes.get_yticklabels()
            [label.set_fontname('Times New Roman') for label in labels]

    @classmethod
    def commonTemplate(cls, **kwargs):

        # 设置图像有效范围(lim)
        cls.setLim(xlim=kwargs.get("xlim"), ylim=kwargs.get("ylim"), zlim=kwargs.get("zlim"))

        # 设置坐标轴名称(label)
        cls.setLabel(xlabel=kwargs.get("xlabel"), ylabel=kwargs.get("ylabel"), zlabel=kwargs.get("zlabel"))

        # 设置标题
        cls.setTitle(title=kwargs.get("title"))

        # 设置图例
        cls.setLegend(showLegend=kwargs.get("showLegend"), labels=kwargs.get("labels"), loc=kwargs.get("loc"),
                      legendOutlier=kwargs.get("legendOutlier", False))

        # 设置分图编号
        cls.setSubplotCode(subplotCode=kwargs.get("subplotCode"), subplotCodeLoc=kwargs.get("subplotCodeLoc"))

        # 设置对数坐标系
        cls.setLogAxes(xlog=kwargs.get("xlog"), ylog=kwargs.get("ylog"), zlog=kwargs.get("zlog"))

        # 设置坐标轴刻度(tick)
        cls.setTick(xtick=kwargs.get("xtick"), ytick=kwargs.get("ytick"), ztick=kwargs.get("ztick"), )

        # 设置坐标轴刻度标签(tickLabel)
        cls.setTickLabel(xtickLabel=kwargs.get("xtickLabel"), ytickLabel=kwargs.get("ytickLabel"),
                         ztickLabel=kwargs.get("ztickLabel"))

        # 设置ticks旋转
        cls.setTickRotation(xrotation=kwargs.get("xrotation"), yrotation=kwargs.get("yrotation"),
                            zrotation=kwargs.get("zrotation"))
        # 开启网格
        cls.setGridOn(gridOn=kwargs.get("gridOn", False))

        # 设置色标(colorbar)
        cls.setColorBar(showColorBar=kwargs.get("showColorBar", False), shrink=kwargs.get("shrink", .92))

        # 设置坐标轴刻度的字体
        cls.setTickFont(tickFont=kwargs.get("tickFont"))

        return


class Postprocessing:
    @classmethod
    def figureShow(cls):
        try:
            plt.tight_layout()
            if cls.DEBUG:
                cls.fig.show()
                plt.pause(3)
            plt.close()
        except Exception as errMsg:
            raise BusinessException(EmBusinessError.FIGURE_POSTPROCESSING_FAIL, errMsg)

    @classmethod
    def figureSave(cls, **kwargs):
        try:
            import os
            save_name = kwargs.get("saveName")
            save_path = kwargs.get('savePath', PATH.get("out/pdf"))
            cls.fig.savefig(
                os.path.join(save_path, '{0}.pdf'.format(save_name) if kwargs.get("saveAsPDF", True) else save_name),
                dpi=500, bbox_inches='tight')
        except Exception as errMsg:
            raise BusinessException(EmBusinessError.FIGURE_POSTPROCESSING_FAIL, errMsg)


class FigureService(Axes, Template, Postprocessing):
    fig, axes = None, None
    handles = []
    # DEBUG = False  # debug模式下，开启三秒展示，展示所有警告信息
    DEBUG = True  # debug模式下，开启三秒展示，展示所有警告信息
    if not DEBUG:
        from matplotlib.axes._axes import _log as matplotlib_axes_logger
        matplotlib_axes_logger.setLevel('ERROR')
    ALPHA = [1, 1, 1, 1, 1, 1]
    COLOR = [plt.get_cmap('tab20c').colors[i] for i in [0, 4, 8, 12, 16, 18]]
    MARKER = ['^', 'o', 's', '*', '+', 'D']
    MARKER_COLOR = [plt.get_cmap('tab20c').colors[i] for i in [1, 5, 8, 12, 16, 18]]

    def __init__(self, **kwargs):
        self.initFigure(num=kwargs.get("num", 1),
                        figsize=kwargs.get("figsize", (10, 8)))

    @classmethod
    def initFigure(cls, **kwargs):
        cls.fig = plt.figure(num=kwargs.get("num"),
                             figsize=kwargs.get("figsize"), )
        cls.axes = plt.subplot()


if __name__ == "__main__":
    # ----------------------------------------测试绘制直线-------------------------------------------

    def simpleLine():
        # 创建FigureService实例
        figureService = FigureService()

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
