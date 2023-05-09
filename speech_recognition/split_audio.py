from pydub import AudioSegment
from pydub.silence import split_on_silence


def split_audio():
    sound = AudioSegment.from_mp3("./records/authenticate_audio.wav")
    loudness = sound.dBFS

    chunks = split_on_silence(sound,
                              min_silence_len=200,
                              silence_thresh=-45,
                              keep_silence=400
                              )

    # 遍历所有chunk，导出为单独的文件
    for i, chunk in enumerate(chunks):
        chunk.export(f"./records/authenticate_audio_{i}.wav", format="wav")

    print('总分段：', len(chunks))
