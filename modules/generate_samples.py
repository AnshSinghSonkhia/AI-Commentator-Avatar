from TTS.api import TTS

# List of speakers
speakers = [
    "p225", "p226", "p227", "p228", "p229", "p230", "p231", "p232", "p233", "p234", "p236", "p237", "p238", "p239", "p240", "p241", "p243", "p244", "p245", "p246", "p247", "p248", "p249", "p250", "p251", "p252", "p253", "p254", "p255", "p256", "p257", "p258", "p259", "p260", "p261", "p262", "p263", "p264", "p265", "p266", "p267", "p268", "p269", "p270", "p271", "p272", "p273", "p274", "p275", "p276", "p277", "p278", "p279", "p280", "p281", "p282", "p283", "p284", "p285", "p286", "p287", "p288", "p292", "p293", "p294", "p295", "p297", "p298", "p299", "p300", "p301", "p302", "p303", "p304", "p305", "p306", "p307", "p308", "p310", "p311", "p312", "p313", "p314", "p316", "p317", "p318", "p323", "p326", "p329", "p330", "p333", "p334", "p335", "p336", "p339", "p340", "p341", "p343", "p345", "p347", "p351", "p360", "p361", "p362", "p363", "p364", "p374", "p376"
]

speakers_selected = [
    "p228",
    "p229",
    "p230",
    "p234",
    "p240",
    "p241",
    "p251",
    "p256",
    "p257",
    "p264",
    "p267",
    "p302",
    "p312",
    "p340",
    "p363",
    "p335",
    "p333",
    "p284",
    "p274",
    "p273",
    "p270",
    "p268",
    "p260",
    "p259",
    "p246",
    "p248",
    "p250",
    "p237",
    "p243",
    "p245",
    "p308",
    "p310",
    "p329",
]

text = ("Hello I'm your personal assistant from India."
        "Aap se mil kar bahut maza aaya.")

# Load the TTS model
tts = TTS(model_name="tts_models/en/vctk/vits")

for speaker in speakers_selected:
    output_path = f"output/sample_{speaker}.mp3"
    tts.tts_to_file(text=text, speaker=speaker, file_path=output_path)
    print(f"Generated: {output_path}")