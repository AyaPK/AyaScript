from ayascript import ayascript

funcs = {

    "output": {
        "#word1.cap# #word2#, Aya!",
        "It's #adjective.a# #noun#"
    },

    "word1": {
        "cool","neat","weird"
    },

    "word2": {
        "program", "application", "cake"
    },

    "noun": {
        "cat","dog","fish","mouse","pet","house"
    },

    "adjective": {
        "quiet","big","small","red","blue","awesome","angry","empty"
    }

}

output = ayascript(funcs)
print(output)
