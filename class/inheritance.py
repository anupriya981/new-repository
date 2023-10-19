            #single inheritance

class whatsUp:
    def chat(self):
        print('chat')

class whatsUp_emoji(whatsUp):
    def emoji(self):
        print('emoji')
    
# y=whatsUp_emoji()
# y.chat()
# y.emoji()

            #multiple inheritance
class whatsUp_ithem(whatsUp_emoji):
    def ithem(self):
        print('ithem')

x=whatsUp_ithem()
x.chat()
x.emoji()
x.ithem()
