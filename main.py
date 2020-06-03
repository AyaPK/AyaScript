import ayascript

nodes = {
    # the output key will be where you can create sentence structures to be created
    # surround a word with hashes to turn it in to a node
    "output": {
        "#word1.cap# #word2#, Aya!",
        "It's #adjective.a# #noun#"
    },

    # keys following the output node will contain values that are
    # randomly selected when generating the final sentence
    "word1": {
        "cool", "neat", "weird", "interesting"
    },

    "word2": {
        "program", "application", "cake", "code"
    },

    "noun": {
        "cat", "dog", "fish", "mouse", "pet", "house"
    },

    "adjective": {
        "quiet", "big", "small", "red", "blue", "awesome", "angry", "empty"
    }

}

# call the ayascript function and pass in your nodes dictionary to generate a sentence
output = ayascript.ayascript(nodes)
print(output)

# Built in Random Number Generation
print(ayascript.randomDigit(20, 50))
print(ayascript.randomChoice(["Choose", "From", "A", "List", "Of", "Items"]))

# Brainfuck transpiler made for fun
ayascript.brainfuck("++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.")