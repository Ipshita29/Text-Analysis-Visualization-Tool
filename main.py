from text_parser import parse_text
from analyzer import analyze_numbers
from visualizer import create_plot

print("Enter text:")

text = input()   # ✅ single Enter only

data = parse_text(text)

print("\n--- TEXT SUMMARY ---")
print("Sentence count:", data["sentence_count"])
print("Word count:", data["word_count"])
print("Average sentence length:", data["avg_sentence_length"], "words")
print("Tone:", data["tone"])
print("Contains numbers:", data["contains_numbers"])


if len(data["numbers"]) > 0:
    stats = analyze_numbers(data["numbers"])

    print("\n--- NUMBER SUMMARY ---")
    print("Count:", stats["count"])
    print("Mean:", stats["mean"])
    print("Min:", stats["min"])
    print("Max:", stats["max"])

    if data["wants_plot"]:
        create_plot(data["numbers"])   # ✅ no saving
else:
    print("\nNo numbers found.")
