# Data Faker

Data Faker is a tool designed to protect privacy and maintain confidentiality by anonymizing sensitive information in text data before passing it to language models like GPT-4. It provides a user-friendly interface for anonymizing and deanonymizing text using the Presidio Reversible Anonymizer.

## Features

- Anonymize sensitive information such as names, email addresses, phone numbers, and more
- Deanonymize previously anonymized text to recover the original information
- Maintain a separate anonymizer instance for each user session
- Simple and intuitive web-based interface using Gradio

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/data-faker.git
```

2. Navigate to the project directory:

```
cd data-faker
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

1. Run the application:

```
python app.py
```

2. Open your web browser and navigate to the provided URL (e.g., `http://localhost:7860`).

3. Enter the text you want to anonymize in the "Text to Convert" input box.

4. Click the "Generate Fake" button to anonymize the text. The anonymized text will appear in the "Output Text" box.

5. To deanonymize the text, click the "Revert Fake" button. The original text will be restored in the "Output Text" box.

6. To reset the anonymizer instance and clear the input and output boxes, click the "Reset" button.

## Configuration

The `AnonymiserManager` class in `anonymiser_manager.py` uses the Presidio Reversible Anonymizer to handle the anonymization and deanonymization process. You can customize the `analyzed_fields` parameter to specify the types of sensitive information you want to anonymize.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Presidio](https://github.com/microsoft/presidio) - Data anonymization library
- [Gradio](https://gradio.app/) - Web-based interface library