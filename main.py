from ayascript import ayascript

funcs = {

    "output": {
        "#word1.cap# #word2#, Aya!",
        "It's #adjective.a# #noun#"
    },

    "word1": {
        "cool"
    },

    "word2": {
        "program"
    },

    "noun": {
        "cat","dog","fish","mouse"
    },

    "adjective": {
        "quiet","big","small","red","blue","awesome","angry","empty"
    }

}

output = ayascript(funcs)
print(output)
