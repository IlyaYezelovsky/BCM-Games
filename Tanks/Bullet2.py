import Kitten 

def Shot2():
  Kitten.show()
  Kitten.move_to('坦克2')
  Kitten.set_rotation(Kitten.value_of_object('坦克2', 'rotation'))
  while True :
    Kitten.move_forward(8)
    if (Kitten.is_touched('Self', '坦克1') or Kitten.is_touched('Self', '炮弹1') or Kitten.is_touched('Self', 'edge')) :
      Kitten.hide()
      break

def when_get_signal(signal):
  if signal == 'V1':
    Kitten.stop_code('self_others')

def when_get_signal(signal):
  if signal == 'Restart':
    Kitten.restart_project()
