
# Resume Generator

This is a Python-based Resume Generator that uses the Tkinter library for the graphical user interface (GUI) and the `fpdf` library to generate a PDF resume. This tool allows users to input their resume details and create a well-formatted PDF resume easily.

## Features

- **Graphical User Interface:** A user-friendly interface built with Tkinter for inputting resume details.
- **Automated PDF Generation:** Automatically formats and generates a PDF resume based on user input.
- **Customizable:** Users can input their name, contact information, summary, skills, experience, education, and projects.

## Prerequisites

- Python 3.x
- Tkinter (pre-installed with Python)
- `fpdf` library

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/resume-generator.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd resume-generator
   ```

3. **Install the required Python package:**

   ```bash
   pip install fpdf
   ```

## Usage

1. **Run the script:**

   ```bash
   python resume_generator.py
   ```

2. **Input your details:**

   - **Name:** Your full name.
   - **Phone:** Your contact number.
   - **Email:** Your email address.
   - **Address:** Your physical address.
   - **Summary:** A brief professional summary.
   - **Skills:** List your skills, separated by commas.
   - **Experience:** Provide details about your work experience.
   - **Education:** List your educational background.
   - **Projects:** Mention any relevant projects.

3. **Generate your resume:**
   - Click the "Generate Resume" button.
   - A PDF resume named `resume.pdf` will be created in the project directory.

## File Structure

```
resume-generator/
│
├── README.md
├── resume_generator.py
└── requirements.txt
```

- **`resume_generator.py`**: The main Python script that runs the GUI and generates the resume.
- **`README.md`**: This file, which contains information about the project.
- **`requirements.txt`**: (Optional) List of required Python packages.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to fork the repository and create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- **[fpdf](https://pyfpdf.readthedocs.io/en/latest/)**: The Python PDF library used to generate the resume.
- **[Tkinter](https://docs.python.org/3/library/tkinter.html)**: The Python library used for the graphical user interface.

