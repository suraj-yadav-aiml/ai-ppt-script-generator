from typing import Dict
from langchain_community.document_loaders import UnstructuredPowerPointLoader
from langchain.schema import Document


class PowerPointProcessor:
    """
    A class to handle PowerPoint content extraction and context generation.
    """

    def __init__(self, verbose: bool = False):
        """
        Initialize the processor.

        Args:
            verbose (bool): Whether to enable verbose logging.
        """
        self.verbose = verbose

    def extract_data(self, file_path: str, mode: str = "elements") -> Dict[int, str]:
        """
        Extracts content from a PowerPoint file.

        Args:
            file_path (str): Path to the PowerPoint file.
            mode (str): Mode for loading the PowerPoint file. Default is 'elements'.

        Returns:
            Dict[int, str]: A dictionary where keys are page numbers and values
                            are the concatenated content of each page.

        Raises:
            FileNotFoundError: If the file path is invalid.
            ValueError: If the loader fails to process the file.
        """
        if self.verbose:
            print(f"Loading file: {file_path}, mode: {mode}...")

        try:
            loader = UnstructuredPowerPointLoader(file_path=file_path, mode=mode)
            docs = loader.load()
            if self.verbose:
                print(f"Loaded {len(docs)} documents.")
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")
        except Exception as e:
            raise ValueError(f"Failed to load file. Error: {str(e)}")

        ppt_data = {}
        for idx, doc in enumerate(docs, start=1):
            if isinstance(doc, Document):
                page_number = doc.metadata.get("page_number")
                if page_number:
                    ppt_data[page_number] = ppt_data.get(page_number, "") + "\n" + doc.page_content
                if self.verbose:
                    print(f"Processed document {idx}/{len(docs)}: Page {page_number}")

        if not ppt_data:
            raise ValueError("No content extracted.")

        return ppt_data

    def build_context(self, ppt_data: Dict[int, str]) -> str:
        """
        Builds a formatted context string from PowerPoint data.

        Args:
            ppt_data (Dict[int, str]): A dictionary where keys are page numbers
                                       and values are the corresponding page content.

        Returns:
            str: A formatted context string with page information.

        Raises:
            ValueError: If `ppt_data` is empty or not a dictionary.
        """
        if not isinstance(ppt_data, dict) or not ppt_data:
            raise ValueError("Invalid `ppt_data`: must be a non-empty dictionary.")

        context = ""
        for page_number, page_content in sorted(ppt_data.items()):
            if isinstance(page_number, int) and isinstance(page_content, str):
                context += f"### Page-{page_number}\n{page_content.strip()}\n\n"
            else:
                if self.verbose:
                    print(f"Skipping invalid content for Page-{page_number}")

        if not context.strip():
            raise ValueError("No valid content for context.")

        return context
