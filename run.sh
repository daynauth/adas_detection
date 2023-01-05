docker run --gpus all -it --rm --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 \
-v $PWD:/adas \
-v /data1:/data1 \
-w /adas adas