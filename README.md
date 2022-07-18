To simply run the gui, you must

```bash
pip install PyQt5
pip install PyAudio
```

with py38 first

then run

```bash
python voiceprint_recognition.py
```

---

更详细一些

经测试，系统可以在Windows和Linux（如Ubuntu）下运行。

- 首先确保系统中安装了anaconda

- 切换到项目文件夹下，在命令行中运行

  ```bash
  conda env create -f env_list/conda_list.yml
  ```

  则会在系统中`$HOME/anaconda3/envs/voice`中安装所需环境
  如需更改安装路径，可修改`conda_env.yml`中的`prefix`参数

- 即可运行

  ```bash
  conda activate voice
  python 'Voiceprint recognition.py'
  ```