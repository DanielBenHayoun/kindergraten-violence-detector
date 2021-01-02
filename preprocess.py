# Importing all necessary libraries
import cv2
import os
import shutil


class preprocessDataset():
    def __init__(self, train_path, val_path, DEBUG=True):
        self.val_path = val_path
        self.train_path = train_path
        if not DEBUG:
            self.relative = 1
        else:
            self.relative = 0.1

    def create_folders(self):
        source_path = ''
        for f1 in [self.train_path, self.val_path]:
            for f2 in ['Fight', 'NonFight']:
                path1 = os.path.join(source_path, f1, f2)
                list_dirs = os.listdir(path1)
                final_list = list_dirs[
                             :int(round(self.relative * len(list_dirs)))]
                for video in final_list:
                    os.mkdir(path1 + "\\" + video[:-4])

    def create_images_from_video(self, full_video_path):
        cam = cv2.VideoCapture(full_video_path)
        # frame
        currentframe = 0
        while (True):
            # reading from frame
            ret, frame = cam.read()
            if ret:
                # if video is still left continue creating images
                name = f'{full_video_path[:-4]}\\frame' + str(
                    int(round(currentframe))).zfill(3) + '.jpg'
                print('Creating...' + name)
                # writing the extracted images
                cv2.imwrite(name, frame)
                # increasing counter so that it will
                # show how many frames are created
                currentframe += 1
            else:
                break
        # Release all space and windows once done
        cam.release()
        cv2.destroyAllWindows()

    def create_all_images(self):
        for f1 in [self.train_path, self.val_path]:
            for f2 in ['Fight', 'NonFight']:
                path1 = os.path.join(f1, f2)
                list_dirs = os.listdir(path1)
                final_list = list_dirs[
                             :int(round(self.relative * len(list_dirs)))]
                for video_name in final_list:
                    if video_name.endswith(".avi"):
                        self.create_images_from_video(
                            os.path.join(f1, f2, video_name))

    def clean_folders(self):
        for f1 in [self.train_path, self.val_path]:
            for f2 in ['Fight', 'NonFight']:
                path1 = os.path.join(f1, f2)
                list_dirs = os.listdir(path1)
                for video_name in list_dirs:
                    if os.path.isdir(os.path.join(path1, video_name)):
                        shutil.rmtree(os.path.join(path1, video_name))

    def preprocess(self):
        self.clean_folders()
        self.create_folders()
        self.create_all_images()

p = preprocessDataset(
    "C:\\Users\\Danielbh\\Desktop\\5th\proj\RWF-2000\\val",
    "C:\\Users\\Danielbh\\Desktop\\5th\proj\RWF-2000\\train")

# p.clean_folders()
# p.create_folders()
#
# # p.create_images_from_video(
# #     "C:\\Users\\Danielbh\\Desktop\\5th\proj\RWF-2000\\val\\NonFight\\Fwhi4UNI_0.avi")
#
# p.create_all_images()

