import os
import openai
import random

openai.api_key = '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'


def generate_description(name, gender, desc_type, age, profession, date_type):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Write an 2 line short {desc_type[2]} for {name}, {age} years {gender}\nwho study {profession} in tel aviv university, looking for {date_type} relationship",
        temperature=0.1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(f"description:{response['choices'][0]['text']}")


def generate_questions():
    # hobby1 = input("Enter first hobby: ")
    # hobby2 = input("Enter second hobby: ")
    # hobby3 = input("Enter third hobby: ")
    desc_type = ['joke', 'description','poem','wordle']
    name = 'moshe'
    gender = 'man'
    age = 24
    profession = 'Economics Student'
    date_type = 'long term'
    generate_description(name, gender, desc_type, age, profession, date_type)
    hobby1 = 'eat fish'
    hobby2 = 'listen to music'
    hobby3 = 'see the sunset'
    hobby_lst = [hobby1, hobby2, hobby3]
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Create a list of 3 questions for my conversation with a date"
               f" loving to '{hobby1}' and f'{hobby2}' and f'{hobby3}'",
        temperature=0.5,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    questions_response_lst = response['choices'][0]['text'].split('\n')
    questions_response_lst = [item.lstrip() for item in questions_response_lst
                              if item]
    return hobby_lst, questions_response_lst


def generate_emoji(hob_lst):
    emoj_lst = []
    for i in range(len(hob_lst)):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Convert movie titles into emoji.\n\n{hob_lst[i]}:",
            temperature=0.8,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\n"]
        )
        emoj_lst.append(response['choices'][0]['text'])
    return emoj_lst


def get_mood_response(hob_lst, i):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"The CSS code for a color like {hob_lst[i]}:\n\n",
        temperature=0,
        max_tokens=64,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=[";"]
    )
    return response


def get_mood_color(hob_lst):
    responses = []
    nums = random.sample(range(3), 2)
    for i in range(2):
        response = get_mood_response(hob_lst, nums[i])
        responses.append(response['choices'][0]['text'].split("color: ", 1)[1])
    return responses[0], responses[1]


def gradient_generator(hob_lst):
    from colour import Color
    red = Color("red")
    colors = list(red.range_to(Color("green"), 10))
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import numpy as np

    def colorFader(c1, c2,
                   mix=6):  # fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)
        c1 = np.array(mpl.colors.to_rgb(c1))
        c2 = np.array(mpl.colors.to_rgb(c2))
        return mpl.colors.to_hex((1 - mix) * c1 + mix * c2)

    c1, c2 = get_mood_color(hob_lst)
    n = 500

    fig, ax = plt.subplots(figsize=(8, 5))
    for x in range(n + 1):
        ax.axvline(x, color=colorFader(c1, c2, x / n), linewidth=4)
    plt.show()


if __name__ == '__main__':
    print('\U0001FAD0 \U0001FAD0 \U0001FAD0 \U0001FAD0 \U0001FAD0'
          '\U0001FAD0 \U0001FAD0 \U0001FAD0 \U0001FAD0 \U0001FAD0'
          '\U0001FAD0 \U0001FAD0 \U0001FAD0 \U0001FAD0 \U0001FAD0'
          '\U0001FAD0 \U0001FAD0 \U0001FAD0 \U0001FAD0 \U0001FAD0'
          '\U0001FAD0 \U0001FAD0 \U0001FAD0 \U0001FAD0')
    print(
        '\U0001FAD0 Hi! Welcome to Berry, your personal dating experience \U0001FAD0')
    print('\U0001FAD0 \U0001FAD0 \U0001FAD0 \U0001FAD0 \U0001FAD0'
          '\U0001FAD0 \U0001FAD0 \U0001FAD0 \U0001FAD0 \U0001FAD0'
          '\U0001FAD0 \U0001FAD0 \U0001FAD0 \U0001FAD0 \U0001FAD0'
          '\U0001FAD0 \U0001FAD0 \U0001FAD0 \U0001FAD0 \U0001FAD0'
          '\U0001FAD0 \U0001FAD0 \U0001FAD0 \U0001FAD0')
    print(u'\U0001FAD0')
    hob_lst, questions_lst = generate_questions()
    emoj_lst = generate_emoji(hob_lst)
    for i in range(len(emoj_lst)):
        print(questions_lst[i] + emoj_lst[i])
    gradient_generator(hob_lst)
