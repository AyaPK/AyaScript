import ayascript

funcs = {

    "output": [
        "#verb.cap# #noun.a# my ass!\n\n(I will not #verb# #noun.a#.)",
        "I will never #verb# #noun.a#, and you can't make me!",
        "#verb.cap# #noun2.a#? In THIS economy!?",
        "I will not #verb# #noun2.a#. Ever."
    ],

    "verb": [
        "run"
    ],

    "noun": [
        "lawyer"
    ],

    "noun2": [
        "cat"
    ]
}

output = ayascript.ayascript(funcs)
print(output)
