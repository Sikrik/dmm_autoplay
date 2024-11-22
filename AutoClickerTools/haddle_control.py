import win32api
import pygetwindow as gw
import win32con
import win32gui
from PIL import ImageGrab

class AutoPlay:
    def get_windows(self):
        im = ImageGrab.grab()
        windows = gw.getAllWindows()
        print("当前打开的窗口列表：")
        for window in windows:
            print(window)

    def get_window_test(self):
        target_window_title = "哔哩哔哩 (゜-゜)つロ 干杯~-bilibili - Google Chrome"
        target_window = gw.getWindowsWithTitle(target_window_title)
        if target_window:
            print("找到bilibili窗口啦")
            return target_window[0]
        else:
            print("未找到该窗口")
            return None

    def get_window_pic(self, name):
        handle = win32gui.FindWindow(0, name)
        if handle == 0:
            print("未找到该窗口")
            return None
        else:
            left, top, right, bottom = win32gui.GetWindowRect(handle)
            screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
            screenshot.show()
            return screenshot

    def click_handle(self, x, y, handle):
        if handle == 0:
            print("无效的窗口句柄")
            return
        long_position = win32api.MAKELONG(x, y)
        win32api.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)
        win32api.SendMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)

    def focus_window(self, handle):
        if handle != 0:
            win32gui.SetForegroundWindow(handle)
        else:
            print("无效的窗口句柄")

    def get_windows_info(self):
        hd = win32gui.GetDesktopWindow()
        hwndChildList = []
        win32gui.EnumChildWindows(hd, lambda hwnd, param: param.append(hwnd), hwndChildList)
        for hwnd in hwndChildList:
            title = win32gui.GetWindowText(hwnd)
            if title:
                print("句柄:", hwnd, "标题:", title)

    def get_window_info(self, name):
        handle = win32gui.FindWindow(0, name)
        return handle

    def get_window_coordinate_info(self, name):
        handle = win32gui.FindWindow(0, name)
        if handle == 0:
            return None
        else:
            return win32gui.GetWindowRect(handle)

    def is_window_exist(self, name):
        handle = win32gui.FindWindow(0, name)
        return handle != 0