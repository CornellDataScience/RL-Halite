# Python 2-3 Compatibility
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from six.moves import range, zip

import argparse
import os
import time
import logzero
import logging

from logzero import logger

# from models import FCQNet


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def main():

  # Parse args and set up logger #
  ################################
  parser = argparse.ArgumentParser(
    description="Trains a q-learning agent on the Cart-Pole-V1 task.")
  parser.add_argument("-n", "--name",
    type=str,
    default="%s" % time.strftime("cart-pole-q-learner_%Y%m%d_%H%M%S"),
    help="The name of the experiment being run. Used to identify different "
         "experiments of the same type. Will by default be named based on the "
         "current time.")
  parser.add_argument("-s", "--save-to", metavar="PATH",
    type=str,
    help="A path to the directory to save the results of the experiment. "
         "If not specified, the results will be saved in a new directory named "
         "the same as the --name argument in the directory where this script "
         "is located.")
  parser.add_argument("-l", "--load-from", metavar="PATH",
    type=str,
    help="This flag will cause the model to be loaded from a prior experiment "
         "located at the given path, rather than starting fresh. This is "
         "useful when loading a (partially) trained agent.")
  parser.add_argument("-v", "--verbosity", metavar="LEVEL",
    type=str.upper,
    nargs='?',
    default="INFO", const="DEBUG",
    choices=("CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"),
    help="Sets the console logger verbosity. Note that all logger messages "
         "will still be written to the logfile. Specifying this flag without "
         "a level will set the verbosity to DEBUG. (default: %(default)s) "
         "(choices: %(choices)s)")
  args = parser.parse_args()

  args.save_to = os.path.join(BASE_DIR, args.name)
  if not os.path.exists(args.save_to):
    os.mkdir(args.save_to)

  # Set up the logfile
  logzero.logfile(
    filename=os.path.join(args.save_to, 'log.txt'),
    mode='w',
    loglevel=logging.DEBUG)
  # Set the console's stderr to use the defined verbosity
  logger.handlers[0].setLevel(args.verbosity)
  logger.debug("Logger created and args parsed!")

  # Print the command line arguments the program ran with
  logger.info("Script location: %s" % __file__)
  logger.info("Parsed args: %s" % vars(args))

  # Initialize framework #
  ########################
  logger.info("Initializing framework...")
  # TODO: Actually initialize the framework
  # q_model = None  # FCQNet(...)
  # q_learner = None  # QLearner(...)
  # env = None  # CartPoleV1(...)

  # Run the agent-environment interface #
  #######################################
  logger.info("Running agent-environment interface...")
  # TODO: Actually run the interface


if __name__ == "__main__":
  main()
