#mPythonType:0
#mPythonType:0
from mpython import *

# 2月份推出桌面图标内容，由LP反馈。【240110-01-ZJ1】
system_core = 'POLA OS 3.5'
system_version = 'PIO-3'
OS_3_5_system_category = '先锋版'
system_core_size = '63.22KB'
device_owner = 'rong'

print(''.join([str(x) for x in [device_owner, '，欢迎体验', system_core]]))

oled.fill(0)
oled.Bitmap(32, 23, bytearray([0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X7F,0XC0,0X0F,0XE0,0X1C,0X00,0X1E,0X00, 0X7F,0XF0,0X1F,0XF8,0X1C,0X00,0X1E,0X00,0X7F,0XF8,0X3F,0XFC,0X1C,0X00,0X3F,0X00, 0X70,0X38,0X78,0X1E,0X1C,0X00,0X3F,0X00,0X70,0X38,0XF0,0X0E,0X1C,0X00,0X3F,0X00, 0X70,0X3C,0XE0,0X0F,0X1C,0X00,0X73,0X80,0X70,0X38,0XE0,0X07,0X1C,0X00,0X73,0X80, 0X70,0X78,0XE0,0X07,0X1C,0X00,0XE3,0X80,0X7F,0XF8,0XE0,0X07,0X1C,0X00,0XE1,0XC0, 0X7F,0XF0,0XE0,0X07,0X1C,0X00,0XE1,0XC0,0X7F,0XC0,0XE0,0X07,0X1C,0X01,0XFF,0XE0, 0X70,0X00,0XF0,0X0E,0X1C,0X01,0XFF,0XE0,0X70,0X00,0X78,0X1E,0X1C,0X01,0XFF,0XE0, 0X70,0X00,0X7E,0XFC,0X1F,0XF3,0X80,0X70,0X70,0X00,0X3F,0XF8,0X1F,0XF3,0X80,0X70, 0X70,0X00,0X0F,0XF0,0X1F,0XF7,0X80,0X70,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,]), 64, 18, 1)
oled.show()

print('无线网络连接中')

import network

my_wifi = wifi()

my_wifi.connectWiFi("wxq", "wxqwxq123")

print('无线网络连接成功')

from machine import Timer

import ntptime

import time

import framebuf

import font.dvsmb_21

import font.dvsm_21

import json

import urequests

_is_shaked = _is_thrown = False
_last_x = _last_y = _last_z = _count_shaked = _count_thrown = 0
def on_shaked():pass
def on_thrown():pass

tim11 = Timer(11)

def timer11_tick(_):
    global _is_shaked, _is_thrown, _last_x, _last_y, _last_z, _count_shaked, _count_thrown
    if _is_shaked:
        _count_shaked += 1
        if _count_shaked == 5: _count_shaked = 0
    if _is_thrown:
        _count_thrown += 1
        if _count_thrown == 10: _count_thrown = 0
        if _count_thrown > 0: return
    x=accelerometer.get_x(); y=accelerometer.get_y(); z=accelerometer.get_z()
    _is_thrown = (x * x + y * y + z * z < 0.25)
    if _is_thrown: on_thrown();return
    if _last_x == 0 and _last_y == 0 and _last_z == 0:
        _last_x = x; _last_y = y; _last_z = z; return
    diff_x = x - _last_x; diff_y = y - _last_y; diff_z = z - _last_z
    _last_x = x; _last_y = y; _last_z = z
    if _count_shaked > 0: return
    _is_shaked = (diff_x * diff_x + diff_y * diff_y + diff_z * diff_z > 1)
    if _is_shaked: on_shaked()

tim11.init(period=100, mode=Timer.PERIODIC, callback=timer11_tick)

import music

def timer1_tick(_):
    global OS_3_5_app_settings_icon_y, OS_3_5_app_settings_chosen_name, OS_3_5_app_settings_chosen, app_settings_selection_item, app_settings_item_3, app_settings_item_2, app_weather_forecast_temperature, app_weather_report, app_lighting_mode, app_settings_item_1, app_weather_location, app_lighting_brightness, app_woodenfish_times, system_time_date, system_time_week, system_time_minute, system_time_hour, home_icon_fillet, home_icon_edge, home_movement_y, home_movement_x, system_app_SOS_resetmode, system_app_system_resetmode, system_app_lighting_resetmode, system_app_woodenfish_resetmode, app_settings_resetmode, system_app_weather_resetmode, syetem_consani_start_fillet, system_consani_start_height, system_consani_start_wide, system_consani_start_y, system_consani_start_x, system_consani_shadow_length, system_app_settings_lockscreen_style, system_app_settings_display_mode, system_homemode, system_notification_source, system_notification_detail, OS_3_5_system_consani_level_above_y, app_mader_name, OS_3_5_system_consani_level_below_corner, OS_3_5_system_consani_level_below_y, OS_3_5_system_consani_level_below_x, OS_3_5_system_consani_expand_corner, OS_3_5_system_consani_expand_tall, OS_3_5_system_consani_expand_width, OS_3_5_system_consani_expand_y, OS_3_5_system_consani_expand_x, device_owner, app_name, OS_3_5_system_consani_level_x, system_core_size, system_interface_y, OS_3_5_system_basic_plugin_countdown, OS_3_5_system_consani_level_basic, OS_3_5_system_category, OS_3_5_system_basic_plugin_chosen, OS_3_5_system_consani_level_y, OS_3_5_system_consani_expand_square_effect_basic, hardware_brightness_value, system_version, system_core
    hardware_brightness_value = hardware_brightness_value
    oled.contrast(hardware_brightness_value)

tim1 = Timer(1)

def consani_V2_expand_enter():
    global system_core, system_version, hardware_brightness_value, OS_3_5_system_consani_expand_square_effect_basic, OS_3_5_system_consani_level_y, OS_3_5_system_basic_plugin_chosen, OS_3_5_system_category, system_interface_y, OS_3_5_system_consani_level_basic, OS_3_5_system_basic_plugin_countdown, system_core_size, OS_3_5_system_consani_level_x, app_name, device_owner, OS_3_5_system_consani_expand_x, OS_3_5_system_consani_expand_y, OS_3_5_system_consani_expand_width, OS_3_5_system_consani_expand_tall, OS_3_5_system_consani_expand_corner, OS_3_5_system_consani_level_below_x, OS_3_5_system_consani_level_below_y, OS_3_5_system_consani_level_below_corner, app_mader_name, OS_3_5_system_consani_level_above_y, system_notification_detail, system_notification_source, system_homemode, system_app_settings_display_mode, system_app_settings_lockscreen_style, system_consani_shadow_length, system_consani_start_x, system_consani_start_y, system_consani_start_wide, system_consani_start_height, syetem_consani_start_fillet, system_app_weather_resetmode, app_settings_resetmode, system_app_woodenfish_resetmode, system_app_lighting_resetmode, system_app_system_resetmode, system_app_SOS_resetmode, home_movement_x, home_movement_y, home_icon_edge, home_icon_fillet, system_time_hour, system_time_minute, system_time_week, system_time_date, app_woodenfish_times, app_lighting_brightness, app_weather_location, app_settings_item_1, app_lighting_mode, app_weather_report, app_weather_forecast_temperature, app_settings_item_2, app_settings_item_3, app_settings_selection_item, OS_3_5_app_settings_chosen, OS_3_5_app_settings_chosen_name, OS_3_5_app_settings_icon_y
    OS_3_5_system_consani_expand_square_effect_basic = 1
    for count in range(2):
        oled.RoundRect(OS_3_5_system_consani_expand_x, OS_3_5_system_consani_expand_y, OS_3_5_system_consani_expand_width, OS_3_5_system_consani_expand_tall, OS_3_5_system_consani_expand_corner, 0)
        oled.RoundRect(OS_3_5_system_consani_expand_x, OS_3_5_system_consani_expand_y, OS_3_5_system_consani_expand_width, OS_3_5_system_consani_expand_tall, OS_3_5_system_consani_expand_corner, 1)
        OS_3_5_system_consani_expand_x = OS_3_5_system_consani_expand_x - OS_3_5_system_consani_expand_square_effect_basic * OS_3_5_system_consani_expand_square_effect_basic
        OS_3_5_system_consani_expand_y = OS_3_5_system_consani_expand_y - OS_3_5_system_consani_expand_square_effect_basic * OS_3_5_system_consani_expand_square_effect_basic
        OS_3_5_system_consani_expand_width = OS_3_5_system_consani_expand_width + 2 * (OS_3_5_system_consani_expand_square_effect_basic * OS_3_5_system_consani_expand_square_effect_basic)
        OS_3_5_system_consani_expand_tall = OS_3_5_system_consani_expand_tall + 2 * (OS_3_5_system_consani_expand_square_effect_basic * OS_3_5_system_consani_expand_square_effect_basic)
        OS_3_5_system_consani_expand_square_effect_basic = OS_3_5_system_consani_expand_square_effect_basic + 1
        OS_3_5_system_consani_expand_corner = OS_3_5_system_consani_expand_corner + -2
        oled.show()
    while not (OS_3_5_system_consani_expand_y + OS_3_5_system_consani_expand_tall >= 63 or OS_3_5_system_consani_expand_x + OS_3_5_system_consani_expand_width >= 127):
        oled.fill_rect(OS_3_5_system_consani_expand_x, OS_3_5_system_consani_expand_y, OS_3_5_system_consani_expand_width, OS_3_5_system_consani_expand_tall, 0)
        oled.rect(OS_3_5_system_consani_expand_x, OS_3_5_system_consani_expand_y, OS_3_5_system_consani_expand_width, OS_3_5_system_consani_expand_tall, 1)
        OS_3_5_system_consani_expand_x = OS_3_5_system_consani_expand_x // 2
        OS_3_5_system_consani_expand_y = OS_3_5_system_consani_expand_y // 2
        OS_3_5_system_consani_expand_width = OS_3_5_system_consani_expand_width + (128 - OS_3_5_system_consani_expand_width) // 2
        OS_3_5_system_consani_expand_tall = OS_3_5_system_consani_expand_tall + (64 - OS_3_5_system_consani_expand_tall) // 2
        oled.show()
        time.sleep_ms(10)

def timer2_tick(_):
    global OS_3_5_app_settings_icon_y, OS_3_5_app_settings_chosen_name, OS_3_5_app_settings_chosen, app_settings_selection_item, app_settings_item_3, app_settings_item_2, app_weather_forecast_temperature, app_weather_report, app_lighting_mode, app_settings_item_1, app_weather_location, app_lighting_brightness, app_woodenfish_times, system_time_date, system_time_week, system_time_minute, system_time_hour, home_icon_fillet, home_icon_edge, home_movement_y, home_movement_x, system_app_SOS_resetmode, system_app_system_resetmode, system_app_lighting_resetmode, system_app_woodenfish_resetmode, app_settings_resetmode, system_app_weather_resetmode, syetem_consani_start_fillet, system_consani_start_height, system_consani_start_wide, system_consani_start_y, system_consani_start_x, system_consani_shadow_length, system_app_settings_lockscreen_style, system_app_settings_display_mode, system_homemode, system_notification_source, system_notification_detail, OS_3_5_system_consani_level_above_y, app_mader_name, OS_3_5_system_consani_level_below_corner, OS_3_5_system_consani_level_below_y, OS_3_5_system_consani_level_below_x, OS_3_5_system_consani_expand_corner, OS_3_5_system_consani_expand_tall, OS_3_5_system_consani_expand_width, OS_3_5_system_consani_expand_y, OS_3_5_system_consani_expand_x, device_owner, app_name, OS_3_5_system_consani_level_x, system_core_size, system_interface_y, OS_3_5_system_basic_plugin_countdown, OS_3_5_system_consani_level_basic, OS_3_5_system_category, OS_3_5_system_basic_plugin_chosen, OS_3_5_system_consani_level_y, OS_3_5_system_consani_expand_square_effect_basic, hardware_brightness_value, system_version, system_core
    if button_a.is_pressed() and button_b.is_pressed():
        system_interface_y = 20
        oled.fill_rect(0, 0, 128, 20, 1)
        oled.DispChar(str((''.join([str(x) for x in [system_notification_detail, '——来自', system_notification_source]]))), 5, 3, 2)
    else:
        system_interface_y = 0

tim2 = Timer(2)

# 变量待适配
def Consani_V2_level_enter():
    global system_core, system_version, hardware_brightness_value, OS_3_5_system_consani_expand_square_effect_basic, OS_3_5_system_consani_level_y, OS_3_5_system_basic_plugin_chosen, OS_3_5_system_category, system_interface_y, OS_3_5_system_consani_level_basic, OS_3_5_system_basic_plugin_countdown, system_core_size, OS_3_5_system_consani_level_x, app_name, device_owner, OS_3_5_system_consani_expand_x, OS_3_5_system_consani_expand_y, OS_3_5_system_consani_expand_width, OS_3_5_system_consani_expand_tall, OS_3_5_system_consani_expand_corner, OS_3_5_system_consani_level_below_x, OS_3_5_system_consani_level_below_y, OS_3_5_system_consani_level_below_corner, app_mader_name, OS_3_5_system_consani_level_above_y, system_notification_detail, system_notification_source, system_homemode, system_app_settings_display_mode, system_app_settings_lockscreen_style, system_consani_shadow_length, system_consani_start_x, system_consani_start_y, system_consani_start_wide, system_consani_start_height, syetem_consani_start_fillet, system_app_weather_resetmode, app_settings_resetmode, system_app_woodenfish_resetmode, system_app_lighting_resetmode, system_app_system_resetmode, system_app_SOS_resetmode, home_movement_x, home_movement_y, home_icon_edge, home_icon_fillet, system_time_hour, system_time_minute, system_time_week, system_time_date, app_woodenfish_times, app_lighting_brightness, app_weather_location, app_settings_item_1, app_lighting_mode, app_weather_report, app_weather_forecast_temperature, app_settings_item_2, app_settings_item_3, app_settings_selection_item, OS_3_5_app_settings_chosen, OS_3_5_app_settings_chosen_name, OS_3_5_app_settings_icon_y
    OS_3_5_system_consani_level_y = 64
    OS_3_5_system_consani_level_basic = 1
    OS_3_5_system_consani_level_x = 0
    OS_3_5_system_consani_level_below_x = 14
    OS_3_5_system_consani_level_above_y = OS_3_5_system_consani_level_y - 64
    OS_3_5_system_consani_level_below_y = 7
    OS_3_5_system_consani_level_below_corner = 10
    for count in range(4):
        oled.fill(0)
        oled.RoundRect(OS_3_5_system_consani_level_below_x, OS_3_5_system_consani_level_below_y, (128 - 2 * OS_3_5_system_consani_level_below_x), (64 - 2 * OS_3_5_system_consani_level_below_y), OS_3_5_system_consani_level_below_corner, 1)
        oled.fill_rect(OS_3_5_system_consani_level_x, OS_3_5_system_consani_level_above_y, 128, 64, 0)
        oled.hline(54, (OS_3_5_system_consani_level_above_y + 59), 20, 1)
        OS_3_5_system_consani_level_above_y = OS_3_5_system_consani_level_above_y + -14
        OS_3_5_system_consani_level_below_x = OS_3_5_system_consani_level_below_x + -2
        OS_3_5_system_consani_level_below_y = OS_3_5_system_consani_level_below_y + -1
        OS_3_5_system_consani_level_below_corner = OS_3_5_system_consani_level_below_corner + -1
        OS_3_5_system_consani_level_y = OS_3_5_system_consani_level_y - OS_3_5_system_consani_level_basic * OS_3_5_system_consani_level_basic
        OS_3_5_system_consani_level_basic = OS_3_5_system_consani_level_basic + 1
        OS_3_5_system_consani_level_above_y = OS_3_5_system_consani_level_y - 64
        time.sleep_ms((OS_3_5_system_consani_level_basic * 5))
        oled.show()
    for count in range(7):
        oled.fill(0)
        oled.RoundRect(OS_3_5_system_consani_level_below_x, OS_3_5_system_consani_level_below_y, (128 - 2 * OS_3_5_system_consani_level_below_x), (64 - 2 * OS_3_5_system_consani_level_below_y), OS_3_5_system_consani_level_below_corner, 1)
        oled.fill_rect(OS_3_5_system_consani_level_x, OS_3_5_system_consani_level_above_y, 128, 64, 0)
        oled.hline(54, (OS_3_5_system_consani_level_above_y + 59), 20, 1)
        OS_3_5_system_consani_level_above_y = OS_3_5_system_consani_level_above_y + -14
        OS_3_5_system_consani_level_below_x = OS_3_5_system_consani_level_below_x + -2
        OS_3_5_system_consani_level_below_y = OS_3_5_system_consani_level_below_y + -1
        OS_3_5_system_consani_level_below_corner = OS_3_5_system_consani_level_below_corner + -1
        OS_3_5_system_consani_level_y = OS_3_5_system_consani_level_y // 2
        OS_3_5_system_consani_level_basic = OS_3_5_system_consani_level_basic + 1
        OS_3_5_system_consani_level_above_y = OS_3_5_system_consani_level_y - 64
        time.sleep_ms((OS_3_5_system_consani_level_basic * 5))
        oled.show()

# 变量待适配
def Consani_V2_level_leave():
    global system_core, system_version, hardware_brightness_value, OS_3_5_system_consani_expand_square_effect_basic, OS_3_5_system_consani_level_y, OS_3_5_system_basic_plugin_chosen, OS_3_5_system_category, system_interface_y, OS_3_5_system_consani_level_basic, OS_3_5_system_basic_plugin_countdown, system_core_size, OS_3_5_system_consani_level_x, app_name, device_owner, OS_3_5_system_consani_expand_x, OS_3_5_system_consani_expand_y, OS_3_5_system_consani_expand_width, OS_3_5_system_consani_expand_tall, OS_3_5_system_consani_expand_corner, OS_3_5_system_consani_level_below_x, OS_3_5_system_consani_level_below_y, OS_3_5_system_consani_level_below_corner, app_mader_name, OS_3_5_system_consani_level_above_y, system_notification_detail, system_notification_source, system_homemode, system_app_settings_display_mode, system_app_settings_lockscreen_style, system_consani_shadow_length, system_consani_start_x, system_consani_start_y, system_consani_start_wide, system_consani_start_height, syetem_consani_start_fillet, system_app_weather_resetmode, app_settings_resetmode, system_app_woodenfish_resetmode, system_app_lighting_resetmode, system_app_system_resetmode, system_app_SOS_resetmode, home_movement_x, home_movement_y, home_icon_edge, home_icon_fillet, system_time_hour, system_time_minute, system_time_week, system_time_date, app_woodenfish_times, app_lighting_brightness, app_weather_location, app_settings_item_1, app_lighting_mode, app_weather_report, app_weather_forecast_temperature, app_settings_item_2, app_settings_item_3, app_settings_selection_item, OS_3_5_app_settings_chosen, OS_3_5_app_settings_chosen_name, OS_3_5_app_settings_icon_y
    for count in range(4):
        oled.fill(0)
        oled.RoundRect(OS_3_5_system_consani_level_below_x, OS_3_5_system_consani_level_below_y, (128 - 2 * OS_3_5_system_consani_level_below_x), (64 - 2 * OS_3_5_system_consani_level_below_y), OS_3_5_system_consani_level_below_corner, 1)
        oled.fill_rect(OS_3_5_system_consani_level_x, OS_3_5_system_consani_level_above_y, 128, 64, 0)
        oled.hline(54, (OS_3_5_system_consani_level_above_y + 59), 20, 1)
        OS_3_5_system_consani_level_above_y = OS_3_5_system_consani_level_above_y + 14
        OS_3_5_system_consani_level_below_x = OS_3_5_system_consani_level_below_x + 2
        OS_3_5_system_consani_level_below_y = OS_3_5_system_consani_level_below_y + 1
        OS_3_5_system_consani_level_below_corner = OS_3_5_system_consani_level_below_corner + 1
        OS_3_5_system_consani_level_y = OS_3_5_system_consani_level_y - OS_3_5_system_consani_level_basic * OS_3_5_system_consani_level_basic
        OS_3_5_system_consani_level_basic = OS_3_5_system_consani_level_basic + 1
        OS_3_5_system_consani_level_above_y = OS_3_5_system_consani_level_y - 64
        time.sleep_ms((OS_3_5_system_consani_level_basic * 5))
        oled.show()
    for count in range(7):
        oled.fill(0)
        oled.RoundRect(OS_3_5_system_consani_level_below_x, OS_3_5_system_consani_level_below_y, (128 - 2 * OS_3_5_system_consani_level_below_x), (64 - 2 * OS_3_5_system_consani_level_below_y), OS_3_5_system_consani_level_below_corner, 1)
        oled.fill_rect(OS_3_5_system_consani_level_x, OS_3_5_system_consani_level_above_y, 128, 64, 0)
        oled.hline(54, (OS_3_5_system_consani_level_above_y + 59), 20, 1)
        OS_3_5_system_consani_level_above_y = OS_3_5_system_consani_level_above_y + 14
        OS_3_5_system_consani_level_below_x = OS_3_5_system_consani_level_below_x + 2
        OS_3_5_system_consani_level_below_y = OS_3_5_system_consani_level_below_y + 1
        OS_3_5_system_consani_level_below_corner = OS_3_5_system_consani_level_below_corner + 1
        OS_3_5_system_consani_level_y = OS_3_5_system_consani_level_y // 2
        OS_3_5_system_consani_level_basic = OS_3_5_system_consani_level_basic + 1
        OS_3_5_system_consani_level_above_y = OS_3_5_system_consani_level_y - 64
        time.sleep_ms((OS_3_5_system_consani_level_basic * 5))
        oled.show()

import machine

def system_basic_plugin():
    global system_core, system_version, hardware_brightness_value, OS_3_5_system_consani_expand_square_effect_basic, OS_3_5_system_consani_level_y, OS_3_5_system_basic_plugin_chosen, OS_3_5_system_category, system_interface_y, OS_3_5_system_consani_level_basic, OS_3_5_system_basic_plugin_countdown, system_core_size, OS_3_5_system_consani_level_x, app_name, device_owner, OS_3_5_system_consani_expand_x, OS_3_5_system_consani_expand_y, OS_3_5_system_consani_expand_width, OS_3_5_system_consani_expand_tall, OS_3_5_system_consani_expand_corner, OS_3_5_system_consani_level_below_x, OS_3_5_system_consani_level_below_y, OS_3_5_system_consani_level_below_corner, app_mader_name, OS_3_5_system_consani_level_above_y, system_notification_detail, system_notification_source, system_homemode, system_app_settings_display_mode, system_app_settings_lockscreen_style, system_consani_shadow_length, system_consani_start_x, system_consani_start_y, system_consani_start_wide, system_consani_start_height, syetem_consani_start_fillet, system_app_weather_resetmode, app_settings_resetmode, system_app_woodenfish_resetmode, system_app_lighting_resetmode, system_app_system_resetmode, system_app_SOS_resetmode, home_movement_x, home_movement_y, home_icon_edge, home_icon_fillet, system_time_hour, system_time_minute, system_time_week, system_time_date, app_woodenfish_times, app_lighting_brightness, app_weather_location, app_settings_item_1, app_lighting_mode, app_weather_report, app_weather_forecast_temperature, app_settings_item_2, app_settings_item_3, app_settings_selection_item, OS_3_5_app_settings_chosen, OS_3_5_app_settings_chosen_name, OS_3_5_app_settings_icon_y
    OS_3_5_system_basic_plugin_chosen = 1
    OS_3_5_system_basic_plugin_countdown = 7
    app_name = '系统基础服务'
    app_mader_name = '系统'
    while True:
        OS_3_5_system_basic_plugin_countdown = 7
        oled.fill(0)
        if _is_shaked:
            break
        if OS_3_5_system_basic_plugin_chosen >= 1 and OS_3_5_system_basic_plugin_chosen <= 2:
            if button_a.is_pressed():
                OS_3_5_system_basic_plugin_chosen = OS_3_5_system_basic_plugin_chosen + -1
            if button_b.is_pressed():
                OS_3_5_system_basic_plugin_chosen = OS_3_5_system_basic_plugin_chosen + 1
        else:
            OS_3_5_system_basic_plugin_chosen = 1
        if OS_3_5_system_basic_plugin_chosen == 1:
            oled.fill_rect(0, 16, 128, 16, 0)
            oled.DispChar(str('重启——TH确认'), 0, 16, 2)
            if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                app_name = '重启确认界面'
                app_mader_name = '系统'
                while not _is_shaked:
                    OS_3_5_system_basic_plugin_countdown = OS_3_5_system_basic_plugin_countdown + -1
                    if OS_3_5_system_basic_plugin_countdown <= 0:
                        oled.fill(0)
                        oled.Bitmap(32, 23, bytearray([0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X7F,0XC0,0X0F,0XE0,0X1C,0X00,0X1E,0X00, 0X7F,0XF0,0X1F,0XF8,0X1C,0X00,0X1E,0X00,0X7F,0XF8,0X3F,0XFC,0X1C,0X00,0X3F,0X00, 0X70,0X38,0X78,0X1E,0X1C,0X00,0X3F,0X00,0X70,0X38,0XF0,0X0E,0X1C,0X00,0X3F,0X00, 0X70,0X3C,0XE0,0X0F,0X1C,0X00,0X73,0X80,0X70,0X38,0XE0,0X07,0X1C,0X00,0X73,0X80, 0X70,0X78,0XE0,0X07,0X1C,0X00,0XE3,0X80,0X7F,0XF8,0XE0,0X07,0X1C,0X00,0XE1,0XC0, 0X7F,0XF0,0XE0,0X07,0X1C,0X00,0XE1,0XC0,0X7F,0XC0,0XE0,0X07,0X1C,0X01,0XFF,0XE0, 0X70,0X00,0XF0,0X0E,0X1C,0X01,0XFF,0XE0,0X70,0X00,0X78,0X1E,0X1C,0X01,0XFF,0XE0, 0X70,0X00,0X7E,0XFC,0X1F,0XF3,0X80,0X70,0X70,0X00,0X3F,0XF8,0X1F,0XF3,0X80,0X70, 0X70,0X00,0X0F,0XF0,0X1F,0XF7,0X80,0X70,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,]), 64, 18, 1)
                        oled.show()
                        time.sleep(1)
                        machine.reset()
                    if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                        break
                    oled.fill(0)
                    oled.DispChar(str(app_name), 5, (system_interface_y + 3), 1)
                    oled.DispChar(str((''.join([str(x) for x in ['系统将于', OS_3_5_system_basic_plugin_countdown, '后重启']]))), 0, 16, 1)
                    oled.DispChar(str('按住PY以取消'), 0, 48, 1)
                    time.sleep(1)
                    oled.show()
        elif OS_3_5_system_basic_plugin_chosen == 2:
            oled.fill_rect(0, 32, 128, 16, 0)
            oled.DispChar(str('清除数据——TH确认'), 0, 32, 2)
            if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                app_name = '数据清除确认界面'
                app_mader_name = '系统'
                while not _is_shaked:
                    OS_3_5_system_basic_plugin_countdown = OS_3_5_system_basic_plugin_countdown + -1
                    if OS_3_5_system_basic_plugin_countdown <= 0:
                        oled.fill(0)
                        oled.Bitmap(32, 23, bytearray([0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X7F,0XC0,0X0F,0XE0,0X1C,0X00,0X1E,0X00, 0X7F,0XF0,0X1F,0XF8,0X1C,0X00,0X1E,0X00,0X7F,0XF8,0X3F,0XFC,0X1C,0X00,0X3F,0X00, 0X70,0X38,0X78,0X1E,0X1C,0X00,0X3F,0X00,0X70,0X38,0XF0,0X0E,0X1C,0X00,0X3F,0X00, 0X70,0X3C,0XE0,0X0F,0X1C,0X00,0X73,0X80,0X70,0X38,0XE0,0X07,0X1C,0X00,0X73,0X80, 0X70,0X78,0XE0,0X07,0X1C,0X00,0XE3,0X80,0X7F,0XF8,0XE0,0X07,0X1C,0X00,0XE1,0XC0, 0X7F,0XF0,0XE0,0X07,0X1C,0X00,0XE1,0XC0,0X7F,0XC0,0XE0,0X07,0X1C,0X01,0XFF,0XE0, 0X70,0X00,0XF0,0X0E,0X1C,0X01,0XFF,0XE0,0X70,0X00,0X78,0X1E,0X1C,0X01,0XFF,0XE0, 0X70,0X00,0X7E,0XFC,0X1F,0XF3,0X80,0X70,0X70,0X00,0X3F,0XF8,0X1F,0XF3,0X80,0X70, 0X70,0X00,0X0F,0XF0,0X1F,0XF7,0X80,0X70,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,]), 64, 18, 1)
                        oled.show()
                        system_homemode = 1
                        system_interface_y = 0
                        system_app_settings_display_mode = '深色'
                        system_app_settings_lockscreen_style = '新版'
                        system_consani_shadow_length = 0
                        system_consani_start_x = 0
                        system_consani_start_y = 0
                        system_consani_start_wide = 128
                        system_consani_start_height = 64
                        syetem_consani_start_fillet = 0
                        OS_3_5_system_consani_expand_x = 0
                        OS_3_5_system_consani_expand_y = 0
                        OS_3_5_system_consani_expand_square_effect_basic = 0
                        system_notification_source = '消息发送者'
                        system_notification_detail = '暂无新消息'
                        system_app_weather_resetmode = 0
                        app_settings_resetmode = 0
                        system_app_woodenfish_resetmode = 0
                        system_app_lighting_resetmode = 0
                        system_app_system_resetmode = 0
                        system_app_SOS_resetmode = 0
                        home_movement_x = 40
                        home_movement_y = 9
                        app_name = '应用名称'
                        app_mader_name = '应用作者'
                        home_icon_edge = 35
                        home_icon_fillet = 7
                    if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                        break
                    oled.fill(0)
                    oled.DispChar(str(app_name), 5, (system_interface_y + 3), 1)
                    oled.DispChar(str((''.join([str(x) for x in ['系统将于', OS_3_5_system_basic_plugin_countdown, '后清除数据']]))), 0, 16, 1)
                    oled.DispChar(str('按住PY以取消'), 0, 48, 1)
                    time.sleep(1)
                    oled.show()
        oled.show()
        oled.DispChar(str(app_name), 5, (system_interface_y + 3), 1)
        oled.DispChar(str('重启'), 0, 16, 1)
        oled.DispChar(str('清除数据'), 0, 32, 1)
        oled.DispChar(str('摇动返回'), 0, 48, 1)

def display_font(_font, _str, _x, _y, _wrap, _z=0):
    _start = _x
    for _c in _str:
        _d = _font.get_ch(_c)
        if _wrap and _x > 128 - _d[2]: _x = _start; _y += _d[1]
        if _c == '1' and _z > 0: oled.fill_rect(_x, _y, _d[2], _d[1], 0)
        oled.blit(framebuf.FrameBuffer(bytearray(_d[0]), _d[2], _d[1],
        framebuf.MONO_HLSB), (_x+int(_d[2]/_z)) if _c=='1' and _z>0 else _x, _y)
        _x += _d[2]

def get_seni_weather(_url, _location):
    _url = _url + "&location=" + _location.replace(" ", "%20")
    response = urequests.get(_url)
    json = response.json()
    response.close()
    return json

myUI = UI(oled)
hardware_brightness_value = 0
tim1.init(period=500, mode=Timer.PERIODIC, callback=timer1_tick)
tim2.init(period=500, mode=Timer.PERIODIC, callback=timer2_tick)
system_homemode = 1
system_interface_y = 0
system_app_settings_display_mode = '深色'
system_app_settings_lockscreen_style = '新版'
system_consani_shadow_length = 0
system_consani_start_x = 0
system_consani_start_y = 0
system_consani_start_wide = 128
system_consani_start_height = 64
syetem_consani_start_fillet = 0
OS_3_5_system_consani_expand_x = 0
OS_3_5_system_consani_expand_y = 0
OS_3_5_system_consani_expand_square_effect_basic = 0
system_notification_source = '消息发送者'
system_notification_detail = '暂无新消息'
system_app_weather_resetmode = 0
app_settings_resetmode = 0
system_app_woodenfish_resetmode = 0
system_app_lighting_resetmode = 0
system_app_system_resetmode = 0
system_app_SOS_resetmode = 0
home_movement_x = 40
home_movement_y = 9
app_name = '应用名称'
app_mader_name = '应用作者'
home_icon_edge = 35
home_icon_fillet = 7
print('POLA OS 使用手册：')
print('打开/确认——同时轻触TH并松开')
print('返回        ——同时轻触PY并松开')
print('滚动图标 ——按住A/B并松开（可长按）')
print('切换        ——同时轻触ON并松开（部分应用）')
if device_owner == '将此替换为用户名（5字以内）':
    device_owner = '我的'
else:
    if len(device_owner) <= 5:
        device_owner = device_owner
    elif len(device_owner) > 5:
        device_owner = '我的'
while True:
    if system_homemode == 1:
        app_name = '锁屏'
        app_mader_name = '系统'
        if my_wifi.sta.isconnected():
            ntptime.settime(8, "time.windows.com")
            system_time_hour = str(time.localtime()[3])
            system_time_minute = str(time.localtime()[4])
            system_time_week = str(time.localtime()[6]+1)
            system_time_date = ''.join([str(x) for x in [time.localtime()[1], '/', time.localtime()[2]]])
            system_notification_detail = ''.join([str(x) for x in [system_time_hour, ':', system_time_minute]])
            system_notification_source = '锁屏'
            if len(system_time_minute) == 1:
                system_time_minute = '0' + str(system_time_minute)
        else:
            system_time_hour = '-  -'
            system_time_minute = '-  -'
            system_time_week = '周  -'
            system_time_date = ''.join([str(x) for x in ['-  -', '/', '-  -']])
            system_notification_detail = '请接入互联网'
            system_notification_source = '锁屏'
        if system_app_settings_lockscreen_style == '新版':
            while True:
                oled.fill(0)
                if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                    system_homemode = 2
                    Consani_V2_level_enter()
                    break
                if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                    system_basic_plugin()
                display_font(font.dvsmb_21, (''.join([str(x) for x in [system_time_hour, ':', system_time_minute]])), 35, (system_interface_y + 20), False)
                oled.hline(44, 61, 40, 1)
                oled.show()
        elif system_app_settings_lockscreen_style == '经典':
            while True:
                oled.fill(0)
                if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                    system_homemode = 2
                    Consani_V2_level_enter()
                    break
                if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                    system_basic_plugin()
                oled.DispChar(str((str(device_owner) + '的掌控板')), 35, (22 + system_interface_y), 1)
                display_font(font.dvsm_21, system_time_hour, 2, (2 + system_interface_y), False)
                display_font(font.dvsm_21, system_time_minute, 2, (22 + system_interface_y), False)
                oled.DispChar(str((''.join([str(x) for x in [system_time_date, '  周', system_time_week]]))), 35, (2 + system_interface_y), 1)
                oled.hline(44, 61, 40, 1)
                oled.show()
    if system_homemode == 2:
        app_name = '桌面'
        app_mader_name = '系统'
        while True:
            oled.fill(0)
            if system_homemode == 1:
                break
            if home_movement_x >= 0 and home_movement_x <= 338:
                if button_a.is_pressed():
                    home_movement_x = home_movement_x + 5
                elif button_b.is_pressed():
                    home_movement_x = home_movement_x + -5
            elif home_movement_x <= 0:
                home_movement_x = home_movement_x + 1
            elif home_movement_x >= 338:
                home_movement_x = home_movement_x + -1
            if home_movement_x >= 0 and home_movement_x <= 46:
                app_name = '天气'
                app_mader_name = '系统'
                if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                    OS_3_5_system_consani_expand_x = home_movement_x
                    OS_3_5_system_consani_expand_y = system_interface_y + home_movement_y
                    OS_3_5_system_consani_expand_width = home_icon_edge
                    OS_3_5_system_consani_expand_tall = home_icon_edge
                    OS_3_5_system_consani_expand_corner = home_icon_fillet
                    consani_V2_expand_enter()
                    if my_wifi.sta.isconnected():
                        WeatherKit = get_seni_weather("https://api.seniverse.com/v3/weather/daily.json?key=SMhSshUxuTL0GLVLS", "ip")
                        system_notification_detail = '请接入互联网'
                        system_notification_source = '天气'
                        app_weather_location = str(WeatherKit["results"][0]["location"]["name"])
                        app_weather_report = str(WeatherKit["results"][0]["daily"][0]["text_day"])
                        app_weather_forecast_temperature = ''.join([str(x) for x in [WeatherKit["results"][0]["daily"][0]["low"], '°C', '~', WeatherKit["results"][0]["daily"][0]["high"], '°C']])
                    else:
                        oled.DispChar(str('请在掌控板接入互联网后重试'), 5, (system_interface_y + 15), 1, True)
                        app_weather_location = '--'
                        app_weather_report = '--'
                        app_weather_forecast_temperature = '--'
                    if system_app_weather_resetmode == 0:
                        system_app_weather_resetmode = 1
                        app_weather_forecast_temperature = '3日预报'
                        app_weather_location = '定位'
                        app_weather_report = '今日天气'
                    elif system_app_weather_resetmode == 1:
                        pass
                    while True:
                        oled.fill(0)
                        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                            break
                        oled.DispChar(str(app_name), 5, (system_interface_y + 3), 1)
                        oled.circle(84, (system_interface_y + 10), 2, 1)
                        oled.DispChar(str((''.join([str(x) for x in [system_time_hour, ':', system_time_minute]]))), 91, (system_interface_y + 3), 1)
                        oled.DispChar(str((''.join([str(x) for x in [app_weather_location, '，', app_weather_report]]))), 5, (system_interface_y + 15), 1, True)
                        oled.DispChar(str((str(app_weather_forecast_temperature))), 5, (system_interface_y + 30), 1, True)
                        oled.hline(44, 61, 40, 1)
                        oled.show()
            elif home_movement_x >= 47 and home_movement_x <= 75:
                app_name = '设置'
                app_mader_name = '系统'
                if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                    OS_3_5_system_consani_expand_x = home_movement_x - 40
                    OS_3_5_system_consani_expand_y = system_interface_y + home_movement_y
                    OS_3_5_system_consani_expand_width = home_icon_edge
                    OS_3_5_system_consani_expand_tall = home_icon_edge
                    OS_3_5_system_consani_expand_corner = home_icon_fillet
                    consani_V2_expand_enter()
                    if app_settings_resetmode == 0:
                        app_settings_resetmode = 1
                        app_settings_item_1 = '显示'
                        app_settings_item_2 = '锁屏'
                        app_settings_item_3 = '关于'
                        app_settings_selection_item = 1
                        system_app_settings_display_mode = '深色'
                        system_app_settings_lockscreen_style = '新版'
                        OS_3_5_app_settings_chosen = 1
                        OS_3_5_app_settings_chosen_name = '选中的设置项'
                        OS_3_5_app_settings_icon_y = 20
                    elif app_settings_resetmode == 1:
                        pass
                    while True:
                        oled.fill(0)
                        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                            while not (touchpad_p.is_pressed() and touchpad_y.is_pressed()):
                                pass
                            break
                        if button_a.is_pressed() and button_b.is_pressed():
                            system_interface_y = 20
                            oled.fill_rect(0, 0, 128, 20, 1)
                            oled.DispChar(str((''.join([str(x) for x in [system_notification_detail, '——来自', system_notification_source]]))), 5, 3, 2)
                        else:
                            system_interface_y = 0
                        oled.DispChar(str(app_name), 5, (system_interface_y + 3), 1)
                        oled.DispChar(str((''.join([str(x) for x in [system_time_hour, ':', system_time_minute]]))), 91, (system_interface_y + 3), 1)
                        if OS_3_5_app_settings_chosen >= 1 and OS_3_5_app_settings_chosen <= 3:
                            if button_a.is_pressed():
                                OS_3_5_app_settings_chosen = OS_3_5_app_settings_chosen + -1
                            if button_b.is_pressed():
                                OS_3_5_app_settings_chosen = OS_3_5_app_settings_chosen + 1
                        else:
                            if OS_3_5_app_settings_chosen < 1:
                                OS_3_5_app_settings_chosen = 1
                            if OS_3_5_app_settings_chosen > 3:
                                OS_3_5_app_settings_chosen = 3
                        if OS_3_5_app_settings_chosen == 1:
                            OS_3_5_app_settings_chosen_name = app_settings_item_1
                            oled.RoundRect(110, ((system_interface_y + OS_3_5_app_settings_icon_y) + 0), 35, 35, 7, 1)
                            oled.RoundRect(113, ((system_interface_y + OS_3_5_app_settings_icon_y) + 3), 29, 29, 5, 1)
                        elif OS_3_5_app_settings_chosen >= 2 and OS_3_5_app_settings_chosen <= 2:
                            oled.RoundRect(110, ((system_interface_y + OS_3_5_app_settings_icon_y) + 0), 35, 35, 7, 1)
                            oled.RoundRect(113, ((system_interface_y + OS_3_5_app_settings_icon_y) + 3), 29, 29, 5, 1)
                            oled.RoundRect((-10), ((system_interface_y + OS_3_5_app_settings_icon_y) + 0), 35, 35, 7, 1)
                            oled.RoundRect((-7), ((system_interface_y + OS_3_5_app_settings_icon_y) + 3), 29, 29, 5, 1)
                            if OS_3_5_app_settings_chosen == 2:
                                OS_3_5_app_settings_chosen_name = app_settings_item_2
                        elif OS_3_5_app_settings_chosen == 3:
                            oled.RoundRect((-10), ((system_interface_y + OS_3_5_app_settings_icon_y) + 0), 35, 35, 7, 1)
                            oled.RoundRect((-7), ((system_interface_y + OS_3_5_app_settings_icon_y) + 3), 29, 29, 5, 1)
                            OS_3_5_app_settings_chosen_name = app_settings_item_3
                        if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                            OS_3_5_system_consani_expand_x = 30
                            OS_3_5_system_consani_expand_y = (system_interface_y + OS_3_5_app_settings_icon_y) + 0
                            OS_3_5_system_consani_expand_width = 75
                            OS_3_5_system_consani_expand_tall = 35
                            OS_3_5_system_consani_expand_corner = 7
                            consani_V2_expand_enter()
                            if OS_3_5_app_settings_chosen == 1:
                                while not (touchpad_p.is_pressed() and touchpad_y.is_pressed()):
                                    oled.fill(0)
                                    if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                                        if system_app_settings_display_mode == '深色':
                                            system_app_settings_display_mode = '浅色'
                                            oled.invert(1)
                                        elif system_app_settings_display_mode == '浅色':
                                            system_app_settings_display_mode = '深色'
                                            oled.invert(0)
                                    oled.DispChar(str((''.join([str(x) for x in [app_name, '-', OS_3_5_app_settings_chosen_name]]))), 5, (system_interface_y + 3), 1)
                                    oled.DispChar(str((''.join([str(x) for x in [system_time_hour, ':', system_time_minute]]))), 91, (system_interface_y + 3), 1)
                                    oled.DispChar(str((str(system_app_settings_display_mode) + '模式')), 91, (system_interface_y + 15), 1)
                                    oled.DispChar(str('TH切换'), 91, (system_interface_y + 30), 1)
                                    oled.hline(44, 61, 40, 1)
                                    oled.show()
                                while touchpad_p.is_pressed() and touchpad_y.is_pressed():
                                    pass
                            elif OS_3_5_app_settings_chosen == 2:
                                while not (touchpad_p.is_pressed() and touchpad_y.is_pressed()):
                                    oled.fill(0)
                                    if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                                        if system_app_settings_lockscreen_style == '新版':
                                            system_app_settings_lockscreen_style = '经典'
                                        elif system_app_settings_lockscreen_style == '经典':
                                            system_app_settings_lockscreen_style = '新版'
                                    oled.DispChar(str((''.join([str(x) for x in [app_name, '-', OS_3_5_app_settings_chosen_name]]))), 5, (system_interface_y + 3), 1)
                                    oled.DispChar(str((''.join([str(x) for x in [system_time_hour, ':', system_time_minute]]))), 91, (system_interface_y + 3), 1)
                                    oled.DispChar(str((str(system_app_settings_display_mode) + '样式')), 91, (system_interface_y + 15), 1)
                                    oled.DispChar(str('TH切换'), 91, (system_interface_y + 30), 1)
                                    oled.hline(44, 61, 40, 1)
                                    oled.show()
                                while touchpad_p.is_pressed() and touchpad_y.is_pressed():
                                    pass
                            elif OS_3_5_app_settings_chosen == 3:
                                while not (touchpad_p.is_pressed() and touchpad_y.is_pressed()):
                                    oled.fill(0)
                                    oled.DispChar(str((''.join([str(x) for x in [app_name, '-', OS_3_5_app_settings_chosen_name]]))), 5, (system_interface_y + 3), 1)
                                    oled.DispChar(str((''.join([str(x) for x in [system_time_hour, ':', system_time_minute]]))), 91, (system_interface_y + 3), 1)
                                    oled.DispChar(str((''.join([str(x) for x in [system_core, ' ', system_version]]))), 5, (system_interface_y + 15), 1)
                                    oled.DispChar(str(('系统大小：' + str(system_core_size))), 5, (system_interface_y + 30), 1)
                                    oled.DispChar(str((str(OS_3_5_system_category) + '系统')), 5, (system_interface_y + 45), 1)
                                    oled.hline(44, 61, 40, 1)
                                    oled.show()
                                while touchpad_p.is_pressed() and touchpad_y.is_pressed():
                                    pass
                        oled.RoundRect(30, ((system_interface_y + OS_3_5_app_settings_icon_y) + 0), 75, 35, 7, 1)
                        oled.RoundRect(33, ((system_interface_y + OS_3_5_app_settings_icon_y) + 3), 29, 29, 5, 1)
                        oled.DispChar(str(OS_3_5_app_settings_chosen_name), 67, ((system_interface_y + OS_3_5_app_settings_icon_y) + 11), 1)
                        oled.hline(44, 61, 40, 1)
                        oled.show()
            elif home_movement_x >= 75 and home_movement_x <= 118:
                app_name = '木鱼'
                app_mader_name = '恺撒！'
                if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                    OS_3_5_system_consani_expand_x = home_movement_x - 80
                    OS_3_5_system_consani_expand_y = system_interface_y + home_movement_y
                    OS_3_5_system_consani_expand_width = home_icon_edge
                    OS_3_5_system_consani_expand_tall = home_icon_edge
                    OS_3_5_system_consani_expand_corner = home_icon_fillet
                    consani_V2_expand_enter()
                    if system_app_woodenfish_resetmode == 0:
                        app_woodenfish_times = 0
                        system_app_woodenfish_resetmode = 1
                    elif system_app_woodenfish_resetmode == 1:
                        pass
                    while True:
                        oled.fill(0)
                        if _is_shaked:
                            music.play('E3:1')
                            app_woodenfish_times = app_woodenfish_times + 1
                        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                            while not (touchpad_p.is_pressed() and touchpad_y.is_pressed()):
                                pass
                            break
                        if button_a.is_pressed() and button_b.is_pressed():
                            system_interface_y = 20
                            oled.fill_rect(0, 0, 128, 20, 1)
                            oled.DispChar(str((''.join([str(x) for x in [system_notification_detail, '——来自', system_notification_source]]))), 5, 3, 2)
                        else:
                            system_interface_y = 0
                        system_notification_detail = str('今日已敲') + str(app_woodenfish_times)
                        system_notification_source = '木鱼'
                        oled.DispChar(str(app_name), 5, (system_interface_y + 3), 1)
                        oled.DispChar(str((''.join([str(x) for x in [system_time_hour, ':', system_time_minute]]))), 91, (system_interface_y + 3), 1)
                        oled.DispChar(str('摇一摇。'), 5, (system_interface_y + 15), 1, True)
                        oled.DispChar(str('——静心——'), 5, (system_interface_y + 30), 1, True)
                        oled.DispChar(str(str(str('今日已敲') + str(app_woodenfish_times)) + str('次。')), 5, (system_interface_y + 45), 1, True)
                        oled.hline(44, 61, 40, 1)
                        oled.show()
            elif home_movement_x >= 119 and home_movement_x <= 162:
                app_name = '照明'
                app_mader_name = '系统'
                if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                    OS_3_5_system_consani_expand_x = home_movement_x - 120
                    OS_3_5_system_consani_expand_y = system_interface_y + home_movement_y
                    OS_3_5_system_consani_expand_width = home_icon_edge
                    OS_3_5_system_consani_expand_tall = home_icon_edge
                    OS_3_5_system_consani_expand_corner = home_icon_fillet
                    consani_V2_expand_enter()
                    if system_app_lighting_resetmode == 0:
                        app_lighting_brightness = 'null'
                        app_lighting_mode = 'null'
                        system_app_lighting_resetmode = 1
                    elif system_app_lighting_resetmode == 1:
                        pass
                    while True:
                        oled.fill(0)
                        if light.read() == 0:
                            rgb.fill((int(102), int(51), int(0)))
                            rgb.write()
                            time.sleep_ms(1)
                            app_lighting_mode = '夜灯'
                            app_lighting_brightness = '微弱'
                            system_notification_detail = '夜灯模式'
                            system_notification_source = '照明'
                        elif light.read() >= 1 and light.read() < 49:
                            rgb.fill((int(255), int(153), int(0)))
                            rgb.write()
                            time.sleep_ms(1)
                            app_lighting_mode = '夜灯'
                            app_lighting_brightness = '一般'
                            system_notification_detail = '夜灯模式'
                            system_notification_source = '照明'
                        elif light.read() >= 50 and light.read() < 249:
                            rgb.fill((int(51), int(51), int(51)))
                            rgb.write()
                            time.sleep_ms(1)
                            app_lighting_mode = '照明'
                            app_lighting_brightness = '微弱'
                            system_notification_detail = '照明模式'
                            system_notification_source = '照明'
                        elif light.read() >= 250 and light.read() < 649:
                            rgb.fill((int(102), int(102), int(102)))
                            rgb.write()
                            time.sleep_ms(1)
                            app_lighting_mode = '照明'
                            app_lighting_brightness = '微弱'
                            system_notification_detail = '照明模式'
                            system_notification_source = '照明'
                        elif light.read() >= 650 and light.read() < 1199:
                            rgb.fill((int(153), int(153), int(153)))
                            rgb.write()
                            time.sleep_ms(1)
                            app_lighting_mode = '照明'
                            app_lighting_brightness = '一般'
                            system_notification_detail = '照明模式'
                            system_notification_source = '照明'
                        elif light.read() >= 1200 and light.read() < 2549:
                            rgb.fill((int(153), int(153), int(153)))
                            rgb.write()
                            time.sleep_ms(1)
                            app_lighting_mode = '照明'
                            app_lighting_brightness = '一般'
                            system_notification_detail = '照明模式'
                            system_notification_source = '照明'
                        else:
                            rgb.fill( (0, 0, 0) )
                            rgb.write()
                            time.sleep_ms(1)
                            app_lighting_mode = '关闭'
                            app_lighting_brightness = '无'
                            system_notification_detail = '灯已熄灭'
                            system_notification_source = '照明'
                        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                            rgb.fill( (0, 0, 0) )
                            rgb.write()
                            time.sleep_ms(1)
                            while not (touchpad_p.is_pressed() and touchpad_y.is_pressed()):
                                pass
                            break
                        oled.DispChar(str(app_name), 5, (system_interface_y + 3), 1)
                        oled.circle(84, (system_interface_y + 10), 2, 1)
                        oled.DispChar(str((''.join([str(x) for x in [system_time_hour, ':', system_time_minute]]))), 91, (system_interface_y + 3), 1)
                        oled.DispChar(str((str(app_lighting_brightness) + '模式')), 5, (system_interface_y + 15), 1, True)
                        oled.DispChar(str(('亮度' + str(app_lighting_mode))), 5, (system_interface_y + 30), 1, True)
                        oled.hline(44, 61, 40, 1)
                        oled.show()
            elif home_movement_x >= 163 and home_movement_x <= 206:
                app_name = '应用定制'
                app_mader_name = '恺撒！'
                if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                    OS_3_5_system_consani_expand_x = home_movement_x - 160
                    OS_3_5_system_consani_expand_y = system_interface_y + home_movement_y
                    OS_3_5_system_consani_expand_width = home_icon_edge
                    OS_3_5_system_consani_expand_tall = home_icon_edge
                    OS_3_5_system_consani_expand_corner = home_icon_fillet
                    consani_V2_expand_enter()
                    if system_app_system_resetmode == 0:
                        system_app_system_resetmode = 1
                    elif system_app_system_resetmode == 1:
                        pass
                    while True:
                        oled.fill(0)
                        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                            while not (touchpad_p.is_pressed() and touchpad_y.is_pressed()):
                                pass
                            break
                        if button_a.is_pressed() and button_b.is_pressed():
                            system_interface_y = 20
                            oled.fill_rect(0, 0, 128, 20, 1)
                            oled.DispChar(str((''.join([str(x) for x in [system_notification_detail, '——来自', system_notification_source]]))), 5, 3, 2)
                        else:
                            system_interface_y = 0
                        oled.DispChar(str(app_name), 5, (system_interface_y + 3), 1)
                        oled.DispChar(str((''.join([str(x) for x in [system_time_hour, ':', system_time_minute]]))), 91, (system_interface_y + 3), 1)
                        myUI.qr_code('https://tracey5140.hocoos.com/contact-us?id=890176', 5, (system_interface_y + 15), scale=2)
                        oled.hline(44, 61, 40, 1)
                        oled.show()
            elif home_movement_x >= 207 and home_movement_x <= 250:
                app_name = '应用定制'
                app_mader_name = '恺撒！'
                if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                    OS_3_5_system_consani_expand_x = home_movement_x - 200
                    OS_3_5_system_consani_expand_y = system_interface_y + home_movement_y
                    OS_3_5_system_consani_expand_width = home_icon_edge
                    OS_3_5_system_consani_expand_tall = home_icon_edge
                    OS_3_5_system_consani_expand_corner = home_icon_fillet
                    consani_V2_expand_enter()
                    if system_app_system_resetmode == 0:
                        system_app_system_resetmode = 1
                    elif system_app_system_resetmode == 1:
                        pass
                    while True:
                        oled.fill(0)
                        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                            while not (touchpad_p.is_pressed() and touchpad_y.is_pressed()):
                                pass
                            break
                        if button_a.is_pressed() and button_b.is_pressed():
                            system_interface_y = 20
                            oled.fill_rect(0, 0, 128, 20, 1)
                            oled.DispChar(str((''.join([str(x) for x in [system_notification_detail, '——来自', system_notification_source]]))), 5, 3, 2)
                        else:
                            system_interface_y = 0
                        oled.DispChar(str(app_name), 5, (system_interface_y + 3), 1)
                        oled.DispChar(str((''.join([str(x) for x in [system_time_hour, ':', system_time_minute]]))), 91, (system_interface_y + 3), 1)
                        myUI.qr_code('https://tracey5140.hocoos.com/contact-us?id=890176', 5, (system_interface_y + 15), scale=2)
                        oled.hline(44, 61, 40, 1)
                        oled.show()
            elif home_movement_x >= 251 and home_movement_x <= 294:
                app_name = '应用定制'
                app_mader_name = '恺撒！'
                if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                    OS_3_5_system_consani_expand_x = home_movement_x - 240
                    OS_3_5_system_consani_expand_y = system_interface_y + home_movement_y
                    OS_3_5_system_consani_expand_width = home_icon_edge
                    OS_3_5_system_consani_expand_tall = home_icon_edge
                    OS_3_5_system_consani_expand_corner = home_icon_fillet
                    consani_V2_expand_enter()
                    if system_app_system_resetmode == 0:
                        system_app_system_resetmode = 1
                    elif system_app_system_resetmode == 1:
                        pass
                    while True:
                        oled.fill(0)
                        if touchpad_p.is_pressed() and touchpad_y.is_pressed():
                            while not (touchpad_p.is_pressed() and touchpad_y.is_pressed()):
                                pass
                            break
                        if button_a.is_pressed() and button_b.is_pressed():
                            system_interface_y = 20
                            oled.fill_rect(0, 0, 128, 20, 1)
                            oled.DispChar(str((''.join([str(x) for x in [system_notification_detail, '——来自', system_notification_source]]))), 5, 3, 2)
                        else:
                            system_interface_y = 0
                        oled.DispChar(str(app_name), 5, (system_interface_y + 3), 1)
                        oled.DispChar(str((''.join([str(x) for x in [system_time_hour, ':', system_time_minute]]))), 91, (system_interface_y + 3), 1)
                        myUI.qr_code('https://tracey5140.hocoos.com/contact-us?id=890176', 5, (system_interface_y + 15), scale=2)
                        oled.hline(44, 61, 40, 1)
                        oled.show()
            elif home_movement_x >= 295 and home_movement_x <= 338:
                app_name = '锁屏'
                app_mader_name = '系统'
                if touchpad_t.is_pressed() and touchpad_h.is_pressed():
                    OS_3_5_system_consani_expand_x = home_movement_x - 280
                    OS_3_5_system_consani_expand_y = system_interface_y + home_movement_y
                    OS_3_5_system_consani_expand_width = home_icon_edge
                    OS_3_5_system_consani_expand_tall = home_icon_edge
                    OS_3_5_system_consani_expand_corner = home_icon_fillet
                    Consani_V2_level_leave()
                    system_homemode = 1
                    break
            oled.RoundRect(home_movement_x, (system_interface_y + home_movement_y), home_icon_edge, home_icon_edge, home_icon_fillet, 1)
            oled.RoundRect((home_movement_x - 40), (system_interface_y + home_movement_y), home_icon_edge, home_icon_edge, home_icon_fillet, 1)
            oled.RoundRect((home_movement_x - 80), (system_interface_y + home_movement_y), home_icon_edge, home_icon_edge, home_icon_fillet, 1)
            oled.RoundRect((home_movement_x - 120), (system_interface_y + home_movement_y), home_icon_edge, home_icon_edge, home_icon_fillet, 1)
            oled.RoundRect((home_movement_x - 160), (system_interface_y + home_movement_y), home_icon_edge, home_icon_edge, home_icon_fillet, 1)
            oled.RoundRect((home_movement_x - 200), (system_interface_y + home_movement_y), home_icon_edge, home_icon_edge, home_icon_fillet, 1)
            oled.RoundRect((home_movement_x - 240), (system_interface_y + home_movement_y), home_icon_edge, home_icon_edge, home_icon_fillet, 1)
            oled.RoundRect((home_movement_x - 280), (system_interface_y + home_movement_y), home_icon_edge, home_icon_edge, home_icon_fillet, 1)
            oled.hline(44, 61, 40, 1)
            oled.show()
