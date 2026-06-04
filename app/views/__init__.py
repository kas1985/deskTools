from app.views.dashboard import dashboard_view
from app.views.downloader import downloader_view
from app.views.gaming import gaming_view
from app.views.network import network_view
from app.views.processes import processes_view
from app.views.storage import storage_view


VIEWS = [
    dashboard_view,
    processes_view,
    gaming_view,
    downloader_view,
    storage_view,
    network_view,
]
