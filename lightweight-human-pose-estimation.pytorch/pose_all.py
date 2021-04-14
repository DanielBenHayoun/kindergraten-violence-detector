from demo import run_demo,ImageReader
from models.with_mobilenet import PoseEstimationWithMobileNet
from modules.keypoints import extract_keypoints, group_keypoints
from modules.load_state import load_state
from modules.pose import Pose, track_poses
from val import normalize, pad_width
import torch
import os
from pathlib import Path
import glob
print(glob.glob("/home/adam/*.txt"))

net = PoseEstimationWithMobileNet()
checkpoint = torch.load("./checkpoint_iter_370000.pth", map_location='cpu')
load_state(net, checkpoint)

fight_directory = r'/home/danielshay2021/t1/RWF-2000/train/Fight'
nonfight_directory = r'/home/danielshay2021/t1/RWF-2000/train/NonFight'
destination_fight_directory = r'/home/danielshay2021/pose_daniel/train/Fight'
destination_nonfight_directory = r'/home/danielshay2021/pose_daniel/train/NonFight'
source=[fight_directory,nonfight_directory]
destination=[destination_fight_directory,destination_nonfight_directory]


for source_dir,dest_dir in zip(source,destination):
	index = 0

	print("source is" + source_dir)
	print(os.listdir(source_dir))
	for dir in os.listdir(source_dir):
	    # vmeid_name = destination_fight_directory+'\\vid'+ str(index)  #windows version (\)
	    vid_dir =  str(index)  # linux version (/)
	    Path( destination_fight_directory + '/' + vid_dir,).mkdir(parents=True, exist_ok=True)
	    print("creating dir: " + vid_dir)
	    frame_index = 0
	    source_dir_current = source_dir + '/' + dir + '/*'
	    source_files=glob.glob(source_dir_current)
	    dest_dir_current = dest_dir + '/' + vid_dir
	    print("dest_dir_current " + dest_dir_current)
	    frame_provider = ImageReader(source_files)
	    print(frame_provider.file_names)
	    track = 0
	    smooth=1
	    cpu=True
	    height_size=256
	    run_demo(net, frame_provider,height_size,cpu, track, smooth,dest_dir_current)
	    index +=1


