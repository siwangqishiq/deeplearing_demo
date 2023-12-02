import whisper
import time

def CurrentTime():
    return int(round(time.time() * 1000))

if __name__ == "__main__" :
    print("run whisper ver:",whisper.__version__)
    
    t1 = CurrentTime()
    model = whisper.load_model("large")
    t2 = CurrentTime()
    print("load model ms time = " , t2 - t1)

    result = model.transcribe("test.mp3")
    print(result["text"])
    t3 = CurrentTime()
    print("speech recog cost ms time:" , t3 - t2)


