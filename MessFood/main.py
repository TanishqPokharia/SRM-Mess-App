from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import DictProperty, StringProperty, ObjectProperty
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore
import datetime
import json
import webbrowser

Window.size = (500, 700)
with open("beverages.json", 'r') as beverage_json:
    json_data = beverage_json.read()
beverage_data = json.loads(json_data)

with open('breakfast.json', 'r') as breakfast_json:
    json_data = breakfast_json.read()
breakfast_data = json.loads(json_data)

with open('lunch.json', 'r') as lunch_json:
    json_data = lunch_json.read()
lunch_data = json.loads(json_data)

with open(r'snacks.json', 'r') as snacks_json:
    json_data = snacks_json.read()
snacks_data = json.loads(json_data)

with open(r'dinner.json', 'r') as dinner_json:
    json_data = dinner_json.read()
dinner_data = json.loads(json_data)


class MenuWindow(MDScreen):

    current_day_number = datetime.datetime.now().weekday()

    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    current_day = days[current_day_number]

    breakfast = breakfast_data[current_day]
    lunch = lunch_data[current_day]
    snacks = snacks_data[current_day]
    dinner = dinner_data[current_day]

    breakfast_data1 = StringProperty("".join(breakfast[0]))
    breakfast_data2 = StringProperty("".join(breakfast[1]))
    breakfast_data3 = StringProperty("".join(breakfast[2]))
    breakfast_data4 = StringProperty("".join(breakfast[3]))
    breakfast_data5 = StringProperty("".join(breakfast[4]))
    breakfast_data6 = StringProperty("".join(breakfast[5]))
    breakfast_data7 = StringProperty("".join(breakfast[6]))
    breakfast_data8 = StringProperty("".join(breakfast[7]))
    breakfast_data9 = StringProperty("".join(breakfast[8]))
    breakfast_data10 = StringProperty("".join(beverage_data["breakfast"]))

    lunch_data1 = StringProperty("".join(lunch[0]))
    lunch_data2 = StringProperty("".join(lunch[1]))
    lunch_data3 = StringProperty("".join(lunch[2]))
    lunch_data4 = StringProperty("".join(lunch[3]))
    lunch_data5 = StringProperty("".join(lunch[4]))
    lunch_data6 = StringProperty("".join(lunch[5]))
    lunch_data7 = StringProperty("".join(lunch[6]))
    lunch_data8 = StringProperty("".join(lunch[7]))
    lunch_data9 = StringProperty("".join(lunch[8]))
    lunch_data10 = StringProperty("".join(lunch[9]))
    lunch_data11 = StringProperty("".join(lunch[10]))
    lunch_data12 = StringProperty("".join(beverage_data["lunch"]))

    snacks_data1 = StringProperty("".join(snacks))
    snacks_data2 = StringProperty("".join(beverage_data["snacks"]))

    dinner_data1 = StringProperty("".join(dinner[0]))
    dinner_data2 = StringProperty("".join(dinner[1]))
    dinner_data3 = StringProperty("".join(dinner[2]))
    dinner_data4 = StringProperty("".join(dinner[3]))
    dinner_data5 = StringProperty("".join(dinner[4]))
    dinner_data6 = StringProperty("".join(dinner[5]))
    dinner_data7 = StringProperty("".join(dinner[6]))
    dinner_data8 = StringProperty("".join(dinner[7]))
    dinner_data9 = StringProperty("".join(dinner[8]))
    dinner_data10 = StringProperty("".join(dinner[9]))
    dinner_data11 = StringProperty("".join(dinner[10]))
    dinner_data12 = StringProperty("".join(dinner[11]))
    dinner_data13 = StringProperty("".join(dinner[12]))
    dinner_data14 = StringProperty("".join(dinner[13]))
    dinner_data15 = StringProperty("".join(beverage_data["dinner"]))

    def update_menu(self, day):
        self.breakfast = breakfast_data[day]
        self.lunch = lunch_data[day]
        self.snacks = snacks_data[day]
        self.dinner = dinner_data[day]
        self.breakfast_data1 = "".join(self.breakfast[0])
        self.breakfast_data2 = "".join(self.breakfast[1])
        self.breakfast_data3 = "".join(self.breakfast[2])
        self.breakfast_data4 = ("".join(self.breakfast[3]))
        self.breakfast_data5 = ("".join(self.breakfast[4]))
        self.breakfast_data6 = ("".join(self.breakfast[5]))
        self.breakfast_data7 = ("".join(self.breakfast[6]))
        self.breakfast_data8 = ("".join(self.breakfast[7]))
        self.breakfast_data9 = ("".join(self.breakfast[8]))
        self.breakfast_data10 = ("".join(beverage_data["breakfast"]))

        self.lunch_data1 = ("".join(self.lunch[0]))
        self.lunch_data2 = ("".join(self.lunch[1]))
        self.lunch_data3 = ("".join(self.lunch[2]))
        self.lunch_data4 = ("".join(self.lunch[3]))
        self.lunch_data5 = ("".join(self.lunch[4]))
        self.lunch_data6 = ("".join(self.lunch[5]))
        self.lunch_data7 = ("".join(self.lunch[6]))
        self.lunch_data8 = ("".join(self.lunch[7]))
        self.lunch_data9 = ("".join(self.lunch[8]))
        self.lunch_data10 = ("".join(self.lunch[9]))
        self.lunch_data11 = ("".join(self.lunch[10]))
        self.lunch_data12 = ("".join(beverage_data["lunch"]))

        self.snacks_data1 = ("".join(self.snacks))
        self.snacks_data2 = ("".join(beverage_data["snacks"]))

        self.dinner_data1 = ("".join(self.dinner[0]))
        self.dinner_data2 = ("".join(self.dinner[1]))
        self.dinner_data3 = ("".join(self.dinner[2]))
        self.dinner_data4 = ("".join(self.dinner[3]))
        self.dinner_data5 = ("".join(self.dinner[4]))
        self.dinner_data6 = ("".join(self.dinner[5]))
        self.dinner_data7 = ("".join(self.dinner[6]))
        self.dinner_data8 = ("".join(self.dinner[7]))
        self.dinner_data9 = ("".join(self.dinner[8]))
        self.dinner_data10 = ("".join(self.dinner[9]))
        self.dinner_data11 = ("".join(self.dinner[10]))
        self.dinner_data12 = ("".join(self.dinner[11]))
        self.dinner_data13 = ("".join(self.dinner[12]))
        self.dinner_data14 = ("".join(self.dinner[13]))
        self.dinner_data15 = ("".join(beverage_data["dinner"]))

    def drpdown(self, caller):

        self.menu_list=[{
            "text": "Complain",
            "on_release": lambda x="Complain": self.openComplain()
        },
            {
                "text": "Change Theme",
                "on_release": lambda x="Change Theme": self.changeTheme()

             }]
        self.menu = MDDropdownMenu(items=self.menu_list, width_mult=4)

        self.menu.caller = caller
        self.menu.open()

    def openComplain(self):
        webbrowser.open("https://www.srmist.edu.in/life-at-srm/complaints-redressal/")

    def changeTheme(self):
        if self.theme_cls.theme_style == 'Dark':
                self.theme_cls.theme_style = 'Light'
        elif self.theme_cls.theme_style == 'Light':
                self.theme_cls.theme_style = 'Dark'


class WindowManager(MDScreenManager):
    pass

class ModeWindow(MDScreen):
    pass

class MessFoodApp(MDApp):
    dropdown = ObjectProperty()
    data = DictProperty()
    lunch_data = StringProperty()
    snacks_data = StringProperty()
    dinner_data = StringProperty()



    def options_callback(self):
            pass

    def callback(self, instance):
        if instance.icon == 'numeric-1-box':
            self.root.get_screen("menu").update_menu("monday")

        elif instance.icon == 'numeric-2-box':
            self.root.get_screen("menu").update_menu("tuesday")


        elif instance.icon == 'numeric-3-box':
            self.root.get_screen("menu").update_menu("wednesday")



        elif instance.icon == 'numeric-4-box':
            self.root.get_screen("menu").update_menu("thursday")



        elif instance.icon == 'numeric-5-box':
            self.root.get_screen("menu").update_menu("friday")



        elif instance.icon == 'numeric-6-box':
            self.root.get_screen("menu").update_menu("saturday")



        elif instance.icon == 'numeric-7-box':
            self.root.get_screen("menu").update_menu("sunday")



    def build(self):
        self.theme_preference = self.load_theme_preference()
        self.theme_cls.theme_style = 'Dark' if self.theme_preference == 'dark' else 'Light'
        self.title = "SRM Mess Menu"
        self.data = {
            "Monday": ['numeric-1-box',
                       "on_press", self.callback],
            "Tuesday": ['numeric-2-box',
                        "on_press", self.callback],
            "Wednesday": ['numeric-3-box',
                          "on_press", self.callback],
            "Thursday": ['numeric-4-box',
                         "on_press", self.callback],
            "Friday": ['numeric-5-box',
                       "on_press", self.callback],
            "Saturday": ['numeric-6-box',
                         "on_press", self.callback],
            "Sunday": ['numeric-7-box',
                       "on_press", self.callback]
        }

        return Builder.load_file("design.kv")

    def toggle_theme(self, active):
        self.theme_preference = 'dark' if active else 'light'
        self.save_theme_preference()
        self.theme_cls.theme_style = 'Dark' if self.theme_preference == 'dark' else 'Light'

    def load_theme_preference(self):
        store = JsonStore('theme_preference.json')
        return store.get('theme')['value'] if 'theme' in store else 'light'

    def save_theme_preference(self):
        store = JsonStore('theme_preference.json')
        store.put('theme', value=self.theme_preference)
    def open(self):
        pass

    def close(self):
        pass


if __name__ == '__main__':
    MessFoodApp().run()
