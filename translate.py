from translation import google, ConnectError

# print(google('This is Sachin Here', dst = 'hi'))
#  Tkinter import *
import Tkinter
de_blob = TextBlob(u"How are you reading this post right now? It might be on desktop, on mobile, maybe a tablet, but whatever device you’re using, it’s most definitely connected to the internet.An internet connection is a wonderful thing, it give us all sorts of benefits that just weren’t possible before. If you’re old enough, think of your cellphone before it was a smartphone. You could call and you could text sure, but now you can read any book, watch any movie, or listen to any song all in the palm of your hand. And that’s just to name a few of the incredible things your smartphone can do.")

# print(de_blob.translate(to='hi'))
# print(de_blob)
window = Tk()
window.title("Welcome to LikeGeeks app")
 
lbl = Label(window, text=fig)
 
lbl.grid(column=0, row=0)
 
window.mainloop()