import os
from langchain import HuggingFaceHub

if __name__ == '__main__':
    os.environ['HUGGINGFACEHUB_API_TOKEN'] = \
        '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'
    
    llm = HuggingFaceHub(repo_id='google/flan-t5-large',
                         model_kwargs={'temperature':0,
                                       'max_length':64})
    llm("translate english to french: How old are you?")