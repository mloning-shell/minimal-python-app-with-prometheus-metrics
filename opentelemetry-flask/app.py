import random
from flask import Flask
import logging
from opentelemetry import metrics

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

meter = metrics.get_meter("diceroller.meter")
roll_counter = meter.create_counter(
    "dice.rolls", description="The number of rolls by value"
)


@app.route("/rolldice")
def roll_dice():
    result = str(roll())
    roll_counter.add(1, {"roll.value": result})
    logger.info("Player is rolling the dice: %s", result)
    return result


def roll():
    return random.randint(1, 6)
