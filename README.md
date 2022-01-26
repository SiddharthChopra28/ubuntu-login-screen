# ubuntu-login-screen
## program for randomizing login screen background everytime you login
### script ubuntu_gdm_set_background.sh from [PRATAP-KUMAR/ubuntu-gdm-set-background](https://github.com/PRATAP-KUMAR/ubuntu-gdm-set-background)

### To get keys 
 
 Create/login to your account from the unsplash website.
 From the [applications page](https://unsplash.com/oauth/applications), create a new app.
 Navigate to keys section to get access key and secret key. Get the redirect uri from Redirect URI and permissions section.

 Allow all the permissions for the app (for the python-unsplash library to work, even though only public photos will be accessed.)


### To run the program, download the files and run as:
```python3 ubuntu-login-screen.py <access key> <secret key> <redirect_uri>```
 If the execution is successful, the program will be added to startup and keys will be cached locally.
 
 Note: Script has been tested only with ubuntu 21.10, but should work with 20.04, 21.04 and 21.10
 Enjoy!