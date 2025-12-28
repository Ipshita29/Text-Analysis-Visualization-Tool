def detect_tone(text):
    if text.count("!") >= 2:
        return "Excited"

    for word in text.split():
        if word.isupper() and len(word) > 2:
            return "Excited"

    return "Neutral"


def parse_text(text):
    original_text = text
    text = text.lower().strip()

    sentences = text.split(".")
    clean_sentences = []
    for s in sentences:
        if s.strip() != "":
            clean_sentences.append(s.strip())

    sentence_count = len(clean_sentences)

    words = text.split()
    word_count = len(words)


    if sentence_count > 0:
        avg_sentence_length = round(word_count / sentence_count, 1)
    else:
        avg_sentence_length = 0

    numbers = []
    for word in words:
        w = word.replace(",", "")
        if w.replace(".", "", 1).isdigit():
            numbers.append(float(w))

    return {
        "sentence_count": sentence_count,
        "word_count": word_count,
        "avg_sentence_length": avg_sentence_length,
        "tone": detect_tone(original_text),
        "contains_numbers": "Yes" if len(numbers) > 0 else "No"
    }
