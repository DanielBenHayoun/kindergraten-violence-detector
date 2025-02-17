# Importing all necessary libraries
import cv2
import os
import shutil
import argparse


class preprocessDataset():
	def __init__(self, train_path, val_path, delete_After=True,DEBUG=True):
		self.val_path = val_path
		self.train_path = train_path
		self.delete_after=delete_After
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
					os.mkdir(path1 + "/" + video[:-4])

	def create_images_from_video(self, full_video_path):
		print("extracting frames from "+ full_video_path)
		cam = cv2.VideoCapture(full_video_path)
		# frame
		currentframe = 0
		i=0
		while (True):
			# reading from frame

			ret, frame = cam.read()

			if ret:
				# taking only 75% if frames
				if i % 4 == 1:
					print("skipping frame " + str(i))
					i += 1
					continue
				# if video is still left continue creating images
				# name = f'{full_video_path[:-4]}/frame' + str(
				#     int(round(currentframe))).zfill(3) + '.jpg'
				name = os.path.join(full_video_path[:-4],'frame'+str(
					int(round(currentframe))).zfill(3) + '.jpg')
				print('Creating...' + name)
				# writing the extracted images
				cv2.imwrite(name, frame)
				# increasing counter so that it will
				# show how many frames are created
				currentframe += 1
				i+=1

			else:
				break
		# Release all space and windows once done
		cam.release()
		cv2.destroyAllWindows()
		if currentframe!= 0 and self.delete_after:
		  print("removing video " + full_video_path )
		  os.remove(full_video_path)

	def create_all_images(self):
		print("starting creating frames")
		print(self.train_path)
		print(self.val_path)
		for f1 in [self.train_path, self.val_path]:
			print("f1 is " + f1)
			for f2 in ['Fight', 'NonFight']:
				print("f2 is " + f2)
				path1 = os.path.join(f1, f2)
				list_dirs = os.listdir(path1)
				final_list = list_dirs[:int(round(self.relative * len(list_dirs)))]
				print("final list is")
				print(final_list)
				for video_name in final_list:
					if video_name.endswith(".avi") or video_name.endswith(".mp4") :
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
		print("cleaning data")
		self.clean_folders()
		print("creating folders")
		self.create_folders()
		print("creating frames")
		self.create_all_images()

# print("DSF")
# p = preprocessDataset(
#     "C:\\Users\\Danielbh\\Desktop\\5th\proj\RWF-2000\\val",
#     "C:\\Users\\Danielbh\\Desktop\\5th\proj\RWF-2000\\train")

# p.clean_folders()
# p.create_folders()
#
# p.create_images_from_video(
#     "C:\\Users\\Danielbh\\Desktop\\5th\proj\RWF-2000\\train\\Fight\\_2RYnSFPD_U_0.avi")
# # #
# p.create_all_images()

if __name__ == '__main__':	
	parser = argparse.ArgumentParser()
	parser.add_argument('--data', type=str, default="RWF-2000", help='folder that containes train,val folders divided into Fight/NonFight')
	args = parser.parse_args()

	data = args.data
	print(os.path.join(data,"val"))
	print(os.path.join(data,"train"))
	
	p = preprocessDataset(os.path.join(data,"val"),os.path.join(data,"train"),DEBUG=False)
	p.preprocess()

