
import wave
import math
import struct
ff=wave.open("两只老虎","w")
ff.setframerate(8000)
ff.setnchannels(1)
ff.setsampwidth(2)

import pyaudio
p=pyaudio.PyAudio()
river=p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=8000,
    output=True,)
    #frames_per_buffer=1024)



def wv(t=0,f=0,v=0.5,wf=ff,sr=8000):
    '''
    t:写入时长
    f:声音频率
    v：音量
    wf：一个可以写入的音频文件
    sr：采样率
    '''
    tt=0
    dt=1.0/sr
    while tt<=t:
        s=math.sin(tt*math.pi*2*f)*v*32768#采样，调节音量，映射到[-2^15,2^15)
        s=int(s)
        
        fd=struct.pack("h",s)#转换成8bit二进制数据
        try:
            wf.writeframes(fd)#写入音频文件
        except:
            wf.write(fd)
        tt+=dt#时间流逝

note={"1":262,"2":294,"3":330,"4":349,"5":392,"6":440,"7":494,"6-":220,"0":0}
n=[
    "1","2","3","1","1","2","3","1",
    "3","4","5","3","4","5",
    "5","6","5","4","3","1",
    "5","6","5","4","3",'2',"1",
    "2","6-","1","0","2","6-","1"
]
tm=[
    2,2,2,2,2,2,2,2,
    2,2,4,2,2,4,
    1,1,1,1,2,2,
    1,1,1,1,1,1,2,
    2,2,2,2,2,2,2
]

for i in range(len(n)):
    wv(tm[i]/4.0,note[n[i]],wf=river)




ff.close()
