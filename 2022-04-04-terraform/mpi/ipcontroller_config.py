import socket
from getpass import getuser
from urllib.request import urlopen, Request

# from traitlets.config import Config
# c = Config()
c = get_config()  # noqa

c.BroadcastScheduler.depth = 3
c.IPController.ip = "*"


# def get_metadata(key):
#     with urlopen(
#         Request(
#             f"http://metadata.google.internal/computeMetadata/v1/{key}",
#             headers={"Metadata-Flavor": "Google"},
#         )
#     ) as f:
#         return f.read().decode("ascii")
#
#
# project_id = get_metadata("project/project-id")
# zone = get_metadata("instance/zone").split("/")[-1]
# hostame = socket.gethostname()
#
#
# c.IPController.ssh_server = f"{hostname}.{zone}.{project_id}"

c.IPController.db_class = "NoDB"
