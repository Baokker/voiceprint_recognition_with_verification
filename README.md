# 安装环境

```bash
conda create -f env_list/environment-new.yml
```

可能能跑起来

# 运行

```bash
conda activate lipreading
python voiceprint_recognition.py
```

可能可以运行

# 系统干了什么

详见`main/authenticate.py`

- 按下s开始录制视频和音频
- 录制5秒的音频
- 录制80帧的嘴唇序列（中间有间隔）
- 判断嘴唇是否移动
- 将5秒的音频分割成四个数字的音频（很容易翻车）
- 进行语音识别
- 对5秒的音频进行声纹识别
- 综合嘴唇、声纹、语音识别，得出结果