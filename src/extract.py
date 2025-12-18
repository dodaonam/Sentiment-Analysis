from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from src.llm import model

class Classification(BaseModel):
    sentiment: str = Field(description="The sentiment of the text")
    political_tendency: str = Field(
        description="The political tendency of the user"
    )
    language: str = Field(description="The language the text is written in")

class SentimentAnalysis:
    def __init__(self):
        self.parser = PydanticOutputParser(pydantic_object=Classification)
        self.prompt = ChatPromptTemplate.from_template("""
Extract the following information from the text:
{format_instructions}

Text to analyze:
{text}
        
Provide ONLY valid JSON output matching the schema.
""")
        self.chain = (
            self.prompt.partial(format_instructions=self.parser.get_format_instructions())
            | model
            | self.parser
        )
    
    def extract(self, text: str):
        return self.chain.invoke({"text": text})