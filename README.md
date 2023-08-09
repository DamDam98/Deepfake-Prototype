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


## Voice Gen




5. Install packages

First run `npm install yarn -g` to install yarn globally (if you haven't already).

Then run:

```
yarn install
```
After installation, you should now see a `node_modules` folder.

3. Set up your `.env` file

- Copy `.env.example` into `.env`
  Your `.env` file should look like this:

```
OPENAI_API_KEY=
```

- Visit [openai](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key) to retrieve API keys and insert into your `.env` file.

## Run the app

run the app `npm run dev` to launch the local dev environment, and then type a question in the chat interface.

Note: ensure you are on node 18+

## Deploying with Vercel

1. create a vercel account
2. connect your github account (ideally, give it access to all your repos)
3. click add new, then choose project
4. choose this repo
5. paste the .env from the repo into the environment variables section on the initial setup page
6. hit deploy and watch the magic happen
note: anytime you push a change to the main branch, this will kick off a new build and deploy live to the website

## Editing the Prompts

the prompts live in `utils/makechain.ts` you'll want to change the `baseCallPrompt` string to update the chatbot call.

**General errors**

- there is a known issue where after a few interactions with the chatbot it begins to over complete, meaning it will begin guessing the users responses and auto completing the remainder of the discussion for some reason
- on vercel, the chat api takes too long meaning it times out. To increase the timeout limit past 10 seconds you'll need to convert your account to paid and configure the vercel.json file as so.

```
{
  "functions": {
    "api/test.js": {
      "maxDuration": 60
    }
  }
}
```

## Credit

Frontend of this repo is inspired by [langchain-chat-nextjs](https://github.com/zahidkhawaja/langchain-chat-nextjs)
