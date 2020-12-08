from tkinter import *
root=Tk()
text=Text(root, width=40, height=10)
text.pack()

#multiline input
text.config(wrap='word')
print(text.get('1.0', 'end'))
(text.get('1.0', '1.end'))
text.insert('1.0 + 2 lines', 'Inserted message')
text.insert('1.0 + 3 lines', 'Inserted message')
text.insert('1.0 +2 lines lineend', 'and\nmore aand\nmore...')
text.delete('1.0')
text.delete('1.0' , '1.0 lineend')
#text.delete('1.0', '3.0 lineend + 1 chars')
text.replace('1.0', '1.0 lineend', 'This is the first line')
#text.config(state='disabled')
#text.delete('1.0', 'end')

#tags
text.tag_add('my_tag', '1.0', '1.0 wordend')
text.tag_configure('my_tag', background='yellow')
text.tag_remove('my_tag', '1.1', '1.3')
print (text.tag_ranges('my_tag'))
print(text.tag_names())
print(text.tag_names('1.0'))
text.replace('my_tag.first', 'my_tag.last', 'That')
text.tag_delete('my_tag')

#marks

print(text.mark_names())
text.insert('insert', '_')
text.mark_set('my_mark', 'end')
text.mark_gravity('my_mark', 'right')
text.mark_unset('my_mark')

#images

image=PhotoImage(file='python_logo.gif')
text.image_create('insert', image=image)
button=Button(text, text='Click Me')
text.window_create('insert', window=button)


root.mainloop()
