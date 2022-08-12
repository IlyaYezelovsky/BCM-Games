# 注释请参考Tank1.py
import Kitten 

self.hp = 5

def when():
  while True:
    if Kitten.is_touched('Self', '炮弹1'):
      hp = hp - 1

def when_press_key(keycode):
  if keycode == 85:
    Kitten.move_forward(3)
    Kitten.bounce_on_edge()



def when_get_signal(signal):
  if signal == 'Restart':
    self.hp = 5

def when():
  while True:
    if (self.hp == 0):
      Kitten.hide()
      Kitten.send_signal('V1')

def when_release_key(keycode):
  if keycode == 76:
    def call_events_of(name_ = '炮弹2'):
      Shot2()


    call_events_of()



def when_press_key(keycode):
  if keycode == 74:
    Kitten.move_forward((-2))



def when_press_key(keycode):
  if keycode == 72:
    Kitten.add_rotation(2)



def when_press_key(keycode):
  if keycode == 75:
    Kitten.add_rotation((-3))
