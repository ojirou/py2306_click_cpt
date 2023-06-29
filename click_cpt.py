import pyautogui as pgui
import os
def main():
    print('キャプチャ画像を保存するフォルダ')
    FolderName = input('>> ')
    FolderPath='C:\\Users\\user\\python\\GUI\\capture_output\\'+FolderName
    os.mkdir(FolderPath)
    i=0
    while True:
        print('Click at the Upper Left')
        dummy = input('>> ')
        PosUpperLeft=pgui.position()
        print('Click at the Lower Right')
        dummy = input('>> ')
        PosLowerRight=pgui.position()
        x1=PosUpperLeft[0]
        y1=PosUpperLeft[1]
        dx=PosLowerRight[0]-PosUpperLeft[0]
        dy=PosLowerRight[1]-PosUpperLeft[1]
        print(x1, y1, dx, dy)
        # type(x1)
        for num in range(1, 2000):
            i=i+1
            num=int(num)
            s=f'{i:03}'
            filename=FolderPath+'\\'+FolderName+'_'+str(s)+'.png' 
            print('Click for Capture (q:quit, c:change frame)')
            pgui.screenshot(filename, region=(x1, y1, dx, dy))
            dummy = input('>> ')
            if dummy == 'c' or dummy == 'q':
                break
        if dummy == 'q':
            break
#         time.sleep(1)
if __name__ == "__main__":
    main()