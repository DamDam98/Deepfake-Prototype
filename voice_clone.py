from elevenlabs import clone, generate, play, set_api_key, voices

set_api_key("<ELEVEN_LABS_API_KEY>")


# for voice in voices():
#     print(voice)

jacques = voices()[-1]

# print(jacques)


def save_as_mp3(bytes_obj, filename):
    with open(filename, 'wb') as f:
        f.write(bytes_obj)


audio = generate(
    text="""I LOVE Orlando, and it is THE BEST place to build a startup. When Sal Rehmetullah, Suneera Madhani and I were asked why we weren't relocating our startup Stax to the west coast, our answer was simple. Orlando has everything we need.

And we proved it!

We grew our little fledgling startup into Orlando's FIRST unicorn, and one of only 14 unicorns ever founded in Florida.

And now we're going to make Sensei-ly unicorn number two!

Hopefully, having two unicorns founded here, launched with local capital and executed by central Florida talent lays to rest any doubt about what is possible in The City Beautiful.

1) Orlando is ranked number 1 in places to found a new startup,
2) We produce the most talent with our concentration of strong colleges and universities,
3) We're the modeling and simulation capital of the world,
4) ..and yes, we take credit for having some wonderful theme parks and being a great place to raise a family.

Let's show the world that they're missing out if they're not part of this Orlando ecosystem!""", voice=jacques)

# play(audio)

save_as_mp3(audio, 'jacques_linkedin_audio.mp3')
