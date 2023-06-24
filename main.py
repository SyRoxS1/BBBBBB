from MainRisker import FileToImages
from FramesToVideoNormal import ImagesToVideo
from MainBigSafe import FileToImagesBig
from FramesToVideoSafe import ImagesBigToVideo
from VideoDownloader import DLFromYt
from VideoToFileNormal import VideoToFileNormal
from VideoToFileBig import VideoToFileBig
from GetYtVideosName import get_channel_videos
from UploadeToYt import upload
from VideoDownloader import DLFromYt
import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Yep')
    parser.add_argument('UploadOrExtract', metavar='UE', type=str, nargs='+',
                    help='Wich function to use')
    parser.add_argument('-u', '--upload')
    parser.add_argument('-e', '--extract')
    parser.add_argument('-c', '--compression')
    parser.add_argument('-f', '--filename')
    parser.add_argument('-v', '--videotodl')
    args = parser.parse_args()
    print(args)
    print(args.upload)
    if args.upload != None:
        PremierChoix = 3
        ChoixCloud = 1
        ChoixCompr = args.compression
    if args.extract != None:
        PremierChoix = 3
        ChoixCloud = 2
        

    channel_url = 'https://www.youtube.com/channel/UCyj7svz9hL15ciYwrV_wpLg'
    
    urls = get_channel_videos(channel_url)
    if ChoixCloud == 1:
        if ChoixCompr == 1:
            fichiervoulue = args.filename
            FileToImages(fichiervoulue)
            
            video_name = fichiervoulue + '.mp4'
            ImagesToVideo(video_name)
            upload(video_name,video_name[:-4],'Compr1','22','','public')
            
        if ChoixCompr == 2:
            fichiervoulue = args.filename
            FileToImagesBig(fichiervoulue)

            video_name = fichiervoulue + '.mp4'
            ImagesBigToVideo(video_name)
            upload(video_name,video_name[:-4],'Compr2','22','','public')
        for filename in os.listdir('./'):
            if filename.endswith('.mp4'):
                file_path = os.path.join('./', filename)
                os.remove(file_path)
                print(f"Deleted: {file_path}",end='\r')
    if ChoixCloud == 2:
        for i in range(len(urls)):
            print(i+1,urls[str(i+1)][1]+'\n')
        ChoixVid = args.videotodl
        urlDL = urls[ChoixVid][0]
        print(urlDL)
        DLFromYt(urlDL)
        if urls[ChoixVid][3] == "Compr1":
            nomVid = urls[ChoixVid][1].replace(".","") + ".mp4"
            print(nomVid)
            Vid = os.path.join('./videos',nomVid)
            VideoToFileNormal(Vid,urls[ChoixVid][1])
            
            os.remove(Vid)
            print(f"Deleted: {file_path}",end='\r')
        elif urls[ChoixVid][3] == "Compr2":
            nomVid = urls[ChoixVid][1].replace(".","") + ".mp4"
            Vid = os.path.join('./videos',nomVid)
            VideoToFileBig(Vid,urls[ChoixVid][1])
            os.remove(Vid)
            print(f"Deleted: {file_path}",end='\r')
        else:
            print("Description invalide")
    if ChoixCloud == 3:
        for i in range(len(urls)):
            print(i+1,urls[str(i+1)][1]+'\n')
        