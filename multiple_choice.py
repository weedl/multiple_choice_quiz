from question import questions

prompts = ("What is the worlds tallest mountain? \na: Mount everest\nb: K2\nc: Galdøpiggen",
 "Where is French Guinea located?\na: Africa\nb: South America\nc: Asia",
  "How old is Usain Bolt (As of June 2022)\na: 31\nb: 24\nc: 35")

question1 = questions(prompts[0], "a")
question2 = questions(prompts[1], "b")
question3 = questions(prompts[2], "c")

quiz = (question1, question2, question3)

score = 0

for q in quiz:
    print(q.prompt)
    answer = input()
    if answer.lower() == q.answer:
        score += 1
        print("Your answer is correct! (+1)")
    else:
        print("Sorry, your answer is not correct.")

print("You're score is a", str(score) + "/3")