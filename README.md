## Inventory
1. Deepfakes
  - Face swap (Roop - https://github.com/s0md3v/roopwa)
  - Lip Sync (Wav2Lip - https://github.com/Rudrabha/Wav2Lip)
  - Downscale (Ffmpeg)
  - Upscale (Real ESRGAN - https://github.com/xinntao/Real-ESRGAN)
2. Voice clone
  - Eleven labs (https://github.com/elevenlabs/elevenlabs-python)

## Pipeline
1. generate audio with vioce clone python script (eleven labs) - (30 secs)
2. downscale stock video to 240p in colab (ffmpeg) - (30 secs)
3. faceswap downscaled stock video with target image in colab (roop) - (2.5 mins)
4. lip sync audio from step 1 to faceswapped output from step 3 in colab (wav2lip) - (1 min)
5. upscale lip synced result from step 4 in colab (Real ESRGAN) - (**30 mins**)

## Deepfake Notebook Links

1. Faceswap (Roop - https://github.com/s0md3v/roopwa)
  - colab: https://colab.research.google.com/drive/16cHi8q2-ut_j_B5JA7pdcbKOEay8hIXL?usp=drive_link
    - inputs:
       - stock video
       - person of interest photo
     - output:
         - stock video with person of interest's face on it
   
2. Lip Sync (Wav2Lip - https://github.com/Rudrabha/Wav2Lip)
  - colab: https://colab.research.google.com/drive/1XivuTIbpnwoxX46l9fTCR0-TOzn083da?usp=sharing
    - inputs:
       - audio file
       - faceswapped video
    - output
       - face swapped video with new audio lip synced
   
3. Downscale (FFmpeg)
  - colab: https://colab.research.google.com/drive/1aO-mKSq6fdpEI8pgqnH4vMGP8ho0H9UY?usp=drive_link
    - inputs:
       - audio file
       - faceswapped video
    - output
       - face swapped video with new audio lip synced
4. Upscale (Real ESRGAN - https://github.com/xinntao/Real-ESRGAN)
  - colab: https://colab.research.google.com/drive/1DqJ8oEL0o698LuX51JWyDUcMM0oJJ0ch?usp=drive_link
    - inputs:
       - audio file
       - faceswapped video
    - output
       - face swapped video with new audio lip synced

## Deepfake Notebook Usage

1. create a directory in the colab filesystem called assets and upload input files to it
2. update command line arguments to fit the new input names
  - roop ex: ` !python run.py --execution-provider cuda -s /content/assets/<PERSON_OF_INTEREST_FILENAME> -t /content/assets/<STOCK_VIDEO_FILENAME> -o /content/assets/<OUTPUT_FILENAME> `
3. run all code cells
  - output:
    - for roop the output file will populate in the assets folder as expected
    - **IMPORTANT**: for wav2lip however, the result will not populate in the assets folder it will be in Wav2Lip/results


## Voice Clone Usage
1. open `voice_clone.py` script
2. run `pip install elevenlabs` to download the library
3. insert eleven labs api key (create one on elevenlabs.io if you need to)
4. browse available voices by uncommenting this line (create a new voice on eleven labs web client if you want)
     ```
     # for voice in voices():
     #     print(voice)
     ```
5. pick a voice from the list with this line (use the print to make sure it's the right voice)
     ```
     jacques = voices()[-1]
      # print(jacques)
     ```
6. run the script locally by calling `python voice_clone.py`
