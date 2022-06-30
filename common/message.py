from termcolor import colored
def message(a):
    #''.center(100,'*')
    #print(a)
    print()
    print (colored(a, 'green'))
    try:
        #import telepot
        import telegram_send
#telegram_send.send(messages=["Wow that was easy!"])
    except:
        try:
            import pip
            pip.main(['install', 'telegram_send'])
            #!pip install telepot
        except Exception as e:
            print(e)
            print('install telegram_send pip package ')
            TOKEN = "5513632066:AAFZgJhCe1t7-T2ias3GkwVFgTD9Cd4_4Ic"  #Enter token of telegram , it will notify during order updates
            chat_id = "898401520"   #chatid in telegram 
    try:
        telegram_send.send(messages=[a])
        #telegram_send.send(messages=["Welcome Ravi"])
        #import telepot
        #bot = telepot.Bot(TOKEN)#"Wow that was easy!"
    except Exception as e:
        print(e)
        print('unable to send message')