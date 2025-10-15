import pygame
import win32api
import win32con
import win32gui

def create_transparent_window(fuchsia):
	# Create layered window
	hwnd = pygame.display.get_wm_info()["window"]
	win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
						win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
	# Set window transparency color
	win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)

def topmost():
	hwnd = win32gui.GetForegroundWindow()

	win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOSIZE)