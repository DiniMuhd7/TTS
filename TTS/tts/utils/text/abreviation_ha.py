import re

# List of (regular expression, replacement) pairs for abbreviations in hausa:
abbreviations_ha = [
    (re.compile("\\b%s\\." % x[0], re.IGNORECASE), x[1])
    for x in [
        ("wlh", "wallahi"),
        ("isa", "inshaallah"),
        ("slm", "salam"),
        ("aslm", "assalamu alaikum"),
        ("aslm", "assalam alaikum"),
        ("wslm", "wa'alaikumu salam"),
        ("w/slm", "wa'alaikumu salam"),
        ("saw", "salallahu alaihi wasalam"),
        ("as", "alaihi salam"),
        ("sw", "subhanahu wata’allah"),
        ("ra", "radiyallahu anhu"),
        ("ra", "radiyallahu anha"),
        ("alhmd", "alhamdulillah"),
        ("ykk", "yakake"),
        ("ykk", "yakike"),
        ("ngd", "nagode"),
        ("gsky", "gaskiya"),
        ("lfy", "lafiya"),
        ("lpy", "lafiya"),
        ("gdy", "godiya"),
        ("hkr", "hakuri"),
        ("mgd", "mungode"),
    ]
]
