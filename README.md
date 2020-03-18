### Add Course Bot for METU Students

Between interactive registration period of METU, Students face lots of difficulties due to **course capacity is full** 

Requirements:
- **Captcha Buster**

The extension should be installed before the execution of the program. 
https://github.com/dessant/buster


Inputs of the application:
- Metu User id
- Metu Password
- Course Code
- Number of Trials

The program will try **Number of Trials** times to take the course. 

- The program uses `pyautogui` package of python and search for images around the screen. In order program to work perfectly, users should update images according to their screen resolution.

- Users should change path of images according to their computer. 
