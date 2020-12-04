from nntplib import NNTP
servername = 'web.aioe.org'
group = 'comp.lang.python.announce'
server = NNTP(servername)
howmany = 1
resp, count, first, last, name = server.group(group)
print(f'resp:{resp},count:{count},first{first},last{last},name{name}')
start = last - howmany + 1
resp, overviews = server.over((start, last))
print(resp)
for id, over in overviews:
    print(f'id:{id},over:{over}')
    subject = over['subject']
    print(f"11111111111{subject}")
    resp, info = server.body(id)
    print(f'resp:{resp},info:{info}')
    print('-' * len(subject))
    for line in info.lines:
        print(f"22222  {line.decode('latin')}")
    print(3333)
server.quit()