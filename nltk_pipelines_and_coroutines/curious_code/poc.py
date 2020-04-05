from coro import coroutine, follow, printer, grep


log = open('follow_me.log')
follow(log, 
        grep('NOTE',
            printer()))
            
