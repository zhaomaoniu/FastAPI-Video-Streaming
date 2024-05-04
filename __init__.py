from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse


app = FastAPI()
video_path = Path("video.mp4")


@app.get("/video")
async def video_endpoint(request: Request):
    file_size = video_path.stat().st_size
    start, end = 0, file_size - 1
    range_header = request.headers.get("Range")
    if range_header:
        start, end = range_header.replace("bytes=", "").split("-")
        start = int(start)
        end = int(end) if end else file_size - 1
        status_code = 206
    else:
        status_code = 200

    def iterfile():
        with open(video_path, mode="rb") as file_like:
            file_like.seek(start)
            bytes_to_send = end - start + 1
            while bytes_to_send > 0:
                chunk_size = min(bytes_to_send, 1024 * 1024)  # 1MB chunks or less
                data = file_like.read(chunk_size)
                if not data:
                    break
                yield data
                bytes_to_send -= len(data)

    headers = {
        "Content-Range": f"bytes {start}-{end}/{file_size}",
        "Accept-Ranges": "bytes",
        "Content-Length": str(end - start + 1),
        "Content-Type": "video/mp4",
    }

    return StreamingResponse(
        iterfile(), status_code=status_code, headers=headers, media_type="video/mp4"
    )
