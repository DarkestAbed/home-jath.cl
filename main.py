"""jath.cl — personal landing site. Run with `uv run python main.py`."""

from fasthtml.common import FastHTML, serve
from starlette.staticfiles import StaticFiles

from jath.config import STATIC_DIR
from jath.routes import not_found, register

app = FastHTML(default_hdrs=False, exception_handlers={404: not_found})
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
register(app.route)

if __name__ == "__main__":
    serve(port=5001)
