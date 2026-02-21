import itertools
import datetime
import sys

from spirecomm.communication.coordinator import Coordinator
from spirecomm.ai.agent import SimpleAgent
from spirecomm.spire.character import PlayerClass


# if __name__ == "__main__":
#     agent = SimpleAgent()
#     coordinator = Coordinator()
#     coordinator.signal_ready()
#     coordinator.register_command_error_callback(agent.handle_error)
#     coordinator.register_state_change_callback(agent.get_next_action_in_game)
#     coordinator.register_out_of_game_callback(agent.get_next_action_out_of_game)

#     # # Play games forever, cycling through the various classes
#     # for chosen_class in itertools.cycle(PlayerClass):
#     #     agent.change_class(chosen_class)
#     #     result = coordinator.play_one_game(chosen_class)

#     coordinator.run()

import logging
import os
from spirecomm.communication.coordinator import Coordinator
from spirecomm.ai.agent import AlphaStSAgent

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_DIR = os.path.join(BASE_DIR, "logs")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOG_FILE = os.path.join(LOG_DIR, "agent.log")

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(name)s] [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("Main")

if __name__ == "__main__":
    logger.info("--- Starting AlphaStS Agent ---")
    try:
        agent = AlphaStSAgent()
        coordinator = Coordinator()
        coordinator.signal_ready()
        coordinator.register_command_error_callback(agent.handle_error)
        coordinator.register_state_change_callback(agent.get_next_action_in_game)
        coordinator.register_out_of_game_callback(agent.get_next_action_out_of_game)
        coordinator.run()
    except Exception as e:
        logger.critical("Program execution error", exc_info=True)