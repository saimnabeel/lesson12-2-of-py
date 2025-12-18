text=open('text.txt','w')
paste=open('texto.txt','r')
lines_seen_so_far=set()
print("deleting duplicates")
for line in text:
    if line not in lines_seen_so_far:
        text.write(line)
        lines_seen_so_far.add(line)
text.close()
paste.close()  