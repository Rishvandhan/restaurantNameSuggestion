
from langchain_community.chat_models import ChatOpenAI 
import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from dotenv import load_dotenv
import os


load_dotenv()

os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


llm = ChatOpenAI(
    model="microsoft/mai-ds-r1:free",
    temperature=0.7
)

def generate_name_items(cuisine):
    prompt_template_name = PromptTemplate(
    input_variables = ['cuisine'],
    template= """Generate ONLY a fancy restaurant name for {cuisine} food. 
                Return JUST the name without quotes, explanations or punctuation.
                Example Output: Royal Spice"""
    )

    name_chain = LLMChain(
    llm=llm,
    prompt=prompt_template_name,
    output_key="restaurant_name"  # Explicit output key
    )

    prompt_template_items = PromptTemplate(
    input_variables=['restaurant_name'],
    template="suggest some menu items for {restaurant_name}."
    )

    food_item_chain = LLMChain(
    llm=llm,
    prompt=prompt_template_items,
    output_key="menu_items"
    )

    full_chain = SequentialChain(
    chains=[name_chain, food_item_chain],
    input_variables=["cuisine"],  # Only initial input
    output_variables=["restaurant_name", "menu_items"],  # All final outputs
    verbose=True
    )

    result = full_chain({"cuisine": cuisine})
    return result




if __name__ == "__main__":
    print(generate_name_items("Indian"))





