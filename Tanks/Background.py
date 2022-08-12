import Kitten 

def when_get_signal(signal):
  if signal == 'V1':
    Kitten.change_shape('V1')
		# 如果得到广播V1,就切换造型到V1

def when_get_signal(signal):
  if signal == 'V2':
    Kitten.change_shape('V2')
		# 如果得到广播V2,就切换造型到V2

def when():
  while True:
    if (Kitten.value_of_object('Self', 'style_index') == 2 and Kitten.is_key_pressed(32)):
			# 32号是空格键
      Kitten.change_shape('坦克大战-背景')
			# 重新开始，切换到原来背景
      def call_events_of(name_ = '坦克1'):
        Kitten.show()

      call_events_of()
      def call_events_of(name_ = '坦克2'):
        Kitten.show()


      call_events_of()
      Kitten.send_signal('Restart')

def when():
  while True:
    if (Kitten.value_of_object('Self', 'style_index') == 3 and Kitten.is_key_up(32)):
      Kitten.change_shape('坦克大战-背景')
      def call_events_of(name_ = '坦克1'):
        Kitten.show()


      call_events_of()
      def call_events_of(name_ = '坦克2'):
        Kitten.show()


      call_events_of()
      Kitten.send_signal('Restart')
