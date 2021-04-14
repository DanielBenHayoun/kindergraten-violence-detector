# kindergraten-violence-detector

## Requirements
library       | version
------------- | -------------
python        | 3.6
pytorch       | 1.8.1
tensorflow    | 1.14
ubuntu        | 18.04


## data 
the data should be arranged as follows:
![alt text](/dataset_fmt.jpg?raw=true)



## preprocess 
to achive arrange the data you can use the script preprocess.py:
```
python3 preprocess.py --data <dataset folder>
```
replace `<dataset folder>` with the main directory of the dataset which need to have the following structure:
![image](https://user-images.githubusercontent.com/33031852/114670328-8d8d9780-9d0b-11eb-9d90-316aafc89f08.png)




## pose estimation .
in order to run a training or detection , make sure to run pose estimation on the dataset. you can chose light-pose or you can chose pose-tensorflow make sure to edit the right paths in the script.

[pose-tensorflow](https://github.com/eldar/pose-tensorflow)

[lightweight-pose](https://github.com/Daniil-Osokin/lightweight-human-pose-estimation.pytorch)
 ```
cd pose-tensorflow/
python3 ProcessImgScript.py
```
OR
```
cd lightweight-human-pose-estimation.pytorch/
python3 pose_all.py
```

## Training 
for training run:
```
python main-run-vr.py --numEpochs 100 \
--lr 1e-4 \
--stepSize 25 \
--decayRate 0.5 \
--seqLen 20 \
--trainBatchSize 16 \
--memSize 256 \
--evalInterval 5 \
--evalMode horFlip \
--numWorkers 4 \
--outDir violence \
--fightsDirTrain fightSamplesTrainDir \
--noFightsDirTrain noFightSamplesTrainDir \
--fightsDirTest fightSamplesTestDir \
--noFightsDirTest noFightSamplesTestDir
```
replace fightSamplesTrainDir noFightSamplesTrainDir fightSamplesTestDir noFightSamplesTestDir with the right paths for your data.
