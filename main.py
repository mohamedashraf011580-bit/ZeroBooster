from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import os
import random

class Booster(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.padding = 20
        self.spacing = 20

        title = Label(
            text="ZERO BOOSTER X",
            font_size=30
        )

        self.info = Label(
            text="READY",
            font_size=22
        )

        boost_btn = Button(
            text="BOOST DEVICE",
            font_size=20
        )

        clean_btn = Button(
            text="CLEAN CACHE",
            font_size=20
        )

        fps_btn = Button(
            text="CHECK FPS",
            font_size=20
        )

        boost_btn.bind(on_press=self.boost)
        clean_btn.bind(on_press=self.clean)
        fps_btn.bind(on_press=self.fps)

        self.add_widget(title)
        self.add_widget(self.info)
        self.add_widget(boost_btn)
        self.add_widget(clean_btn)
        self.add_widget(fps_btn)

    def boost(self, instance):

        os.system("am kill-all")

        self.info.text = "BOOST COMPLETE"

    def clean(self, instance):

        os.system("rm -rf /data/data/com.termux/cache/*")

        self.info.text = "CACHE CLEANED"

    def fps(self, instance):

        fps = random.randint(50, 90)

        self.info.text = f"FPS: {fps}"


class ZeroApp(App):

    def build(self):
        return Booster()

ZeroApp().run()
