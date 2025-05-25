import re
import json

def call_llm_api(input_text, temp=0, model='gpt-3.5-turbo'):

    pass # This function should be replaced with the actual LLM API call logic.

with open("textbook.json") as f:
    paragraphs = json.load(f)
with open("question.json") as f:
    questions = json.load(f)

    
def test_llm(id, model, locate=True):
    source_text = questions[id]['updated_paragraph']
    question_text = questions[id]['updated_question']['question']
    choice1 = questions[id]['updated_question']['updated']
    choice2 = questions[id]['updated_question']['random1']
    choice3 = questions[id]['updated_question']['random2']
    choice4 = questions[id]['updated_question']['random3']
    
    if locate:
        input_text = (
            f"Here's a paragraph with modified knowledge: {source_text} \n"
            f"Please answer the following question based on the modified knowledge source above, you may combine with your own knowledge only when the required knowledge does not exist in the original paragraph.\n"
            f"{question_text}\n"
            f"A. {choice1}\n"
            f"B. {choice2}\n"
            f"C. {choice3}\n"
            f"D. {choice4}\n"
            f"Please first identify the corresponding sentences that include the answer to the question, and print your selected answer's alphabet with in double brackets, e.g. [[A]]."
        )
    else:
        input_text = (
            f"Here's a paragraph with modified knowledge: {source_text} \n"
            f"Please answer the following question based on the modified knowledge source above, you may combine with your own knowledge only when the required knowledge does not exist in the original paragraph.\n"
            f"{question_text}\n"
            f"A. {choice1}\n"
            f"B. {choice2}\n"
            f"C. {choice3}\n"
            f"D. {choice4}\n"
            f"Please directly print your selected answer's alphabet within double brackets, e.g. [[C]]. You should not include any other information in your response."
        )
    
    while True:
        answer_raw = call_llm_api(input_text, temp=0, model=model)
        if answer_raw is not None:
            break
    
    matches = re.findall(r"\[\[([A-Za-z])", answer_raw)
    if len(matches) == 0:
        return id, 'F', None
    return id, matches[0], answer_raw