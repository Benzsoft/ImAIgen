# ImAIgen - Image Generation App by Benzsoft

The Image Generation App is a Python-based web application that utilizes the OpenAI API to generate images based on user-provided text prompts. The app provides an intuitive interface for users to input their prompts and view the corresponding generated images.

![App Screenshot](screenshot.png)

## Features

- User-friendly interface for entering text prompts.
- Integration with the OpenAI API for image generation.
- Display of the generated images within the app.
- Responsive design for a seamless user experience.
- Error handling to gracefully handle edge cases and provide informative messages.
- Additional customizable features such as image styles, dimensions, and templates (can be extended as per requirements).

## Installation

1. Clone the repository:


2. Navigate to the project directory:


3. Install the required dependencies:


4. Set up the OpenAI API:

- Obtain an API key from OpenAI.
- Copy the provided API key.

5. Configure the API key:

- Make a copy of `config.py.template` and rename it to `config.py`.
- Open `config.py` and replace `'YOUR_API_KEY'` with your actual OpenAI API key.

6. Run the application:


7. Open your web browser and visit [http://localhost:5000](http://localhost:5000).

8. Enter your text prompt and click "Generate Image".

9. View the generated image on the result page.

## Dependencies

The Image Generation App requires the following dependencies:

- Python 3.x
- Flask
- OpenAI Python library (included in requirements.txt)

## License

The Image Generation App is open-source software licensed under the MIT license. See [LICENSE](LICENSE) for more information.
