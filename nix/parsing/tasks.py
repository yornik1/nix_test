from nix import celery_app
import celery
from parsing.utils import parse
logger = celery.utils.log.get_task_logger(__name__)


@celery_app.task(
    name="parsing",
)
def task(n=100):
    parse(n)
    logger.info("parsing done!")
