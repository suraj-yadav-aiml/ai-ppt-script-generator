from powerpoint_processor import PowerPointProcessor
from script_generator import ScriptGenerator
from config import Config


def main(file_path: str):
    try:
        processor = PowerPointProcessor(verbose=Config.VERBOSE)
        ppt_data = processor.extract_data(file_path=file_path)
        context = processor.build_context(ppt_data)

        question = (
            "For each PowerPoint slide provided above, write a 3-4 minute script "
            "that effectively conveys the key points. Ensure a smooth flow between slides, "
            "maintaining a clear and engaging narrative."
        )
        script_generator = ScriptGenerator()
        response = script_generator.generate_script(context=context, question=question)

        print("\n--- Generated Script ---\n")
        print(response)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    FILE_PATH = "../data/ml_course.pptx"  
    main(file_path=FILE_PATH)
