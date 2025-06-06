def sentence_to_word_lengths(sentence):
    words = sentence.split()
    result = [f"{word} {len(word)}" for word in words]
    return result

print(sentence_to_word_lengths("hello how are you"))

