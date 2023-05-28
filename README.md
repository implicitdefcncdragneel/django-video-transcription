# Video Transcription Tool

This is a Django project for a video transcription tool that allows users to upload youtube video link and get their transcriptions. The project consists of an app named `video_transcription_app` with `video_transcription_project` project.

## Project Structure

- `video_transcription_project`: Django project directory
- `video_transcription_app`: Django app directory
    - `models.py`: Contains the `Video` model for storing video information
    - `views.py`: Contains the `transcribe_video` view function for video upload and transcription
    - `urls.py`: Contains URL patterns for the `transcribe_video` view
- `templates/`: Directory for HTML templates
    - `base.html`: Base template to be extended by other templates
    - `transcribe_video.html`: Template for video upload
    - `transcription_result.html`: Template for transcription result

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/implicitdefcncdragneel/django-video-transcription.git
   ```

2. Change into the project directory:

   ```bash
   cd video_transcription_project
   ```

3. Create a virtual environment:

   ```bash
   python -m venv env
   ```

4. Activate the virtual environment:

   - For Linux/Mac:

     ```bash
     source env/bin/activate
     ```

   - For Windows:

     ```bash
     env\Scripts\activate
     ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

8. Open your web browser and access the application at `http://localhost:8000`.

## Usage

- To transcribe a video:
  1. Access the `transcribe_video` page by navigating to `http://localhost:8000/`.
  2. Enter the video URL in the provided form and submit it.
  3. The video will be downloaded and converted to an audio file.
  4. The audio will be transcribed using the SpeechRecognition library.
  5. The video information and transcript will be saved to the database.
  6. You will be redirected to the `transcription_result` page, where you can view the transcription result.

## Contact

For any questions or inquiries, please contact [chandranandan.chandrakar@gmail.com](mailto:chandranandan.chandrakar@gmail.com).