import Kitten 

self.hp = 5
# 生命值:5

def when_press_key(keycode):
  if keycode == 87:
    Kitten.move_forward(3)
    Kitten.bounce_on_edge()
# 87号键是W


def when():
  while True:
    if (self.hp == 0):
      Kitten.hide()
      Kitten.send_signal('V2')
# 如果自己生命值=0发送V2广播

def when_get_signal(signal):
  if signal == 'Restart':
    self.hp = 5

def when():
  while True:
    if Kitten.is_touched('Self', '炮弹2'):
      hp = hp - 1

def when_release_key(keycode):
  if keycode == 70:
    def call_events_of(name_ = '炮弹1'):
      Shot1()


    call_events_of()



def when_press_key(keycode):
  if keycode == 83:
    Kitten.move_forward((-2))



def when_press_key(keycode):
  if keycode == 65:
    Kitten.add_rotation(2)



def when_press_key(keycode):
  if keycode == 68:
    Kitten.add_rotation((-3))
