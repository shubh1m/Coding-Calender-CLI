from urllib.request import urlopen, Request
import json
import os

def main():
    BASE_URL = 'https://contesttrackerapi.herokuapp.com/'
    headers = {
        'Accept' : 'Application/json'
    }

    req = Request(BASE_URL, headers=headers)
    response_body = urlopen(req).read().decode('utf-8')
    readable = json.loads(response_body)

    ongoing = readable['result']['ongoing']
    upcoming = readable['result']['upcoming']

    print('\n')
    star()
    print ('{:>{}}'.format('LIVE CONTESTS', cols/3 + 30))
    star()

    #print ('{:>{}}'.format('LIVE CONTESTS', cols/3 + 30))
    print ('{:<5}{:<50}{:^20}{:<60}\n'.format('INDEX','NAME', 'PLATFORM', 'LINK TO CONTEST'))

    for i in range(len(ongoing)-2):
        contest = ongoing[i]
        print ('{:<5}{:<50}{:^20}{:<60}'.format(i+1, contest['Name'], contest['Platform'], contest['url']))

    #print('\n')
    #star()
    #print ('{:>{}}'.format('UPCOMING CONTESTS', cols/3 + 30))
    #star()

    #for i in range(len(upcoming)):
    #    contest = upcoming[i]
    #    print ('{:<8}{:<50}{:^20}{:<60}'.format(i+1, contest['Name'], contest['Platform'], contest['url']))


def star():
    global cols
    rows,cols = os.popen('stty size', 'r').read().split()
    cols = int(cols)
    print ( '*'*cols )


if __name__ == '__main__':
    main()
