
# AI-Powered PowerPoint Script Generator

This project provides a **Streamlit web application** that utilizes **OpenAI's GPT models** to generate engaging scripts from PowerPoint slide content. Simply upload a `.pptx` file, configure AI settings, and let the app create a structured and captivating narrative for your presentation slides.

## Features
- **PowerPoint Content Extraction**: Extracts text content from slides using `UnstructuredPowerPointLoader`.
- **Script Generation**: Leverages OpenAI's GPT models to craft a detailed and engaging script for your presentation.
- **Customizable AI Settings**: Adjust the model (`gpt-4`, `gpt-3.5`, etc.) and creativity (temperature) to suit your needs.
- **Downloadable Script**: Download the generated script directly from the app.

## Project Structure
The project is organized into the following directories and files:

```plaintext
script_from_ppt/
├── __init__.py              # Marks the directory as a Python package
├── config.py                # Centralized configuration for the app
├── main.py                  # Main script for PowerPoint processing and script generation
├── powerpoint_processor.py  # Handles PowerPoint file extraction and processing
├── prompts.py               # Stores and manages AI prompt templates
├── script_generator.py      # Handles interaction with OpenAI's GPT models
streamlit_app/
├── app.py                   # Streamlit web application
.env                         # Stores OpenAI API key
.env.example                 # Example of the .env file for configuration
requirements.txt             # Python dependencies for the project
Script-from-ppt.ipynb        # Jupyter notebook for exploratory work
```

## Prerequisites
1. **Python 3.8 or higher**: Ensure you have Python installed on your system.
2. **OpenAI API Key**: Obtain your OpenAI API key from the [OpenAI website](https://platform.openai.com/) and add it to the `.env` file.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/suraj-yadav-aiml/ai-ppt-script-generator.git
   cd ai-ppt-script-generator
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv script_generation
   source script_generation/bin/activate    # Linux/Mac
   script_generation\Scripts\activate       # Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Environment**
   - Rename `.env.example` to `.env`:
     ```bash
     mv .env.example .env
     ```
   - Add your OpenAI API key in the `.env` file:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ```

## Usage

1. **Run the Streamlit App**
   ```bash
   streamlit run streamlit_app/app.py
   ```

2. **Upload a PowerPoint File**
   - Use the sidebar to upload a `.pptx` file.

3. **Configure AI Settings**
   - Select the AI model (e.g., GPT-4).
   - Adjust the creativity (temperature).

4. **Generate Script**
   - Click the "Generate Script" button to process the file and generate the script.
   - Download the script as a text file for further use.

## Example Workflow
1. Upload your PowerPoint file.
2. Adjust the AI settings in the sidebar.
3. Click "Generate Script" to produce the presentation script.
4. Review and download the generated script.


## License
This project is licensed under the MIT License.

## Author
Developed with ❣️ by [Suraj Yadav](https://github.com/suraj-yadav-aiml) 🎉