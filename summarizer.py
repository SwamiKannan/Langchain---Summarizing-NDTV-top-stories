import pickle
from langchain.chains.summarize import load_summarize_chain
from langchain.llms import OpenAI
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
import os

def get_openai_api():
    if 'OPEN_API_KEY' in os.environ:
        pass
    else:
        key=input('Enter your key here')
        os.environ['OPEN_API_KEY']=key



def summarize():
    with open('data.pkl','rb') as f:
        news_dict=pickle.load(f)

    llm=OpenAI(model_name='text-davinci-003', temperature=0)
    summarizer=load_summarize_chain(llm,chain_type='map_reduce',verbose=True)

    summary_dict={}
    for k,v in news_dict.items():
        if 'No content' in v[2]:
            continue
        hl=v[0]
        docs=(v[1]+v[2]).replace("\xa0", " ")
        d=Document(page_content=docs)
        result=summarizer.run([d])
        url=v[3]
        summary_dict[k]=(hl,url,docs,result,len(docs),len(result))
    return summary_dict

def summarize_news():
    get_openai_api()
    summary_dict_final=summarize()
    with open('summary.pkl', 'wb') as f:
        pickle.dump(summary_dict_final, f, protocol=pickle.HIGHEST_PROTOCOL)
    return summary_dict_final
