## Inventory
1. Deepfakes
  - Face swap (Roop - https://github.com/s0md3v/roopwa)
  - Lip Sync (Wav2Lip - https://github.com/Rudrabha/Wav2Lip)
2. Voice clone
  - Eleven labs (https://github.com/elevenlabs/elevenlabs-python)

## Deepfake Notebook Links

1. Faceswap (Roop - https://github.com/s0md3v/roopwa)
    - inputs:
       - stock video
       - person of interest photo
     - output:
         - stock video with person of interest's face on it
   - https://colab.research.google.com/drive/16cHi8q2-ut_j_B5JA7pdcbKOEay8hIXL?usp=drive_link
2. Lip Sync (Wav2Lip - https://github.com/Rudrabha/Wav2Lip)
   - inputs:
       - audio file
       - faceswapped video
   - output
     - face swapped video with new audio lip synced
   - https://colab.research.google.com/drive/1XivuTIbpnwoxX46l9fTCR0-TOzn083da?usp=sharing

## Deepfake Notebook Usage

1. create a directory called assets and upload the source and target input files to it
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

## Next Steps
- try down up ai resolution enhancement to make clarity better and model run more efficiently
- search for good up down models and run in colab as well
