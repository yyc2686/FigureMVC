from error.CommonError import CommonError
from enum import Enum


class EmBusinessError(CommonError, Enum):
    # 通用错误类型10001开始
    PARAMETER_VALIDATION_ERROR = {"errCode": 10001, "errMsg": "参数不合法"}
    UNKNOW_ERROR = {"errCode": 10002, "errMsg": "未知错误"}

    # Figure相关错误50001开始
    FIGURE_PREPROCESSING_FAIL = {"errCode": 60001, "errMsg": "Figure数据预处理异常"}
    FIGURE_AXES_FAIL = {"errCode": 60002, "errMsg": "Figure绘图异常"}
    FIGURE_TEMPLATE_FAIL = {"errCode": 60003, "errMsg": "Figure模板异常"}
    FIGURE_POSTPROCESSING_FAIL = {"errCode": 60004, "errMsg": "Figure后续处理异常"}

    def getErrCode(self):
        return self.value.get("errCode")

    def getErrMsg(self):
        return self.value.get("errMsg")

    def setErrMsg(self, errMsg):
        self.value["errMsg"] = errMsg
        return self

    def __str__(self):
        return str(self.value)


if __name__ == "__main__":
    a = EmBusinessError.PARAMETER_VALIDATION_ERROR
    print(a)
    print(a.getErrCode())
    print(a.getErrMsg())

    print()

    a = EmBusinessError.PARAMETER_VALIDATION_ERROR.setErrMsg("哈哈哈")
    print(a)
    print(a.getErrCode())
    print(a.getErrMsg())
