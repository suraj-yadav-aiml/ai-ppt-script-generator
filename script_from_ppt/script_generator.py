from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from .prompts import PromptHandler
from .config import Config


class ScriptGenerator:
    """
    A class to handle LLM-based script generation from context.
    """

    def __init__(self):
        """
        Initialize the script generator.
        """
        self.llm = ChatOpenAI(model=Config.MODEL_NAME, temperature=Config.TEMPERATURE)
        self.qna_chain = self._initialize_chain()

    def _initialize_chain(self):
        """
        Initialize the LLM chain.

        Returns:
            Callable: A chain that processes prompts and generates responses.
        """
        prompt_template = PromptHandler.get_chat_prompt()
        return prompt_template | self.llm | StrOutputParser()

    def generate_script(self, context: str, question: str) -> str:
        """
        Generate a script based on the given context and question.

        Args:
            context (str): The context string.
            question (str): The question or instruction for script creation.

        Returns:
            str: The generated script.

        Raises:
            ValueError: If script generation fails.
        """
        try:
            return self.qna_chain.invoke({"context": context, "question": question})
        except Exception as e:
            raise ValueError(f"Script generation failed. Error: {str(e)}")
