from abc import ABC,abstractmethod



class dmm_autoplay(ABC):


    """
    以下为抽象变量screenshot_path的定义与获取
    """
    #screenshot_path：用来保存识别当前屏幕截图的文件地址
    @property
    @abstractmethod
    def screenshot_path(self):
        """获取抽象变量的值"""
        pass

    @screenshot_path.setter
    @abstractmethod
    def screenshot_path(self, value):
        """设置抽象变量的值"""
        pass

    """
    以下为在子类中需要实现抽象方法
    """
    #领取登录奖励
    @abstractmethod
    def login_bonus(self):
        raise NotImplemented()

    #完成每日任务
    @abstractmethod
    def daily_task(self):
        raise NotImplemented()

    #识别当前游戏处于哪个场景中
    @abstractmethod
    def judgment_interface(self):
        raise NotImplemented()

    #识别当前屏幕中有哪些图片
    @abstractmethod
    def judgment_imgs(self):
        raise NotImplemented()
