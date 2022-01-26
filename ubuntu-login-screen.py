#!/usr/bin/python3

import os, sys, subprocess
from unsplash.api import Api
from unsplash.photo import Photo
from unsplash.auth import Auth
from urllib import request


with open('ubuntu_gdm_set_background.sh', 'r') as script:
    ubuntu_gdm_set_background = script.read()


def add_to_autostart():
    
    subprocess.call(['/bin/bash', '-c', f"chmod +x {__file__}"])

    
    desktopfile = f"""[Desktop Entry]
    Type=Application

    Version=1.0

    Name=Ubuntu Login Screen

    Comment=Login Screen Wallpapers (ubuntu 21.10)

    Path={os.path.expanduser('~')}

    Exec={__file__}

    Categories=Utilities;

    """ 

    with open(os.path.join(os.path.expanduser('~/.config/autostart/'), 'ubuntu-login-screen.desktop'), 'w') as script:
        script.write(desktopfile)


def download_photo(api, photo):
    photos = api.photo.random(query="dark background", orientation="landscape")

    downloadLink = photo.download(photos[0].id)

    if not os.path.exists(f"{os.path.expanduser('~')}/.ubuntu-login-screen/"):
        os.mkdir(f"{os.path.expanduser('~')}/.ubuntu-login-screen/")

    request.urlretrieve(downloadLink['url'], f"{os.path.expanduser('~')}/.ubuntu-login-screen/bg.jpg")

def set_login_screen_bg():
    
    with open(os.path.join(os.path.expanduser('~/.ubuntu-login-screen/'), 'ubuntu_gdm_set_background.sh'), 'w') as script:
        script.write(ubuntu_gdm_set_background)
    
    subprocess.call(['/bin/bash', '-c', "chmod +x $HOME/.ubuntu-login-screen/ubuntu_gdm_set_background.sh"])
    subprocess.call(['/bin/bash', '-c', "sudo $HOME/.ubuntu-login-screen/ubuntu_gdm_set_background.sh --image $HOME/.ubuntu-login-screen/bg.jpg"])


def main(client_id, client_secret, redirect_uri):
    
    try:
        auth = Auth(client_id, client_secret, redirect_uri)
        api = Api(auth)
        photo = Photo(api=api)
    except:
        print('Incorrect or insufficient parameters passed')
        return None
    
    print('. . .')
        
    try:
        download_photo(api, photo)
    except Exception as e:
        print("image downloaded failed, please check your network connection")
        print(e)   
    else:
        print("image downloaded")
        
    try:
        set_login_screen_bg()
    except Exception as e:
        print("there was some error in setting the bg")
        print(e)   
    else:
        print("background changed successfully")
    
    try:
        add_to_autostart()
    except Exception as e:
        print("failed to add program to autostart")
        print(e)   
    else:
        print("added program to autostart")
    
    try:
        with open(os.path.join(os.path.expanduser('~/.ubuntu-login-screen/'), 'keys.txt'), 'w') as file:
            file.write(f'{client_id}\n{client_secret}\n{redirect_uri}')
            
    except:
        
        print("couldn't cache unsplash keys")
        
    else:
        print("cached unsplash keys")
        


if __name__ == '__main__':
        
        try:
            if sys.argv[1] == '--help':
                print("Run the command as follows for the first time ->\npython3 ubuntu-login-screen.py <client_id> <client_secret> <redirect_uri>\nAfter first use, application will be added to autostart and keys will be cached.")

        except:
            pass
        
        else:
            sys.exit()
    
        if len(sys.argv)>3:
                
            main(client_id=sys.argv[1], client_secret=sys.argv[2], redirect_uri=sys.argv[3])
            
        else:
            
            try:

                with open(os.path.join(os.path.expanduser('~/.ubuntu-login-screen/'), 'keys.txt'), 'r') as file:
                    keys = file.readlines()
                    main(client_id=keys[0].strip('\n'), client_secret=keys[1].strip('\n'), redirect_uri=keys[2].strip('\n'))
                    
            except Exception as e:

                print('Incorrect or insufficient parameters passed, no cached keys found\n use --help for more info')
            
