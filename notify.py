from win11toast import toast

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# toast('Arslan Arshad')

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# toast('Arslan Arshad', 'GitHub', on_click='https://github.com/ArslanArshad24')

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
icon = {
    'src': 'https://unsplash.it/64?image=669',
    # 'placement': 'appLogoOverride' for Square image
}
# toast('Arslan Arshad', 'GitHub',icon=icon)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
image = {
    'src': 'https://4.bp.blogspot.com/-u-uyq3FEqeY/UkJLl773BHI/AAAAAAAAYPQ/7bY05EeF1oI/s800/cooking_toaster.png',
    # 'placement': 'hero' for hero simg
}
# toast('Arslan Arshad', 'Hello from Python', image=image)
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# toast('Arslan Arshad', 'Hello from Python', audio='https://nyanpass.com/nyanpass.mp3')

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# toast('Arslan Arshad', dialogue='Hello Arslan! How are You?')

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# from time import sleep
# from win11toast import notify, update_progress

# notify(progress={
#     'title': 'YouTube',
#     'status': 'Downloading...',
#     'value': '0',
#     'valueStringOverride': '0/15 videos'
# })

# for i in range(1, 15+1):
#     sleep(1)
#     update_progress({'value': i/15, 'valueStringOverride': f'{i}/15 videos'})

# update_progress({'status': 'Completed!'})

######%%%%%%%%%%%%%%%%%%%%%%%%%%%
Button =[{
    'activationType': 'protocol', 
    'arguments': 'https://github.com/ArslanArshad24', 
    'content': 'Open Github'
},
{
    'activationType': 'protocol', 
    'arguments': 'Dismiss', 
    'content': 'Dismiss'
}]
toast('Arslan Arshad', 'Hello from Github', buttons=Button)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# toast('Hello', 'Type anything', input='reply', button='Send')
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Button=button={
    'activationType': 'protocol', 
    'arguments': 'http:', 
    'content': 'Send', 
    'hint-inputId': 'reply'
}
# toast('Hello', 'Type anything', input='reply',button=Button )
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# toast('Hello', 'Which do you like?', selection=['Apple', 'Banana', 'Grape'], button='Submit')
