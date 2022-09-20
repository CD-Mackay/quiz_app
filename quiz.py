import random
from string import ascii_lowercase
NUM_PER_QUIZ = 3
QUESTIONS = {
  "When was the first use of the word 'quiz'": ["1781", "1771", "1871", "1881"],
  "What method can we use to get user input?": ["input", "get", "print", "write"],
  "What keyword do you use to loop over a given list of elements": ["for", "while", "each", "loop"],
  "What is the purpose of the zip() function": ["To iterate over two or more sequences at the same time", 
  "To combine several strings into one", "To compress several files into one archive", "to get information from the user"]
}

##

def run_quiz():
  #Preprocess
  questions = prepare_questions()

  # Process (Main Loop)
  num_correct = 0
  for question in questions:
    num_correct += ask_question(question)

  # Postprocess
  print(f"\nYou got {num_correct} correct!")

## -------
def prepare_questions():
  num_questions = min(NUM_PER_QUIZ, len(QUESTIONS))
  questions = random.sample(list(QUESTIONS.items()), k=num_questions)
  return questions

## ------

def get_answer(question, alternatives):
  print(f"{question}?")
  labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
  for label, alternative in labeled_alternatives.items():
    print(f" {label}) {alternative}")

  while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
    print(f"Please answer one of {', '.join(labeled_alternatives)}")
  return labeled_alternatives[answer_label]

## ------

def ask_question(question, alternatives):
  correct_answer = alternatives[0]
  ordered_alternatives = random.sample(alternatives, k=len(alternatives))
   
  answer = labeled_alternatives.get(answer_label)
  if answer == correct:
    print("Nailed it!")
    num_correct += 1
  else:
    print(f"Apologies, the correct answer was {correct!r}, not {answer!r}")



##
# for num, (question, alternatives) in enumerate(questions, start=1):
#   print(f"\nQuestion {num}:")
#   print(f"{question}?")
#   correct = alternatives[0]
#   labeled_alternatives = dict(zip(ascii_lowercase, random.sample(alternatives, k=len(alternatives))))
#   for label, alternative in labeled_alternatives.items():
#       print(f" {label}) {alternative}")

#   while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
#     print(f"Please answer one of {', '.join(labeled_alternatives)}")
#   answer = labeled_alternatives.get(answer_label)
#   if answer == correct:
#     print("Nailed it!")
#     num_correct += 1
#   else:
#     print(f"Apologies, the correct answer was {correct!r}, not {answer!r}")
print(f"\nYou got {num_correct} correct out of a total of {num}")