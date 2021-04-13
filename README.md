# kindergraten-violence-detector
## data 
the data should be arrabged as follows:


![alt text](/dataset_fmt.jpg?raw=true)


## Training 

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
