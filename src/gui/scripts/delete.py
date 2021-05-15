from kivy.app import App
from kivy.uix.video import Video
from kivy.uix.widget import Widget
 
 
 
class VideoWindow(App):
    def build(self):
 
        video = Video(source='https://www.youtube.com/watch?v=4f2A_vjEwMY')
        video.state = 'play'
        video.options = {'eos': 'loop'}
 
 
        video.allow_stretch = True
        return video
 
 
 
 
if __name__ == "__main__":
    window = VideoWindow()
    window.run()

