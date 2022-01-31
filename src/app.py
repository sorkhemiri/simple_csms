from os.path import join

from fastapi.openapi.docs import get_swagger_ui_html

from settings import env_config
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from router import main_router
from starlette.middleware.cors import CORSMiddleware

from settings.config import SOURCE_DIR

app = FastAPI(
    title=env_config.app_title,
    description=env_config.app_description,
    version=env_config.app_version,
)
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

app.include_router(main_router)

if env_config.debug:
    # loading OPEN API (SWAGGER) static files
    app.mount(
        "/static", StaticFiles(directory=join(SOURCE_DIR, "static")), name="static"
    )

    # route to swagger documents
    @app.get("/docs", include_in_schema=False)
    async def custom_swagger_ui_html():
        return get_swagger_ui_html(
            openapi_url=app.openapi_url,
            title=app.title + " - Swagger UI",
            oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
            swagger_js_url="/static/swagger-ui-bundle.js",
            swagger_css_url="/static/swagger-ui.css",
        )

if env_config.debug and __name__ == "__main__":
    # run the project locally for development
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=env_config.exposed_port, debug=True)
