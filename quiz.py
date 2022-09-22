import random
from string import ascii_lowercase
import pathlib
try:
  import tomllib
except ModuleNotFoundError:
  import tomli as tomllib

NUM_PER_QUIZ = 3
QUESTIONS_PATH = pathlib.Path(__file__).parent / "questions.toml"
QUESTIONS = tomllib.loads(QUESTIONS_PATH.read_text())
# QUESTIONS = {
#   "When was the first use of the word 'quiz'": ["1781", "1771", "1871", "1881"],
#   "What method can we use to get user input?": ["input", "get", "print", "write"],
#   "What keyword do you use to loop over a given list of elements": ["for", "while", "each", "loop"],
#   "What is the purpose of the zip() function": ["To iterate over two or more sequences at the same time", 
#   "To combine several strings into one", "To compress several files into one archive", "to get information from the user"]
# }

def run_quiz():
  #Preprocess
  questions = prepare_questions(QUESTIONS, num_questions=NUM_PER_QUIZ)

  # Process (Main Loop)
  num_correct = 0
  for num, (question, alternatives) in enumerate(questions, start=1):
    print(f"\nQuestions {num}:")
    num_correct += ask_question(question, alternatives)

  # Postprocess
  print(f"\nYou got {num_correct} correct out of {num}")

## -------
def prepare_questions(questions, num_questions):
  num_questions = min(num_questions, len(questions))
  questions = random.sample(list(questions.items()), k=num_questions)
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

  answer =  get_answer(question, ordered_alternatives)
  if answer == correct_answer:
    print("Nailed it!")
    return 1
  else:
    print(f"The answer is {correct_answer!r} not {answer!r}")
    return 0

## -----
if __name__ == "__main__":
    run_quiz()