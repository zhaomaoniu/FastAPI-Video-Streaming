# FastAPI-Video-Streaming
A FastAPI application for handling video streaming requests.


## Installation
1. Clone the repository
```bash
git clone https://github.com/zhaomaoniu/FastAPI-Video-Streaming.git
```

2. Install the required packages
```bash
pdm install
```

3. Run the FastAPI application
```bash
pdm run uvicorn __init__:app --reload
```

4. Open the browser and navigate to `http://host:port/video` to view the video stream.

## Usage
The application is an example of how to handle video streaming requests using FastAPI.
Instead of using a rudimentary generator function to stream the video, the application uses a modified way to control the video streaming process in a more user-friendly way.


## License
This project is licensed under the Apache-2.0 License - see the [LICENSE](LICENSE) file for details.


## Acknowledgements
- [FastAPI](https://fastapi.tiangolo.com/)
- [How to stream local video to browser in FastAPI?](https://stackoverflow.com/questions/72923097/how-to-stream-local-video-to-browser-in-fastapi)
