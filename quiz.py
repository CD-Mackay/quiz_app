from string import ascii_lowercase

QUESTIONS = {
  "When was the first use of the word 'quiz'": ["1781", "1771", "1871", "1881"],
  "What method can we use to get user input?": ["input", "get", "print", "write"],
  "What keyword do you use to loop over a given list of elements": ["for", "while", "each", "loop"],
  "What is the purpose of the zip() function": ["To iterate over two or more sequences at the same time", 
  "To combine several strings into one", "To compress several files into one archive", "to get information from the user"]
}

for num, (question, alternatives) in enumerate(QUESTIONS.items(), start=1):
  print(f"\nQuestion {num}:")
  print(f"{question}?")
  correct = alternatives[0]
  labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
  for label, alternative in labeled_alternatives.items():
      print(f" {label}) {alternative}")

  answer_label = input("\nChoice?")
  answer = labeled_alternatives.get(answer_label)
  if answer == correct:
    print("Nailed it!")
  else:
    print(f"Apologies, the correct answer was {correct!r}, not {answer!r}")