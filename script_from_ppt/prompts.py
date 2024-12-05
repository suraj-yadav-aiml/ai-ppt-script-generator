from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)


class PromptHandler:
    """
    A class to manage prompt templates for the LLM interaction.
    """

    @staticmethod
    def get_system_prompt() -> SystemMessagePromptTemplate:
        """
        Returns the system message prompt template.

        Returns:
            SystemMessagePromptTemplate: The system prompt template.
        """
        return SystemMessagePromptTemplate.from_template(
            "You are a highly skilled assistant. Your task is to create a script "
            "based on the context extracted from a PowerPoint presentation. "
            "Ensure clarity, engagement, and continuity in the script."
        )

    @staticmethod
    def get_human_prompt() -> HumanMessagePromptTemplate:
        """
        Returns the human message prompt template.

        Returns:
            HumanMessagePromptTemplate: The human prompt template.
        """
        return HumanMessagePromptTemplate.from_template(
            "Based on the context provided below, write a detailed, engaging script for each slide. "
            "Ensure the narrative flows smoothly and connects the key points.\n\n"
            "### Context:\n```{context}```\n\n### Question:\n```{question}```\n\n### Script:"
        )

    @staticmethod
    def get_chat_prompt() -> ChatPromptTemplate:
        """
        Combines the system and human prompts into a chat prompt template.

        Returns:
            ChatPromptTemplate: The combined chat prompt template.
        """
        system_prompt = PromptHandler.get_system_prompt()
        human_prompt = PromptHandler.get_human_prompt()
        return ChatPromptTemplate.from_messages(messages=[system_prompt, human_prompt])
