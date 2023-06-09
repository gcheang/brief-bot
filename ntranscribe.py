"""
Module for audio transcription, helper module for app.py

Imported By
-----------
app.py              : main module for the BriefBot discord app

Imports
-------
SpeechRecognition   : Audio to text transcription

Functions:
----------
transcribe          : Returns a transcription of an audio file
"""

#!/usr/bin/env python3

import speech_recognition as sr

def transcribe(audio_file):
    """
    Returns a transcription of an audio file

    Parameters
    ----------
    audio_file : audio_file
        an audio file to be transcribed by speech recognition

    Returns
    -------
    str
        a transcription of the audio file
    """
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)

    return recognizer.recognize_sphinx(audio)
