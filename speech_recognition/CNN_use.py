# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:21:11 2022

@author: Bestom
"""

from speech_recognition.split_audio import split_audio


def predict_4_digit_audio():
    from CNN_model import load_model, predict

    cnn = load_model('./speech_recognition/cnn_best.pkl')

    split_audio()

    result = []

    for i in range(4):
        file = "./records/authenticate_audio_" + str(i) + ".wav"
        result.extend(predict(cnn, file))

    return result
