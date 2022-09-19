QUESTIONS = {
  "When was the first use of the word 'quiz'": ["1781", "1771", "1871", "1881"],
  "What method can we use to get user input?": ["input", "get", "print", "write"],
  "What keyword do you use to loop over a given list of elements": ["for", "while", "each", "loop"],
  "What is the purpose of the zip() function": ["To iterate over two or more sequences at the same time", 
  "To combine several strings into one", "To compress several files into one archive", "to get information from the user"]
}

for question, alternatives in QUESTIONS.items():
  correct = alternatives[0]
  for alternative in sorted(alternatives):
      print(f" -{alternative}")

  answer = input(f"{question}?")
  if answer == correct:
    print("Nailed it!")
  else:
    print(f"Apologies, the correct answer was {correct}, not {answer}")