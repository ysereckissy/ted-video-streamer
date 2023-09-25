from kivy.app import App

from video import Video


class KivyPlayerApp(App):

    def build(self):
        self.video = Video()
        self.video.bind(on_touch_down=self.touch_down)
        return self.video

    def touch_down(self, instance, touch):
        if self.video.state == 'play':
            self.video.state = 'pause'
        else:
            self.video.state = 'stop'


if __name__ == "__main__":
    KivyPlayerApp().run()
