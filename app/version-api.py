from podman import PodmanClient
from podman.errors import NotFound
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/version/{container_name}")
def get_version(container_name: str):
    try:
        with PodmanClient(base_url="unix:///run/podman/podman.sock") as client:
            container = client.containers.get(container_name)
            # Get version from image tag
            if container.image.tags:
                version = container.image.tags[0].split(':')[-1]
            else:
                # Fallback to image ID if no tags
                version = container.image.short_id
            return {"service": container_name, "version": version}
    except NotFound:
        raise HTTPException(status_code=404, detail=f"Container '{container_name}' not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))